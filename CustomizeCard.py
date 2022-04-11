import bpy
import os
import bpy
import numpy as np
from bpy.props import StringProperty, BoolProperty, FloatProperty, IntProperty
from bpy_extras.io_utils import ImportHelper 
from bpy.types import Operator

scene = bpy.context.scene

#main Panel
class Main_Panel(bpy.types.Panel):
    bl_label = "Customize Card"
    bl_idname = "main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Card"
    
    def draw(self, context):
        layout = self.layout
        
        layout.operator("bake_sound")
        row = layout.row() 
        layout.operator("set_title")
        row = layout.row() 
        layout.operator("set_duration")
        row = layout.row() 
        layout.operator("change_background_texture")
        row = layout.row() 
        layout.operator("set_shape")
        row = layout.row() 
        layout.operator("change_sculpture")
        row = layout.row()        
              
class Change_Sculpture(bpy.types.Operator):
    bl_label = "Change Sculpture"
    bl_idname = "change_sculpture"
    
    sculpture_enum : bpy.props.EnumProperty(
        name= "",
        description="Select an option",
        items=[ 
            ('OP1', "Ammon", "Select"),
            ('OP2', "Zeus", "Select"),
            ('OP3', "Venus", "Select"),
            ('OP4', "Hera", "Select"),
            ('OP5', "Hercules", "Select"),
            ('OP6', "Dyionisos", "Select"),
            ('OP7', "Triton", "Select"),
            ('OP8', "Apollo", "Select")
        ]
    )    
       
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
        
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "sculpture_enum")
    
    def execute(self, context):
        
        if self.sculpture_enum == 'OP1':
            bpy.context.layer_collection.children['Ammon'].exclude = False
            bpy.context.layer_collection.children['Zeus'].exclude = True
            bpy.context.layer_collection.children['Venus'].exclude = True
            bpy.context.layer_collection.children['Hera'].exclude = True
            bpy.context.layer_collection.children['Hercules'].exclude = True
            bpy.context.layer_collection.children['Dyinisos'].exclude = True
            bpy.context.layer_collection.children['Triton'].exclude = True
            bpy.context.layer_collection.children['Apollo'].exclude = True
            
        if self.sculpture_enum == 'OP2':
            bpy.context.layer_collection.children['Ammon'].exclude = True
            bpy.context.layer_collection.children['Zeus'].exclude = False
            bpy.context.layer_collection.children['Venus'].exclude = True
            bpy.context.layer_collection.children['Hera'].exclude = True
            bpy.context.layer_collection.children['Hercules'].exclude = True
            bpy.context.layer_collection.children['Dyinisos'].exclude = True
            bpy.context.layer_collection.children['Triton'].exclude = True
            bpy.context.layer_collection.children['Apollo'].exclude = True

        if self.sculpture_enum == 'OP3':
            bpy.context.layer_collection.children['Ammon'].exclude = True
            bpy.context.layer_collection.children['Zeus'].exclude = True
            bpy.context.layer_collection.children['Venus'].exclude = False
            bpy.context.layer_collection.children['Hera'].exclude = True
            bpy.context.layer_collection.children['Hercules'].exclude = True
            bpy.context.layer_collection.children['Dyinisos'].exclude = True
            bpy.context.layer_collection.children['Triton'].exclude = True
            bpy.context.layer_collection.children['Apollo'].exclude = True
            
        if self.sculpture_enum == 'OP4':
            bpy.context.layer_collection.children['Ammon'].exclude = True
            bpy.context.layer_collection.children['Zeus'].exclude = True
            bpy.context.layer_collection.children['Venus'].exclude = True
            bpy.context.layer_collection.children['Hera'].exclude = False
            bpy.context.layer_collection.children['Hercules'].exclude = True
            bpy.context.layer_collection.children['Dyinisos'].exclude = True
            bpy.context.layer_collection.children['Triton'].exclude = True
            bpy.context.layer_collection.children['Apollo'].exclude = True
        
        if self.sculpture_enum == 'OP5':
            bpy.context.layer_collection.children['Ammon'].exclude = True
            bpy.context.layer_collection.children['Zeus'].exclude = True
            bpy.context.layer_collection.children['Venus'].exclude = True
            bpy.context.layer_collection.children['Hera'].exclude = True
            bpy.context.layer_collection.children['Hercules'].exclude = False
            bpy.context.layer_collection.children['Dyinisos'].exclude = True
            bpy.context.layer_collection.children['Triton'].exclude = True
            bpy.context.layer_collection.children['Apollo'].exclude = True 

        if self.sculpture_enum == 'OP6':
            bpy.context.layer_collection.children['Ammon'].exclude = True
            bpy.context.layer_collection.children['Zeus'].exclude = True
            bpy.context.layer_collection.children['Venus'].exclude = True
            bpy.context.layer_collection.children['Hera'].exclude = True
            bpy.context.layer_collection.children['Hercules'].exclude = True
            bpy.context.layer_collection.children['Dyinisos'].exclude = False
            bpy.context.layer_collection.children['Triton'].exclude = True
            bpy.context.layer_collection.children['Apollo'].exclude = True 
            
        if self.sculpture_enum == 'OP7':
            bpy.context.layer_collection.children['Ammon'].exclude = True
            bpy.context.layer_collection.children['Zeus'].exclude = True
            bpy.context.layer_collection.children['Venus'].exclude = True
            bpy.context.layer_collection.children['Hera'].exclude = True
            bpy.context.layer_collection.children['Hercules'].exclude = True
            bpy.context.layer_collection.children['Dyinisos'].exclude = True
            bpy.context.layer_collection.children['Triton'].exclude = False
            bpy.context.layer_collection.children['Apollo'].exclude = True

        if self.sculpture_enum == 'OP8':
            bpy.context.layer_collection.children['Ammon'].exclude = True
            bpy.context.layer_collection.children['Zeus'].exclude = True
            bpy.context.layer_collection.children['Venus'].exclude = True
            bpy.context.layer_collection.children['Hera'].exclude = True
            bpy.context.layer_collection.children['Hercules'].exclude = True
            bpy.context.layer_collection.children['Dyinisos'].exclude = True
            bpy.context.layer_collection.children['Triton'].exclude = True
            bpy.context.layer_collection.children['Apollo'].exclude = False
   
        
        return {'FINISHED'} 

