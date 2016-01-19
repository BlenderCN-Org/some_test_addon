bl_info = {
    "name": "Some Test Addon",
    "author": "----",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "category": "User Interface",
}

import bpy

from .included_addons import boolean_2d_union


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
