import bpy

############################ Add Lattices ############################ 

def add_lattices(self, context):
    
    self.blenrig_lattice_names[:] = []
    lattice_name = []
    vgroup_name = []

    def add_lattice(l_name, l_parent_type, l_parent_bone, l_location, l_rotation, l_scale, l_int_type_u, l_int_type_v, l_int_type_w, l_points_u, l_points_v, l_points_w):
        scene = bpy.context.scene
        lattice_name[:] = []
        
        lattice = bpy.data.lattices.new(l_name)
        lattice_ob = bpy.data.objects.new(l_name, lattice)
        lattice_ob.parent = bpy.data.objects[self.blenrig_armature_name[0]]
        lattice_ob.parent_type = l_parent_type
        lattice_ob.parent_bone = l_parent_bone
        lattice_ob.location[:] = l_location
        lattice_ob.rotation_euler[:] = l_rotation
        lattice_ob.scale[:] = l_scale
        lattice_ob.data.interpolation_type_u = l_int_type_u
        lattice_ob.data.interpolation_type_v = l_int_type_v
        lattice_ob.data.interpolation_type_w = l_int_type_w
        lattice_name.append(lattice_ob.name)
        self.blenrig_lattice_names.append(lattice_ob.name)
        scene.objects.link(lattice_ob)
        scene.update()    
        lattice_ob.data.points_u = l_points_u
        lattice_ob.data.points_v = l_points_v
        lattice_ob.data.points_w = l_points_w    

    def add_vgroups(l_vg_name):
        vgroup_name[:] = []
        for ob in bpy.data.objects:
            if ob.name == lattice_name[0]:
                vg = ob.vertex_groups.new(l_vg_name)
                vgroup_name.append(vg.name)
        
    def add_vg_weights(l_vg_point, l_vg_weight):
        for ob in bpy.data.objects:
            if ob.name == lattice_name[0]:
                for vg in ob.vertex_groups:
                    if vg.name == vgroup_name[0]:
                        vg.add([l_vg_point],l_vg_weight, 'REPLACE')
                        
    def add_mod(m_name, m_type, m_strength, m_subtarget, m_vgroup):
        for ob in bpy.data.objects:
            if ob.name == lattice_name[0]:
                mod = ob.modifiers.new(m_name, m_type)
                mod.object = bpy.data.objects[self.blenrig_armature_name[0]]     
                mod.strength = m_strength             
                mod.subtarget = m_subtarget
                mod.vertex_group = m_vgroup     
                bpy.context.scene.objects.active = ob

                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.lattice.select_all(action='SELECT')
                for mod in ob.modifiers:
                    if mod.type == 'HOOK':
                        bpy.ops.object.hook_reset(modifier=mod.name)
                bpy.ops.object.mode_set(mode='OBJECT')                
                        
                        
    # Add lattices

    add_lattice('LATTICE_BODY', 'BONE', 'lattice_body', (-8.63926601368803e-08, -0.00030263327062129974, 1.2091856002807617), (0.024332890287041664, 1.5453298640721869e-09, 3.608138454680443e-09), (0.5012080073356628, 0.42478740215301514, 0.7450575828552246), 'KEY_BSPLINE', 'KEY_BSPLINE', 'KEY_BSPLINE', 5, 4, 4)
    add_vgroups('belly_ctrl')
    add_vg_weights(20,1.0)
    add_vg_weights(21,1.0)
    add_vg_weights(22,1.0)
    add_vg_weights(23,1.0)
    add_vg_weights(24,1.0)
    add_vg_weights(40,1.0)
    add_vg_weights(41,1.0)
    add_vg_weights(42,1.0)
    add_vg_weights(43,1.0)
    add_vg_weights(44,1.0)
    add_vg_weights(60,1.0)
    add_vg_weights(61,1.0)
    add_vg_weights(62,1.0)
    add_vg_weights(63,1.0)
    add_vg_weights(64,1.0)
    add_vgroups('butt_ctrl')
    add_vg_weights(10,1.0)
    add_vg_weights(11,1.0)
    add_vg_weights(12,1.0)
    add_vg_weights(13,1.0)
    add_vg_weights(14,1.0)
    add_vg_weights(15,1.0)
    add_vg_weights(16,1.0)
    add_vg_weights(17,1.0)
    add_vg_weights(18,1.0)
    add_vg_weights(19,1.0)
    add_vg_weights(30,1.0)
    add_vg_weights(31,1.0)
    add_vg_weights(32,1.0)
    add_vg_weights(33,1.0)
    add_vg_weights(34,1.0)
    add_vg_weights(35,1.0)
    add_vg_weights(36,1.0)
    add_vg_weights(37,1.0)
    add_vg_weights(38,1.0)
    add_vg_weights(39,1.0)
    add_mod('belly_ctrl', 'HOOK', 1.0, 'belly_ctrl', 'belly_ctrl')
    add_mod('butt_ctrl', 'HOOK', 1.0, 'butt_ctrl', 'butt_ctrl')
    add_lattice('LATTICE_HEAD', 'BONE', 'head_def_mstr', (-3.72880448740176e-10, -0.04017431288957596, 1.6862335205078125), (0.08672714233398438, 1.923316354299712e-17, 8.345392112822994e-19), (0.24261817336082458, 0.3338454067707062, 0.2790469229221344), 'KEY_BSPLINE', 'KEY_BSPLINE', 'KEY_BSPLINE', 2, 3, 4)
    add_vgroups('face_toon_up')
    add_vg_weights(12,1.0)
    add_vg_weights(13,1.0)
    add_vg_weights(14,1.0)
    add_vg_weights(15,1.0)
    add_vg_weights(16,1.0)
    add_vg_weights(17,1.0)
    add_vg_weights(18,1.0)
    add_vg_weights(19,1.0)
    add_vg_weights(20,1.0)
    add_vg_weights(21,1.0)
    add_vg_weights(22,1.0)
    add_vg_weights(23,1.0)
    add_vgroups('face_toon_mid')
    add_vg_weights(6,1.0)
    add_vg_weights(7,1.0)
    add_vg_weights(8,1.0)
    add_vg_weights(9,1.0)
    add_vg_weights(10,1.0)
    add_vg_weights(11,1.0)
    add_vgroups('face_toon_low')
    add_vg_weights(0,1.0)
    add_vg_weights(1,1.0)
    add_mod('face_toon_up', 'HOOK', 1.0, 'face_toon_up', 'face_toon_up')
    add_mod('face_toon_mid', 'HOOK', 1.0, 'face_toon_mid', 'face_toon_mid')
    add_mod('face_toon_low', 'HOOK', 1.0, 'face_toon_low', 'face_toon_low')
    add_lattice('LATTICE_MOUTH', 'BONE', 'face_mstr_str_1', (-2.8826318612118484e-06, -0.1255491077899933, 1.5817996263504028), (0.0075166733004152775, -2.649082125572022e-05, -5.460783722810447e-05), (0.21389998495578766, 0.1337505728006363, 0.16382871568202972), 'KEY_BSPLINE', 'KEY_BSPLINE', 'KEY_BSPLINE', 2, 2, 3)
    add_vgroups('lattice_mouth')
    add_vg_weights(0,1.0)
    add_vg_weights(1,1.0)
    add_vg_weights(4,1.0)
    add_vg_weights(5,1.0)
    add_mod('lattice_mouth', 'HOOK', 1.0, 'lattice_mouth', 'lattice_mouth')
    add_lattice('LATTICE_BROW', 'BONE', 'face_mstr_str_3', (-3.3360704492224613e-06, -0.10098646581172943, 1.7232903242111206), (0.000719951291102916, -3.685006595333107e-05, -5.4009138693800196e-05), (0.16859573125839233, 0.08979645371437073, 0.061545390635728836), 'KEY_BSPLINE', 'KEY_BSPLINE', 'KEY_BSPLINE', 5, 2, 4)
    add_vgroups('toon_brow_L')
    add_vg_weights(13,1.0)
    add_vg_weights(23,1.0)
    add_vgroups('toon_brow_R')
    add_vg_weights(11,1.0)
    add_vg_weights(21,1.0)
    add_mod('toon_brow_L', 'HOOK', 1.0, 'toon_brow_L', 'toon_brow_L')
    add_mod('toon_brow_R', 'HOOK', 1.0, 'toon_brow_R', 'toon_brow_R')
    add_lattice('LATTICE_EYE_R', 'BONE', 'eye_mstr_str_R', (-0.036970000714063644, -0.09232743084430695, 1.682620882987976), (0.0, -0.0, 3.1415927410125732), (0.06499999761581421, -0.06520706415176392, 0.06520706415176392), 'KEY_BSPLINE', 'KEY_BSPLINE', 'KEY_BSPLINE', 3, 2, 3)
    add_vgroups('R')
    add_vg_weights(2,0.5)
    add_vg_weights(5,0.5)
    add_vg_weights(8,1.0)
    add_vg_weights(11,1.0)
    add_vg_weights(14,0.5)
    add_vg_weights(17,0.5)
    add_vgroups('L')
    add_vg_weights(0,0.5)
    add_vg_weights(3,0.5)
    add_vg_weights(6,1.0)
    add_vg_weights(9,1.0)
    add_vg_weights(12,0.5)
    add_vg_weights(15,0.5)
    add_vgroups('UP')
    add_vg_weights(12,0.5)
    add_vg_weights(13,1.0)
    add_vg_weights(14,0.5)
    add_vg_weights(15,0.5)
    add_vg_weights(16,1.0)
    add_vg_weights(17,0.5)
    add_vgroups('LOW')
    add_vg_weights(0,0.5)
    add_vg_weights(1,1.0)
    add_vg_weights(2,0.5)
    add_vg_weights(3,0.5)
    add_vg_weights(4,1.0)
    add_vg_weights(5,0.5)
    add_vgroups('lattice_eye_R')
    add_vg_weights(7,1.0)
    add_vg_weights(10,1.0)
    add_mod('lattice_eye_R', 'HOOK', 1.0, 'lattice_eye_R', 'lattice_eye_R')
    add_mod('toon_eye_out_R', 'HOOK', 1.0, 'toon_eye_out_R', 'R')
    add_mod('toon_eye_in_R', 'HOOK', 1.0, 'toon_eye_in_R', 'L')
    add_mod('toon_eye_up_R', 'HOOK', 1.0, 'toon_eye_up_R', 'UP')
    add_mod('toon_eye_low_R', 'HOOK', 1.0, 'toon_eye_low_R', 'LOW')
    add_lattice('LATTICE_EYE_L', 'BONE', 'eye_mstr_str_L', (0.036968424916267395, -0.09232743084430695, 1.682620882987976), (0.0, 0.0, 0.0), (-0.06499999761581421, 0.06520706415176392, 0.06520706415176392), 'KEY_BSPLINE', 'KEY_BSPLINE', 'KEY_BSPLINE', 3, 2, 3)
    add_vgroups('R')
    add_vg_weights(2,0.5)
    add_vg_weights(5,0.5)
    add_vg_weights(8,1.0)
    add_vg_weights(11,1.0)
    add_vg_weights(14,0.5)
    add_vg_weights(17,0.5)
    add_vgroups('L')
    add_vg_weights(0,0.5)
    add_vg_weights(3,0.5)
    add_vg_weights(6,1.0)
    add_vg_weights(9,1.0)
    add_vg_weights(12,0.5)
    add_vg_weights(15,0.5)
    add_vgroups('UP')
    add_vg_weights(12,0.5)
    add_vg_weights(13,1.0)
    add_vg_weights(14,0.5)
    add_vg_weights(15,0.5)
    add_vg_weights(16,1.0)
    add_vg_weights(17,0.5)
    add_vgroups('LOW')
    add_vg_weights(0,0.5)
    add_vg_weights(1,1.0)
    add_vg_weights(2,0.5)
    add_vg_weights(3,0.5)
    add_vg_weights(4,1.0)
    add_vg_weights(5,0.5)
    add_vgroups('lattice_eye_L')
    add_vg_weights(7,1.0)
    add_vg_weights(10,1.0)
    add_mod('lattice_eye_L', 'HOOK', 1.0, 'lattice_eye_L', 'lattice_eye_L')
    add_mod('toon_eye_out_L', 'HOOK', 1.0, 'toon_eye_out_L', 'L')
    add_mod('toon_eye_in_L', 'HOOK', 1.0, 'toon_eye_in_L', 'R')
    add_mod('toon_eye_up_L', 'HOOK', 1.0, 'toon_eye_up_L', 'UP')
    add_mod('toon_eye_low_L', 'HOOK', 1.0, 'toon_eye_low_L', 'LOW')