class Set_Title(bpy.types.Operator):
    bl_idname = "set_title"
    bl_label = "Set Song Title"
    bl_options = {'REGISTER', 'UNDO'}
    Name : StringProperty()

    def execute(self, context):
        bpy.data.node_groups["Script"].nodes["ScriptedString"].inputs[0].default_value = self.Name
        if os.path.isdir(os.path.join('D:\ManaSounds',self.Name)):
            print("dir exists already")
        else:
            os.mkdir(os.path.join('D:\ManaSounds',self.Name))
        
        filename = bpy.path.basename(bpy.data.filepath)
        filename = os.path.splitext(filename)[0]
        
        if filename:
            bpy.context.scene.render.filepath = os.path.join(os.path.join("D:\ManaSounds",self.Name), self.Name)
        
            return {'FINISHED'}

class Set_Duration(bpy.types.Operator):
    bl_idname = "set_duration"
    bl_label = "Set Duration"
    bl_options = {'REGISTER', 'UNDO'}
    Minutes : IntProperty()
    Seconds : IntProperty()
    def execute(self, context):
        frameMinutes =self.Minutes * 60
        frameSeconds = self.Seconds + frameMinutes
        framesTotal = frameSeconds * 24  
    
        #letztes keyframe zuerst löschen   
        deleteEndKey = bpy.data.scenes["Scene"].frame_end
        bpy.data.node_groups["Script"].nodes["Combine XYZ.001"].inputs[1].keyframe_delete('default_value', frame = deleteEndKey)
        
        #End frame setzten eingabe verursacht blender crashing loop
        bpy.data.scenes["Scene"].frame_end = framesTotal
        
        #neues letztes keyframe einfügen 
        bpy.data.node_groups["Script"].nodes["Combine XYZ.001"].inputs[1].default_value=1
        bpy.data.node_groups["Script"].nodes["Combine XYZ.001"].inputs[1].keyframe_insert('default_value', frame = framesTotal)
        
        #set Timer absteigend
        bpy.data.node_groups["Script"].nodes["ScriptedValue"].outputs[0].default_value=framesTotal
        return {'FINISHED'}

class Change_Font_Timer(Operator, ImportHelper): 
    bl_idname = "change_font_timer" 
    bl_label = "Change Timer Font" 
    filter_glob: StringProperty( 
        default='*.TTF', 
        options={'HIDDEN'} 
    ) 
    some_boolean: BoolProperty( 
        name='Do a thing', 
        description='Do a thing with the file you\'ve selected', 
        default=True, 
    ) 
    def execute(self, context): 
        
        filename, extension = os.path.splitext(self.filepath) 
        path_font = self.filepath
        print('Selected file:', self.filepath) 
        print('File name:', filename) 
        print('File extension:', extension) 
        print('Some Boolean:', self.some_boolean) 
        data_font = bpy.data.fonts.load(path_font)
        bpy.data.node_groups["Script"].nodes["ScriptedTimerA"].font = data_font
        bpy.data.node_groups["Script"].nodes["ScriptedTimerB"].font = data_font
        
        return {'FINISHED'}

