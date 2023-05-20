import bpy
class TestPanel(bpy.types.Panel):
	bl_label = "something"
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_category = "somethingElse"
	bl_context = "mesh_edit"

	def draw(self,context):
		layout = self.layout

		row = layout.row()
		row.operator('object.something',text='Select By Vertex Color')