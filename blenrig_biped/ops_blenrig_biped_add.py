import bpy
import os

class Operator_BlenRig5_Add_Biped(bpy.types.Operator):    
    
    bl_idname = "blenrig5.add_biped_rig"   
    bl_label = "BlenRig 5 Add Biped Rig"   
    bl_description = "Generates BlenRig 5 biped rig"    
    bl_options = {'REGISTER', 'UNDO',}     


    @classmethod
    def poll(cls, context):                            #method called by blender to check if the operator can be run
        return bpy.context.scene != None
       
    def import_blenrig_biped(self, context):
        opath = "//blenrig_biped.blend\\Group\\blenrig_biped"
        s = os.sep
        dpath=''
        fpath=''
        
        for p in bpy.utils.script_paths():
            testfname= p + '%saddons%sBlenRig%sblenrig_biped%sblenrig_biped.blend' % (s,s,s,s)
            print(testfname)
            if os.path.isfile(testfname):
                fname=testfname
                dpath = p + '%saddons%sBlenRig%sblenrig_biped%sblenrig_biped.blend\\Group\\' % (s, s, s, s)
                break
        # DEBUG
        #print('import_object: ' + opath)
        bpy.ops.wm.append(
            filepath=opath,
            filename="blenrig_biped",
            directory=dpath,
            filemode=1,
            link=False,
            autoselect=True,
            active_layer=False,
            instance_groups=False
            )

    def set_pose(self, context):
        bpy.context.scene.layers[10] = True  
        
        active = []
        
        for ob in bpy.context.selected_objects:
            if ob.type == 'ARMATURE':
                active[:] = []
                active.append(ob.name)
                print (active[:])
                                
        bpy.ops.object.select_all(action='DESELECT')
        
        for ob in bpy.data.objects:
            if ob.name in active:
                bpy.context.scene.objects.active = ob
                bpy.ops.object.mode_set(mode='POSE')                         

    def execute(self, context):
        self.import_blenrig_biped(context)
        self.set_pose(context)
        return{'FINISHED'}  