class Bake_Sound(Operator, ImportHelper): 
    bl_idname = "bake_sound" 
    bl_label = "Bake Sound" 
    filter_glob: StringProperty( 
        default='*.mp3', 
        options={'HIDDEN'} 
    ) 
    some_boolean: BoolProperty( 
        name='Do a thing', 
        description='Do a thing with the file you\'ve selected', 
        default=True, 
    ) 
    def execute(self, context): 
        
        filename, extension = os.path.splitext(self.filepath) 
        path_font = self.filepath
        print('Selected file:', self.filepath) 
        print('File name:', filename) 
        print('File extension:', extension) 
        print('Some Boolean:', self.some_boolean) 
        
        context = bpy.context
        scene = context.scene

        seq = scene.sequence_editor

        # stips meta_strips 
        for strip in seq.sequences:
            print(strip.name)
        # all strips
        for strip in seq.sequences_all:
            print(strip.name)
        #remove
        for strip in seq.sequences:
            seq.sequences.remove(strip)   
        
        bpy.context.area.type = 'SEQUENCE_EDITOR'
        bpy.ops.sequencer.sound_strip_add(filepath=self.filepath, files=[{"name":filename, "name":filename}], relative_path=True, frame_start=0, channel=1)
        bpy.context.area.type = 'VIEW_3D'
        
        ob = bpy.context.scene.objects["MainCube"]       # Get the object
        bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
        bpy.context.view_layer.objects.active = ob   # Make the cube the active object 
        ob.select_set(True)  
        
        node = bpy.data.node_groups["Geometry Nodes"].nodes["Value.001"]
        nodeGroup = bpy.data.node_groups["Geometry Nodes"]
        bpy.context.area.type = 'NODE_EDITOR'
        node.select = True
        nodeGroup.nodes.active = node
        bpy.data.scenes["Scene"].frame_current = 0#set current frame
        bpy.context.area.type = "GRAPH_EDITOR"#open graph editor
        bpy.ops.graph.sound_bake(filepath=self.filepath)#works when node is selected
        bpy.context.area.type = "VIEW_3D"#go back to 3d view
        return {'FINISHED'}

class Change_Font_Title(Operator, ImportHelper): 
    bl_idname = "change_font_title" 
    bl_label = "Change Title Font" 
    filter_glob: StringProperty( 
        default='*.TTF', 
        options={'HIDDEN'} 
    ) 
    some_boolean: BoolProperty( 
        name='Do a thing', 
        description='Do a thing with the file you\'ve selected', 
        default=True, 
    ) 
    def execute(self, context): 
        
        filename, extension = os.path.splitext(self.filepath) 
        path_font = self.filepath
        print('Selected file:', self.filepath) 
        print('File name:', filename) 
        print('File extension:', extension) 
        print('Some Boolean:', self.some_boolean) 
        data_font = bpy.data.fonts.load(path_font)
        bpy.data.node_groups["Script"].nodes["ScriptedString"].font = data_font
        
        return {'FINISHED'}

class Change_Background_Texture(bpy.types.Operator):
    bl_label = "Change Background Texture"
    bl_idname = "change_background_texture"
    
    background_enum : bpy.props.EnumProperty(
        name= "",
        description="Select an option",
        items=[ 
            ('OP1', "Wood", "Select Wood Texture"),
            ('OP2', "Voronoi", "Select Voronoi Texture"),
            ('OP3', "Stucci", "Select Stucci Texture"),
            ('OP5', "Musgrave", "Select Musgrave Texture"),
            ('OP7', "Magic", "Select Magic Texture")
        ]
    
    )    
       
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
        
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "background_enum")
    
    def execute(self, context):
        
        if self.background_enum == 'OP1':
            bpy.data.textures["Texture"].type = 'WOOD'
            
        if self.background_enum == 'OP2':
            bpy.data.textures["Texture"].type = 'VORONOI'

        if self.background_enum == 'OP3':
            bpy.data.textures["Texture"].type = 'STUCCI'
            
        if self.background_enum == 'OP4':
            bpy.data.textures["Texture"].type = 'NOISE'
        
        if self.background_enum == 'OP5':
            bpy.data.textures["Texture"].type = 'MUSGRAVE'  

        if self.background_enum == 'OP6':
            bpy.data.textures["Texture"].type = 'MARBLE'  
            
        if self.background_enum == 'OP7':
            bpy.data.textures["Texture"].type = 'MAGIC' 

        if self.background_enum == 'OP8':
            bpy.data.textures["Texture"].type = 'CLOUDS' 

        if self.background_enum == 'OP9':
            bpy.data.textures["Texture"].type = 'BLEND'     
        
        return {'FINISHED'}    

