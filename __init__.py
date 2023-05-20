bl_info = {
    "name":"Select by Vertex Color",
    "blender":(2,80,0),
    "category":"Object"
}

import bpy

from . select_operator import SelectVertexColor
from . select_panel import TestPanel

classes = (SelectVertexColor,TestPanel)

register, unregister = bpy.utils.register_classes_factory(classes)


# def menu_func(self,context):
#     self.layout.operator(SelectVertexColor.bl_idname,SelectVertexColor.bl_label)

# def register():
    # bpy.utils.register_class(SelectVertexColor)
    # bpy.types.VIEW3D_MT_object.append(menu_func)
# def unregister():
#     bpy.utils.unregister_class(SelectVertexColor)
#     bpy.types.VIEW3D_MT_object.remove(menu_func)
    
    

# register()
