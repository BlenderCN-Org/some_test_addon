bl_info = {
    "name": "Some Test Addon",
    "author": "----",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "category": "User Interface",
}

import bpy

from .addons import boolean_2d_union
from boolean_2d_union import Boolean2DUnion

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