class Set_Shape(bpy.types.Operator):
    bl_label = "Change Shape"
    bl_idname = "set_shape"
    
    background_enum : bpy.props.EnumProperty(
        name= "",
        description="Select an option",
        items=[ 
            ('OP1', "Cube", "Select Cube"),
            ('OP2', "Sphere", "Select Sphere"),
            ('OP3', "Pyramid", "Select Pyramid"),
            ('OP4',"Cylinder", "Select Cylinder"),
            ('OP5',"Torus","Select Torus"),
            
        ]
    
    )    
       
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
        
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "background_enum")
    
    def execute(self, context):
        
        if self.background_enum == 'OP1':
            bpy.data.objects["Pyramid"].hide_render = True
            bpy.data.objects["Pyramid"].hide_set(True)
            bpy.data.objects["Kugel"].hide_render = True
            bpy.data.objects["Kugel"].hide_set(True)
            bpy.data.objects["Cube"].hide_render = False
            bpy.data.objects["Cube"].hide_set(False) 
            bpy.data.objects["Torus"].hide_render = True
            bpy.data.objects["Torus"].hide_set(True) 
            bpy.data.objects["Cylinder"].hide_render = True
            bpy.data.objects["Cylinder"].hide_set(True) 

            
        if self.background_enum == 'OP2':
            bpy.data.objects["Pyramid"].hide_render = True
            bpy.data.objects["Pyramid"].hide_set(True)
            bpy.data.objects["Kugel"].hide_render = False
            bpy.data.objects["Kugel"].hide_set(False)
            bpy.data.objects["Cube"].hide_render = True
            bpy.data.objects["Cube"].hide_set(True) 
            bpy.data.objects["Torus"].hide_render = True
            bpy.data.objects["Torus"].hide_set(True) 
            bpy.data.objects["Cylinder"].hide_render = True
            bpy.data.objects["Cylinder"].hide_set(True) 

        if self.background_enum == 'OP3':
            bpy.data.objects["Pyramid"].hide_render = False
            bpy.data.objects["Pyramid"].hide_set(False)
            bpy.data.objects["Kugel"].hide_render = True
            bpy.data.objects["Kugel"].hide_set(True)
            bpy.data.objects["Cube"].hide_render = True
            bpy.data.objects["Cube"].hide_set(True) 
            bpy.data.objects["Torus"].hide_render = True
            bpy.data.objects["Torus"].hide_set(True) 
            bpy.data.objects["Cylinder"].hide_render = True
            bpy.data.objects["Cylinder"].hide_set(True) 
            
        if self.background_enum == 'OP4':
            bpy.data.objects["Pyramid"].hide_render = True
            bpy.data.objects["Pyramid"].hide_set(True)
            bpy.data.objects["Kugel"].hide_render = True
            bpy.data.objects["Kugel"].hide_set(True)
            bpy.data.objects["Cube"].hide_render = True
            bpy.data.objects["Cube"].hide_set(True) 
            bpy.data.objects["Torus"].hide_render = True
            bpy.data.objects["Torus"].hide_set(True) 
            bpy.data.objects["Cylinder"].hide_render = False
            bpy.data.objects["Cylinder"].hide_set(False) 
    
        if self.background_enum == 'OP5':
            bpy.data.objects["Pyramid"].hide_render = True
            bpy.data.objects["Pyramid"].hide_set(True)
            bpy.data.objects["Kugel"].hide_render = True
            bpy.data.objects["Kugel"].hide_set(True)
            bpy.data.objects["Cube"].hide_render = True
            bpy.data.objects["Cube"].hide_set(True) 
            bpy.data.objects["Torus"].hide_render = False
            bpy.data.objects["Torus"].hide_set(False) 
            bpy.data.objects["Cylinder"].hide_render = True
            bpy.data.objects["Cylinder"].hide_set(True) 
        
        return {'FINISHED'} 
classes = [Main_Panel, Change_Background_Texture, Set_Duration, Set_Shape, Set_Title, Bake_Sound, Change_Sculpture]

def register():
     
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

    

  