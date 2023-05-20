import bpy
import bmesh
import math
from mathutils import Color

class SelectVertexColor(bpy.types.Operator):
	bl_idname="object.something"
	bl_label="Simple operator"
	bl_description="select by vertex"
	
	def execute(self, context):
		print("Start")
		threshold = .1
		currentObj = bpy.context.object
		

		bpy.ops.object.mode_set(mode="OBJECT")

		bpy.ops.object.editmode_toggle()
		bpy.ops.mesh.remove_doubles(threshold=0.0001,use_unselected=True)
		bpy.ops.object.editmode_toggle()
		
		# colors = obj.data.vertex_colors.active.data
		print(currentObj.data)
		colors = currentObj.data.vertex_colors.active.data
		# selected_polygons = list(filter(lambda p: p.select, obj.data.polygons))
		colorList = []
		for i in colors:
			# print(i.color)
			found = False
			# print(colorList)
			for v in colorList:
				
				# print(v[0])
				# print(i.color[1])
				# print(v[1] == i.color[1])
				# print(v[2] == i.color[2])
				# print(v[3] == i.color[3])
				# print(v[1] == i.color[1] and v[2] == i.color[2] and v[3] == i.color[3])
				if v[0] == i.color[0] and v[1] == i.color[1] and v[2] == i.color[2] and v[3] == i.color[3]:
					found = True
			if not found:
				colorList.append([i.color[0],i.color[1],i.color[2],i.color[3]])
		counter = 0
		mesh_list = []
		for i in colorList:
			# obj = bpy.context.object
			# print(obj.name)
			colors = currentObj.data.vertex_colors.active.data
			# p = selected_polygons[0]
			# r = g = b = 0
			# for i in p.loop_indices:
			# 	c = colors[i].color
			# 	r += c[0]
			# 	g += c[1]
			# 	b += c[2]
			# r /= p.loop_total
			# g /= p.loop_total
			# b /= p.loop_total
			target = Color((i[0], i[1], i[2]))
			
			for p in currentObj.data.polygons:
				r = g = b = 0
				testR = None
				for i in p.loop_indices:
					c = colors[i].color
					# print()
					r += c[0]
					g += c[1]
					b += c[2]
				r /= p.loop_total
				g /= p.loop_total
				b /= p.loop_total
				source = Color((r, g, b))

				# print(target, source)

				if (source.r == target.r and
					source.g == target.g and
					source.b == target.b):

					p.select = True
				else:
					p.select = False
			me = currentObj.data
			bm = bmesh.new()
			bm.from_mesh(me)
			mesh2 = bm.copy()
			bm.verts.ensure_lookup_table()
			
			
			selected_faces1 = list(filter(lambda p: p.select, bm.faces))
			selected_faces2 = list(filter(lambda p: not p.select, mesh2.faces))
			bmesh.ops.delete(mesh2,geom=selected_faces2,context='FACES')
			selected_edges = list(filter(lambda p: p.select and p.is_valid, mesh2.edges))
			selected_vertices = list(filter(lambda p: p.select and p.is_valid, bm.verts))
			bmesh.ops.remove_doubles(bm,verts=selected_vertices,dist=0.0001)
			bmesh.ops.dissolve_limit(mesh2,angle_limit=math.radians(5),use_dissolve_boundaries=False,edges=selected_edges)
			bmesh.ops.delete(bm,geom=selected_faces1,context='FACES')
			
			
			mesh_name="test"+str(counter)
			mesh_data = bpy.data.meshes.new(mesh_name)
			newMat = bpy.data.materials.new(name='Material')
			newMat.use_nodes = True
			mesh_data.materials.append(newMat)
			mesh_obj = bpy.data.objects.new(mesh_data.name, mesh_data)
			mesh2.to_mesh(mesh_obj.data)
			mesh2.free()
			
			bpy.context.collection.objects.link(mesh_obj)

			bpy.context.view_layer.objects.active = mesh_obj
			bpy.ops.object.editmode_toggle()
			bpy.ops.mesh.remove_doubles(threshold=0.0001,use_unselected=True)
			bpy.ops.mesh.dissolve_limited(angle_limit=math.radians(5),use_dissolve_boundaries=False,delimit={'NORMAL'})

			bpy.ops.object.editmode_toggle()

			bm.to_mesh(me)
			bm.free()
			mesh_list.append(mesh_obj)
			counter+=1

			
			
			
			mesh_data.update()

		# bpy.ops.object.editmode_toggle()
		counter = 0
		for i in range(0,len(colorList)):
			print("test"+str(i))
			bpy.context.collection.objects["test"+str(i)].select_set(True)

		
		
		bpy.context.view_layer.objects.active = currentObj

		mesh = currentObj.data
		# bm = bmesh.new()
		# bm.from_mesh(me)
		bpy.ops.object.join()
		# for i,v in mesh.edges:
		# 	v.select = True
		bpy.ops.object.editmode_toggle()
		bpy.ops.mesh.remove_doubles(threshold=0.0001,use_unselected=True)
		bpy.ops.object.editmode_toggle()


		
		# bmesh.ops.dissolve_limit(bm,angle_limit=math.radians(5),use_dissolve_boundaries=True,faces=bm.faces)
		# bm.to_mesh(me)
		# bmesh.ops.remove_doubles(bm,verts=bm.verts,dist=0.0001)
		# bm.to_mesh(me)
		# bm.free()
		# objects = bpy.data.objects
		for block in bpy.data.meshes:
			if block.users == 0:
				bpy.data.meshes.remove(block)

		for block in bpy.data.materials:
			if block.users == 0:
				bpy.data.materials.remove(block)
		
		return {'FINISHED'}
