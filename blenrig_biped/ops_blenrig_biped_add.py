import bpy

class Operator_BlenRig5_Add_Biped(bpy.types.Operator):    
    
    bl_idname = "blenrig5.add_biped_rig"   
    bl_label = "BlenRig 5 Add Biped Rig"   
    bl_description = "Generates BlenRig 5 biped rig"    
    bl_options = {'REGISTER', 'UNDO',}     


    @classmethod
    def poll(cls, context):                            #method called by blender to check if the operator can be run
        return bpy.context.scene != None
    
    blenrig_armature_name = []
    blenrig_action_names = []
    blenrig_lattice_names = []

    from BlenRig5.blenrig_biped.add_bone_shapes import add_shape_objects
    from BlenRig5.blenrig_biped.add_armature import add_blenrig_armature  
    from BlenRig5.blenrig_biped.add_data_id_properties import add_data_id_properties  
    from BlenRig5.blenrig_biped.add_pbones_id_properties import add_pbones_id_properties   
    from BlenRig5.blenrig_biped.add_armature_groups import add_armature_groups       
    from BlenRig5.blenrig_biped.add_pbones_properties import add_pbones_properties              
    from BlenRig5.blenrig_biped.add_armature_actions import add_armature_actions  
    from BlenRig5.blenrig_biped.add_pbones_constraints import add_pbones_constraints  
    from BlenRig5.blenrig_biped.add_armature_drivers import add_armature_drivers  
    from BlenRig5.blenrig_biped.add_lattices import add_lattices  
    from BlenRig5.blenrig_biped.add_mdef_cage import add_mdef_cage  
    from BlenRig5.blenrig_biped.add_proxy_model import add_proxy_model  

############################ Distribute Objects ############################ 
    
    def distrubute_objects(self, context):

        for ob in bpy.data.objects:
            for N in self.blenrig_lattice_names:
                if ob.name == N:
                    ob.layers = (False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False)
            for N in self.blenrig_armature_name:
                if ob.name == N:
                    ob.layers = (False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False)        
                    bpy.context.scene.objects.active = ob
        bpy.context.scene.layers[10] = True
        
####### Create BlenRig Rig #######        

    def execute(self, context):
        self.add_shape_objects(context)
        self.add_blenrig_armature(context)
        self.add_data_id_properties(context)
        self.add_pbones_id_properties(context)
        self.add_armature_groups(context)
        self.add_pbones_properties(context)
        self.add_armature_actions(context)
        self.add_pbones_constraints(context)
        self.add_armature_drivers(context)
        self.add_lattices(context)
        self.add_mdef_cage(context)
        self.add_proxy_model(context)
        self.distrubute_objects(context)
        
        return{'FINISHED'}   
            