import bpy

############################ Add Bone ID Properties ############################ 

def add_pbones_id_properties(self, context):
    
    bpy.ops.object.mode_set(mode='POSE') 
    pbones = bpy.context.active_object.pose.bones

    for b in pbones:
        if b.name == 'master':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 1
        if b.name == 'master_pivot_point':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 1
        if b.name == 'floor_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}}
            b["ROT_MODE"] = 2
        if b.name == 'floor_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}}
            b["ROT_MODE"] = 2
        if b.name == 'master_body':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 1
        if b.name == 'master_body_pivot_point':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 1
        if b.name == 'properties':
            b["_RNA_UI"] ={'glasses_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_leg_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_low': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'deformation_extras': {'max': 1, 'min': 0, 'description': 'Turn Lattices and extra deformers on or off for viewpoer performance', 'soft_max': 1, 'soft_min': 0}, 'muscle_system': {'max': 1, 'min': 0, 'description': 'Turn muscle system on or off', 'soft_max': 1, 'soft_min': 0}, 'toon_arm_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_up': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_torso': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'hat_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'model_res': {'max': 5, 'min': 0, 'description': 'Character Subsurf level', 'soft_max': 5, 'soft_min': 0}, 'muscle_res': {'max': 5, 'min': 0, 'description': 'Subsurf level of muscle objects', 'soft_max': 5, 'soft_min': 0}, 'hand_accessory_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_leg_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'hand_accessory_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'toon_head': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_arm_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'ik_torso': {}, 'look_switch': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["model_res"] = 0
            b["deformation_extras"] = 0
            b["muscle_res"] = 0
            b["muscle_system"] = 0
        if b.name == 'properties_head':
            b["_RNA_UI"] ={'bones_fk_hinge': {'description': 'list used in auto-hide function'}, 'toon_leg_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_low': {'max': 1.0, 'min': 0.0, 'description': 'Automatic movement for when mouth corner moves', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_ik_hinge': {'description': 'list used in auto-hide function'}, 'toon_teeth_up': {'max': 1.0, 'min': 0.0, 'description': 'Automatic movement for when mouth corner moves', 'soft_max': 1.0, 'soft_min': 0.0}, 'glasses_free': {'max': 1.0, 'min': 0.0, 'description': 'Make glasses follow head or be free', 'soft_max': 1.0, 'soft_min': 0.0}, 'rj_hands': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'toon_torso': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_ik': {'description': 'list used in auto-hide function'}, 'rj_feet': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'toon_leg_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'muscle_system': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'hand_accessory_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_head': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_arm_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'ik_torso': {}, 'bones_fk': {'description': 'list used in auto-hide function'}, 'flex_head_scale': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping head scale', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'flex_neck_width': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping neck width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'rj_arms': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'reproportion': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'toon_arm_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_neck_length': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping neck length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'rj_legs': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'hat_free': {'max': 1.0, 'min': 0.0, 'description': 'Make hat follow head or be free', 'soft_max': 1.0, 'soft_min': 0.0}, 'deformation_extras': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'muscle_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'model_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'hand_accessory_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'look_switch': {'max': 3.0, 'min': 0.0, 'description': '', 'soft_max': 3.0, 'soft_min': 0.0}}
            b["ik_head"] = 1.0
            b["hinge_head"] = 0.0
            b["toon_head"] = 0.0
            b["look_switch"] = 3.0
            b["hinge_neck"] = 0.0
            b["bones_fk"] = ['neck_1_fk', 'neck_2_fk', 'neck_3_fk', 'neck_fk_ctrl']
            b["bones_fk_hinge"] = ['head_fk']
            b["bones_ik"] = ['neck_1_ik_ctrl', 'neck_2_ik_ctrl', 'neck_3_ik_ctrl', 'neck_ik_ctrl', 'neck_pivot_point', 'head_ik_ctrl']
            b["bones_ik_hinge"] = ['']
            b["hat_free"] = 0.0
            b["glasses_free"] = 0.0
            b["toon_teeth_low"] = 0.20000000298023224
            b["toon_teeth_up"] = 0.20000000298023224
            b["flex_head_scale"] = 1.0
            b["flex_neck_length"] = 1.0
            b["flex_neck_width"] = 1.0
        if b.name == 'properties_torso':
            b["_RNA_UI"] ={'toon_leg_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_low': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_up': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'rj_arms': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'rj_hands': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'flex_pelvis_width': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping pelvis length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'toon_torso': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_inv': {'description': 'list used in auto-hide function'}, 'bones_ik': {'description': 'list used in auto-hide function'}, 'rj_feet': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'toon_leg_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'muscle_system': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'hand_accessory_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_head': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_arm_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'ik_torso': {}, 'bones_fk': {'description': 'list used in auto-hide function'}, 'flex_ribs_width': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping ribs length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'flex_torso_height': {'max': 100.0, 'min': -100.0, 'description': 'Dynamic Shaping torso height', 'soft_max': 100.0, 'soft_min': -100.0}, 'glasses_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_torso_scale': {'max': 100.0, 'min': -100.0, 'description': 'Dynamic Shaping torso scale', 'soft_max': 100.0, 'soft_min': -100.0}, 'flex_chest_width': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping chest length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'reproportion': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'toon_arm_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_waist_width': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping waist width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'rj_legs': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'hat_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'deformation_extras': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'muscle_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'model_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'hand_accessory_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'look_switch': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["inv_torso"] = 0.0
            b["ik_torso"] = 0.0
            b["toon_torso"] = 0.0
            b["bones_inv"] = ['pelvis_inv', 'torso_inv_ctrl', 'spine_1_inv', 'spine_2_inv', 'spine_3_inv', 'spine_3_inv_ctrl']
            b["bones_ik"] = ['torso_ik_ctrl', 'torso_pivot_point', 'spine_1_ik_ctrl', 'spine_2_ik_ctrl', 'spine_3_ik_ctrl', 'spine_4_ik_ctrl']
            b["bones_fk"] = ['spine_1_fk', 'torso_fk_ctrl', 'spine_2_fk', 'spine_3_fk']
            b["flex_chest_width"] = 1.0
            b["flex_pelvis_width"] = 1.0
            b["flex_ribs_width"] = 1.0
            b["flex_torso_scale"] = 1.0
            b["flex_waist_width"] = 1.0
            b["flex_torso_height"] = 0.0
        if b.name == 'properties_arm_L':
            b["_RNA_UI"] ={'bones_ik_palm_L': {'description': 'list used in auto-hide function'}, 'bones_fk_palm_L': {'description': ''}, 'toggle_fingers_L': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'bones_fingers_def_2_L': {'description': 'list used in auto-hide function'}, 'toon_leg_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'realistic_joints_wrist_L': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'rj_hands': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'toon_torso': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_arm_width_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping arm width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'flex_arm_length_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping arm length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'toon_head': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'ik_torso': {}, 'bones_fingers_str_L': {'description': 'list used in auto-hide function'}, 'glasses_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'curved_arm_L': {'max': 1.0, 'min': 0.0, 'description': 'Curvature rate for arm bending', 'soft_max': 1.0, 'soft_min': 0.0}, 'curved_arm_tweak_L': {'max': 10.0, 'min': -10.0, 'description': 'Curvature tweak value for arm and forearm', 'soft_max': 10.0, 'soft_min': -10.0}, 'bones_fingers_ctrl_1_L': {'description': 'list used in auto-hide function'}, 'rj_legs': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'realistic_joints_elbow_L': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'model_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'muscle_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'flex_hand_scale_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping hand scale', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'flex_arm_uniform_scale_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping arm scale', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'bones_fingers_ctrl_2_L': {'description': 'list used in auto-hide function'}, 'toon_leg_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_low': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_up': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'realistic_joints_hand_L': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'bones_fk_hand_L': {'description': 'list used in auto-hide function'}, 'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'rj_feet': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'flex_forearm_length_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping forearm length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'muscle_system': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'hand_accessory_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_arm_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_ik_L': {'description': 'list used in auto-hide function'}, 'bones_fk_L': {'description': 'list used in auto-hide function'}, 'rj_arms': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'bones_ik_hand_L': {'description': 'list used in auto-hide function'}, 'reproportion': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'toon_arm_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_fingers_def_1_L': {'description': 'list used in auto-hide function'}, 'hat_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'deformation_extras': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'flex_forearm_width_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping forearm width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'hand_accessory_L': {'max': 1.0, 'min': 0.0, 'description': 'Make accessory follow left hand or be free', 'soft_max': 1.0, 'soft_min': 0.0}, 'look_switch': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["ik_arm_L"] = 0.0
            b["hinge_arm_L"] = 0.0
            b["hinge_hand_L"] = 1.0
            b["hinge_fing_thumb_L"] = 0.0
            b["hinge_fing_ind_L"] = 0.0
            b["hinge_fing_mid_L"] = 0.0
            b["hinge_fing_ring_L"] = 0.0
            b["hinge_fing_lit_L"] = 0.0
            b["toon_arm_L"] = 0.0
            b["ik_fing_ind_L"] = 0.0
            b["hinge_fing_all_L"] = 0.0
            b["ik_fing_all_L"] = 0.0
            b["ik_fing_thumb_L"] = 0.0
            b["ik_fing_lit_L"] = 0.0
            b["ik_fing_ring_L"] = 0.0
            b["ik_fing_mid_L"] = 0.0
            b["bones_fk_palm_L"] = ['palm_bend_fk_ctrl_L']
            b["toggle_fingers_L"] = 1
            b["bones_fingers_ctrl_1_L"] = ['hand_close_L', 'fing_thumb_ctrl_L', 'fing_spread_L', 'fing_lit_ctrl_L', 'fing_ring_ctrl_L', 'fing_ind_ctrl_L', 'fing_mid_ctrl_L', 'fing_ind_ik_L', 'fing_thumb_ik_L', 'fing_mid_ik_L', 'fing_ring_ik_L', 'fing_lit_ik_L']
            b["bones_fingers_ctrl_2_L"] = ['fing_thumb_1_L', 'fing_thumb_2_L', 'fing_thumb_3_L', 'fing_lit_2_L', 'fing_lit_3_L', 'fing_lit_4_L', 'fing_ring_2_L', 'fing_ring_3_L', 'fing_ring_4_L', 'fing_ind_2_L', 'fing_ind_3_L', 'fing_ind_4_L', 'fing_mid_2_L', 'fing_mid_3_L', 'fing_mid_4_L']
            b["bones_fingers_def_1_L"] = ['fing_thumb_fix_low_1_L', 'fing_thumb_fix_up_1_L', 'fing_thumb_fix_low_2_L', 'fing_thumb_fix_up_2_L', 'fing_lit_fix_low_1_L', 'fing_lit_fix_up_1_L', 'fing_lit_fix_low_2_L', 'fing_lit_fix_up_2_L', 'fing_lit_fix_low_3_L', 'fing_lit_fix_up_3_L', 'fing_ring_fix_low_1_L', 'fing_ring_fix_up_1_L', 'fing_ring_fix_low_2_L', 'fing_ring_fix_up_2_L', 'fing_ring_fix_low_3_L', 'fing_ring_fix_up_3_L', 'fing_ind_fix_low_1_L', 'fing_ind_fix_up_1_L', 'fing_ind_fix_low_2_L', 'fing_ind_fix_up_2_L', 'fing_ind_fix_low_3_L', 'fing_ind_fix_up_3_L', 'fing_mid_fix_low_1_L', 'fing_mid_fix_up_1_L', 'fing_mid_fix_low_2_L', 'fing_mid_fix_up_2_L', 'fing_mid_fix_low_3_L', 'fing_mid_fix_up_3_L']
            b["bones_fingers_def_2_L"] = ['fing_thumb_1_def_L', 'fing_thumb_2_def_L', 'fing_thumb_3_def_L', 'fing_lit_1_def_L', 'fing_lit_2_def_L', 'fing_lit_3_def_L', 'fing_lit_4_def_L', 'fing_ring_1_def_L', 'fing_ring_2_def_L', 'fing_ring_3_def_L', 'fing_ring_4_def_L', 'fing_ind_1_def_L', 'fing_ind_2_def_L', 'fing_ind_3_def_L', 'fing_ind_4_def_L', 'fing_mid_1_def_L', 'fing_mid_2_def_L', 'fing_mid_3_def_L', 'fing_mid_4_def_L']
            b["bones_fingers_str_L"] = ['fing_lit_str_2_L', 'fing_lit_str_3_L', 'fing_lit_str_4_L', 'fing_lit_str_5_L', 'fing_ring_str_2_L', 'fing_ring_str_3_L', 'fing_ring_str_4_L', 'fing_ring_str_5_L', 'fing_ind_str_2_L', 'fing_ind_str_3_L', 'fing_ind_str_4_L', 'fing_ind_str_5_L', 'fing_mid_str_2_L', 'fing_mid_str_3_L', 'fing_mid_str_4_L', 'fing_mid_str_5_L', 'fing_thumb_str_2_L', 'fing_thumb_str_3_L', 'fing_thumb_str_4_L', 'fing_thumb_str_1_L', 'fing_lit_str_1_L', 'fing_ring_str_1_L', 'fing_ind_str_1_L', 'fing_mid_str_1_L']
            b["bones_fk_L"] = ['arm_fk_L', 'forearm_fk_L']
            b["bones_fk_hand_L"] = ['hand_fk_L']
            b["bones_ik_L"] = ['elbow_pole_L', 'elbow_line_L']
            b["bones_ik_hand_L"] = ['hand_ik_ctrl_L']
            b["bones_ik_palm_L"] = ['palm_bend_ik_ctrl_L', 'hand_ik_pivot_point_L']
            b["curved_arm_L"] = 0.0
            b["curved_arm_tweak_L"] = -0.05999999865889549
            b["flex_arm_length_L"] = 1.0
            b["flex_arm_uniform_scale_L"] = 1.0
            b["flex_arm_width_L"] = 1.0
            b["flex_forearm_length_L"] = 1.0
            b["flex_forearm_width_L"] = 1.0
            b["flex_hand_scale_L"] = 1.0
            b["hand_accessory_L"] = 1.0
            b["realistic_joints_elbow_L"] = 0.019999999552965164
            b["realistic_joints_hand_L"] = 0.004000000189989805
            b["realistic_joints_wrist_L"] = 0.00800000037997961
        if b.name == 'properties_arm_R':
            b["_RNA_UI"] ={'bones_fingers_ctrl_1_R': {'description': 'list used in auto-hide function'}, 'bones_ik_R': {'description': 'list used in auto-hide function'}, 'model_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'curved_arm_tweak_R': {'max': 10.0, 'min': -10.0, 'description': 'Curvature tweak value for arm and forearm', 'soft_max': 10.0, 'soft_min': -10.0}, 'rj_hands': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'toon_torso': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_leg_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_head': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_arm_uniform_scale_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping arm scale', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'ik_torso': {}, 'glasses_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toggle_fingers_R': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'realistic_joints_wrist_R': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'realistic_joints_hand_R': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'rj_legs': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'bones_fk_R': {'description': 'list used in auto-hide function'}, 'bones_fingers_def_2_R': {'description': 'list used in auto-hide function'}, 'muscle_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'curved_arm_R': {'max': 1.0, 'min': 0.0, 'description': 'Curvature rate for arm bending', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_fingers_ctrl_2_R': {'description': 'list used in auto-hide function'}, 'toon_leg_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_low': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_up': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_hand_scale_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping hand scale', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'bones_fingers_str_R': {'description': 'list used in auto-hide function'}, 'flex_forearm_length_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping forearm length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'rj_feet': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'bones_fingers_def_1_R': {'description': 'list used in auto-hide function'}, 'muscle_system': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'hand_accessory_R': {'max': 1.0, 'min': 0.0, 'description': 'Make accessory follow left hand or be free', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_arm_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_arm_width_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping arm width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'rj_arms': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'bones_ik_palm_R': {'description': 'list used in auto-hide function'}, 'reproportion': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'toon_arm_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'realistic_joints_elbow_R': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'bones_fk_palm_R': {'description': 'list used in auto-hide function'}, 'hat_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'deformation_extras': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'bones_fk_hand_R': {'description': 'list used in auto-hide function'}, 'flex_forearm_width_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping forearm width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'hand_accessory_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_ik_hand_R': {'description': 'list used in auto-hide function'}, 'look_switch': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_arm_length_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping arm length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}}
            b["hinge_arm_R"] = 0.0
            b["hinge_hand_R"] = 1.0
            b["hinge_fing_thumb_R"] = 0.0
            b["hinge_fing_ind_R"] = 0.0
            b["hinge_fing_mid_R"] = 0.0
            b["hinge_fing_ring_R"] = 0.0
            b["hinge_fing_lit_R"] = 0.0
            b["ik_arm_R"] = 0.0
            b["toon_arm_R"] = 0.0
            b["ik_fing_all_R"] = 0.0
            b["hinge_fing_all_R"] = 0.0
            b["ik_fing_ind_R"] = 0.0
            b["ik_fing_mid_R"] = 0.0
            b["ik_fing_ring_R"] = 0.0
            b["ik_fing_lit_R"] = 0.0
            b["ik_fing_thumb_R"] = 0.0
            b["toggle_fingers_R"] = 1
            b["bones_fingers_ctrl_1_R"] = ['hand_close_R', 'fing_thumb_ctrl_R', 'fing_spread_R', 'fing_lit_ctrl_R', 'fing_ring_ctrl_R', 'fing_ind_ctrl_R', 'fing_mid_ctrl_R', 'fing_ind_ik_R', 'fing_thumb_ik_R', 'fing_mid_ik_R', 'fing_ring_ik_R', 'fing_lit_ik_R']
            b["bones_fingers_ctrl_2_R"] = ['fing_thumb_1_R', 'fing_thumb_2_R', 'fing_thumb_3_R', 'fing_lit_2_R', 'fing_lit_3_R', 'fing_lit_4_R', 'fing_ring_2_R', 'fing_ring_3_R', 'fing_ring_4_R', 'fing_ind_2_R', 'fing_ind_3_R', 'fing_ind_4_R', 'fing_mid_2_R', 'fing_mid_3_R', 'fing_mid_4_R']
            b["bones_fingers_def_1_R"] = ['fing_thumb_fix_up_1_R', 'fing_thumb_fix_low_1_R', 'fing_thumb_fix_low_2_R', 'fing_thumb_fix_up_2_R', 'fing_lit_fix_up_1_R', 'fing_lit_fix_low_1_R', 'fing_lit_fix_low_2_R', 'fing_lit_fix_up_2_R', 'fing_lit_fix_low_3_R', 'fing_lit_fix_up_3_R', 'fing_ring_fix_up_1_R', 'fing_ring_fix_low_1_R', 'fing_ring_fix_low_2_R', 'fing_ring_fix_up_2_R', 'fing_ring_fix_low_3_R', 'fing_ring_fix_up_3_R', 'fing_ind_fix_low_1_R', 'fing_ind_fix_up_1_R', 'fing_ind_fix_low_2_R', 'fing_ind_fix_up_2_R', 'fing_ind_fix_low_3_R', 'fing_ind_fix_up_3_R', 'fing_mid_fix_up_1_R', 'fing_mid_fix_low_1_R', 'fing_mid_fix_low_2_R', 'fing_mid_fix_up_2_R', 'fing_mid_fix_low_3_R', 'fing_mid_fix_up_3_R']
            b["bones_fingers_def_2_R"] = ['fing_thumb_1_def_R', 'fing_thumb_2_def_R', 'fing_thumb_3_def_R', 'fing_lit_1_def_R', 'fing_lit_2_def_R', 'fing_lit_3_def_R', 'fing_lit_4_def_R', 'fing_ring_1_def_R', 'fing_ring_2_def_R', 'fing_ring_3_def_R', 'fing_ring_4_def_R', 'fing_ind_1_def_R', 'fing_ind_2_def_R', 'fing_ind_3_def_R', 'fing_ind_4_def_R', 'fing_mid_1_def_R', 'fing_mid_2_def_R', 'fing_mid_3_def_R', 'fing_mid_4_def_R']
            b["bones_fingers_str_R"] = ['fing_lit_str_2_R', 'fing_lit_str_3_R', 'fing_lit_str_4_R', 'fing_lit_str_5_R', 'fing_ring_str_2_R', 'fing_ring_str_3_R', 'fing_ring_str_4_R', 'fing_ring_str_5_R', 'fing_ind_str_2_R', 'fing_ind_str_3_R', 'fing_ind_str_4_R', 'fing_ind_str_5_R', 'fing_mid_str_2_R', 'fing_mid_str_3_R', 'fing_mid_str_4_R', 'fing_mid_str_5_R', 'fing_thumb_str_2_R', 'fing_thumb_str_3_R', 'fing_thumb_str_4_R', 'fing_thumb_str_1_R', 'fing_lit_str_1_R', 'fing_ring_str_1_R', 'fing_ind_str_1_R', 'fing_mid_str_1_R']
            b["bones_fk_R"] = ['arm_fk_R', 'forearm_fk_R']
            b["bones_fk_hand_R"] = ['hand_fk_R']
            b["bones_fk_palm_R"] = ['palm_bend_fk_ctrl_R']
            b["bones_ik_R"] = ['elbow_pole_R', 'elbow_line_R']
            b["bones_ik_hand_R"] = ['hand_ik_ctrl_R']
            b["bones_ik_palm_R"] = ['palm_bend_ik_ctrl_R', 'hand_ik_pivot_point_R']
            b["curved_arm_R"] = 0.0
            b["curved_arm_tweak_R"] = -0.05999999865889549
            b["flex_arm_length_R"] = 1.0
            b["flex_arm_uniform_scale_R"] = 1.0
            b["flex_arm_width_R"] = 1.0
            b["flex_forearm_length_R"] = 1.0
            b["flex_forearm_width_R"] = 1.0
            b["flex_hand_scale_R"] = 1.0
            b["hand_accessory_R"] = 0.0
            b["realistic_joints_elbow_R"] = 0.019999999552965164
            b["realistic_joints_hand_R"] = 0.004000000189989805
            b["realistic_joints_wrist_R"] = 0.00800000037997961
        if b.name == 'properties_leg_R':
            b["_RNA_UI"] ={'bones_fk_foot_R': {'description': 'list used in auto-hide function'}, 'hinge_toes_all_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'realistic_joints_knee_R': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'bones_ik_R': {'description': 'list used in auto-hide function'}, 'flex_foot_loc_R': {'max': 100.0, 'min': -100.0, 'description': 'Dynamic Shaping widen feet separation to match pelvis width', 'soft_max': 100.0, 'soft_min': -100.0}, 'flex_foot_scale_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping foot scale', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'rj_hands': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'toon_torso': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'curved_leg_R': {'max': 1.0, 'min': 0.0, 'description': 'Curvature rate for leg bending', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_shin_length_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping shin length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'bones_no_toes_ctrl_R': {'description': 'list used in auto-hide function'}, 'toon_head': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_shin_width_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping shin width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'ik_torso': {}, 'glasses_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'realistic_joints_ankle_R': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'bones_toes_ctrl_1_R': {'description': 'list used in auto-hide function'}, 'toggle_toes_R': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'rj_legs': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'bones_fk_R': {'description': 'list used in auto-hide function'}, 'model_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'muscle_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'bones_no_toes_def_R': {'description': 'list used in auto-hide function'}, 'ik_toes_all_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_leg_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_low': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'realistic_joints_foot_R': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'toon_teeth_up': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_thigh_width_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping thigh width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'bones_toes_def_2_R': {'description': 'list used in auto-hide function'}, 'rj_feet': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'muscle_system': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'hand_accessory_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_toes_str_R': {'description': 'list used in auto-hide function'}, 'toon_arm_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_toes_def_1_R': {'description': ''}, 'rj_arms': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'bones_ik_foot_R': {'description': 'list used in auto-hide function'}, 'flex_leg_uniform_scale_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping leg scale', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'reproportion': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'toon_arm_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_thigh_length_R': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping thigh length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'hat_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'deformation_extras': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'look_switch': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_toes_ctrl_2_R': {'description': 'list used in auto-hide function'}, 'hand_accessory_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'curved_leg_tweak_R': {'max': 10.0, 'min': -10.0, 'description': 'Curvature tweak value for thigh and shin', 'soft_max': 10.0, 'soft_min': -10.0}}
            b["ik_leg_R"] = 0.0
            b["hinge_leg_R"] = 0.0
            b["toon_leg_R"] = 0.0
            b["ik_toes_all_R"] = 0.0
            b["hinge_toes_all_R"] = 0.0
            b["bones_toes_def_1_R"] = ['toe_big_fix_up_1_R', 'toe_big_fix_low_1_R', 'toe_big_fix_up_2_R', 'toe_big_fix_low_2_R', 'toe_lit_fix_up_1_R', 'toe_lit_fix_low_1_R', 'toe_lit_fix_up_2_R', 'toe_lit_fix_low_2_R', 'toe_fourth_fix_up_1_R', 'toe_fourth_fix_low_1_R', 'toe_fourth_fix_up_2_R', 'toe_fourth_fix_low_2_R', 'toe_fourth_fix_up_3_R', 'toe_fourth_fix_low_3_R', 'toe_mid_fix_up_1_R', 'toe_mid_fix_low_1_R', 'toe_mid_fix_up_2_R', 'toe_mid_fix_low_2_R', 'toe_mid_fix_up_3_R', 'toe_mid_fix_low_3_R', 'toe_ind_fix_up_1_R', 'toe_ind_fix_low_1_R', 'toe_ind_fix_up_2_R', 'toe_ind_fix_low_2_R', 'toe_ind_fix_up_3_R', 'toe_ind_fix_low_3_R']
            b["toggle_toes_R"] = 0
            b["bones_toes_str_R"] = ['toe_big_str_2_R', 'toe_mid_str_2_R', 'toe_fourth_str_2_R', 'toe_lit_str_2_R', 'toe_ind_str_2_R', 'toe_big_str_3_R', 'toe_mid_str_3_R', 'toe_mid_str_4_R', 'toe_fourth_str_3_R', 'toe_fourth_str_4_R', 'toe_lit_str_3_R', 'toe_ind_str_3_R', 'toe_ind_str_4_R', 'toe_lit_str_4_R', 'toe_big_str_4_R', 'toe_fourth_str_5_R', 'toe_mid_str_5_R', 'toe_ind_str_5_R', 'toe_lit_str_1_R', 'toe_fourth_str_1_R', 'toe_mid_str_1_R', 'toe_big_str_1_R', 'toe_ind_str_1_R']
            b["bones_toes_def_2_R"] = ['toe_big_1_def_R', 'toe_big_2_def_R', 'toe_big_3_def_R', 'toe_lit_1_def_R', 'toe_lit_2_def_R', 'toe_lit_3_def_R', 'toe_fourth_1_def_R', 'toe_fourth_2_def_R', 'toe_fourth_3_def_R', 'toe_fourth_4_def_R', 'toe_mid_1_def_R', 'toe_mid_2_def_R', 'toe_mid_3_def_R', 'toe_mid_4_def_R', 'toe_ind_1_def_R', 'toe_ind_2_def_R', 'toe_ind_3_def_R', 'toe_ind_4_def_R']
            b["bones_toes_ctrl_2_R"] = ['toe_lit_2_R', 'toe_lit_3_R', 'toe_big_2_R', 'toe_big_3_R', 'toe_fourth_2_R', 'toe_fourth_3_R', 'toe_fourth_4_R', 'toe_mid_2_R', 'toe_mid_3_R', 'toe_mid_4_R', 'toe_ind_2_R', 'toe_ind_3_R', 'toe_ind_4_R']
            b["bones_toes_ctrl_1_R"] = ['toe_lit_ik_R', 'toe_fourth_ik_R', 'toe_mid_ik_R', 'toe_ind_ik_R', 'toe_big_ik_R', 'toes_spread_R', 'toe_lit_ctrl_R', 'toe_big_ctrl_R', 'toe_fourth_ctrl_R', 'toe_mid_ctrl_R', 'toe_ind_ctrl_R']
            b["bones_no_toes_def_R"] = ['toe_2_def_R', 'toe_1_def_R', 'toe_fix_up_1_R', 'toe_fix_low_1_R']
            b["bones_no_toes_ctrl_R"] = ['toes_ik_ctrl_mid_R', 'toe_1_fk_R', 'toe_2_fk_R']
            b["bones_ik_foot_R"] = ['toes_ik_ctrl_mid_R', 'toes_ik_ctrl_R', 'toe_roll_2_R', 'toe_roll_1_R', 'toe_lit_ik_R', 'toe_fourth_ik_R', 'toe_mid_ik_R', 'toe_ind_ik_R', 'toe_big_ik_R']
            b["bones_ik_R"] = ['knee_pole_R', 'knee_line_R', 'foot_roll_ctrl_R', 'sole_pivot_point_R', 'foot_ik_ctrl_R', 'sole_ctrl_R']
            b["bones_fk_foot_R"] = ['']
            b["bones_fk_R"] = ['thigh_fk_R', 'shin_fk_R', 'tarsal_fk_R', 'foot_fk_R']
            b["curved_leg_R"] = 0.0
            b["curved_leg_tweak_R"] = 0.11999999731779099
            b["flex_foot_scale_R"] = 1.0
            b["flex_leg_uniform_scale_R"] = 1.0
            b["flex_shin_length_R"] = 1.0
            b["flex_shin_width_R"] = 1.0
            b["flex_thigh_length_R"] = 1.0
            b["flex_thigh_width_R"] = 1.0
            b["flex_foot_loc_R"] = 0.0
            b["realistic_joints_ankle_R"] = 0.024000000208616257
            b["realistic_joints_foot_R"] = 0.004000000189989805
            b["realistic_joints_knee_R"] = 0.035999998450279236
        if b.name == 'properties_leg_L':
            b["_RNA_UI"] ={'bones_toes_str_L': {'description': 'list used in auto-hide function'}, 'rj_hands': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'toon_torso': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_leg_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'realistic_joints_knee_L': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'flex_foot_scale_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping foot scale', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'toon_head': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'ik_torso': {}, 'flex_thigh_width_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping thigh width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'bones_toes_def_1_L': {'description': 'list used in auto-hide function'}, 'glasses_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_foot_loc_L': {'max': 100.0, 'min': -100.0, 'description': 'Dynamic Shaping widen feet separation to match pelvis width', 'soft_max': 100.0, 'soft_min': -100.0}, 'realistic_joints_foot_L': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'curved_leg_L': {'max': 1.0, 'min': 0.0, 'description': 'Curvature rate for leg bending', 'soft_max': 1.0, 'soft_min': 0.0}, 'realistic_joints_ankle_L': {'max': 90.0, 'min': 0.0, 'description': 'joint displacement simulation', 'soft_max': 90.0, 'soft_min': 0.0}, 'rj_legs': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'bones_toes_ctrl_2_L': {'description': 'list used in auto-hide function'}, 'bones_ik_foot_L': {'description': 'list used in auto-hide function'}, 'muscle_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'flex_thigh_length_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping thigh length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'hand_accessory_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'hinge_toes_all_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'curved_leg_tweak_L': {'max': 10.0, 'min': -10.0, 'description': 'Curvature tweak value for thigh and shin', 'soft_max': 10.0, 'soft_min': -10.0}, 'toon_leg_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_low': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toon_teeth_up': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'rj_arms': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'look_switch': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'flex_leg_uniform_scale_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping leg scale', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'ik_toes_all_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'rj_feet': {'max': 50.0, 'min': 0.0, 'description': '', 'soft_max': 50.0, 'soft_min': 0.0}, 'muscle_system': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'flex_shin_length_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping shin length', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'toon_arm_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_ik_L': {'description': 'list used in auto-hide function'}, 'flex_shin_width_L': {'max': 100.0, 'min': 0.009999999776482582, 'description': 'Dynamic Shaping shin width', 'soft_max': 100.0, 'soft_min': 0.009999999776482582}, 'bones_toes_def_2_L': {'description': 'list used in auto-hide function'}, 'bones_fk_L': {'description': 'list used in auto-hide function'}, 'reproportion': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'bones_fk_foot_L': {'description': 'list used in auto-hide function'}, 'toon_arm_R': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'bones_toes_ctrl_1_L': {'description': 'list used in auto-hide function'}, 'hat_free': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'deformation_extras': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'bones_no_toes_ctrl_L': {'description': 'list used in auto-hide function'}, 'model_res': {'max': 5, 'min': 0, 'description': '', 'soft_max': 5, 'soft_min': 0}, 'hand_accessory_L': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'toggle_toes_L': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'bones_no_toes_def_L': {'description': 'list used in auto-hide function'}}
            b["ik_leg_L"] = 0.0
            b["hinge_leg_L"] = 0.0
            b["toon_leg_L"] = 0.0
            b["ik_toes_all_L"] = 0.0
            b["hinge_toes_all_L"] = 0.0
            b["toggle_toes_L"] = 0
            b["bones_toes_str_L"] = ['toe_big_str_2_L', 'toe_mid_str_2_L', 'toe_fourth_str_2_L', 'toe_lit_str_2_L', 'toe_ind_str_2_L', 'toe_big_str_3_L', 'toe_mid_str_3_L', 'toe_mid_str_4_L', 'toe_fourth_str_3_L', 'toe_fourth_str_4_L', 'toe_lit_str_3_L', 'toe_ind_str_3_L', 'toe_ind_str_4_L', 'toe_lit_str_4_L', 'toe_fourth_str_5_L', 'toe_mid_str_5_L', 'toe_big_str_4_L', 'toe_ind_str_5_L', 'toe_lit_str_1_L', 'toe_fourth_str_1_L', 'toe_mid_str_1_L', 'toe_big_str_1_L', 'toe_ind_str_1_L']
            b["bones_toes_def_2_L"] = ['toe_lit_1_def_L', 'toe_lit_2_def_L', 'toe_lit_3_def_L', 'toe_big_1_def_L', 'toe_big_2_def_L', 'toe_big_3_def_L', 'toe_fourth_1_def_L', 'toe_fourth_2_def_L', 'toe_fourth_3_def_L', 'toe_fourth_4_def_L', 'toe_mid_1_def_L', 'toe_mid_2_def_L', 'toe_mid_3_def_L', 'toe_mid_4_def_L', 'toe_ind_1_def_L', 'toe_ind_2_def_L', 'toe_ind_3_def_L', 'toe_ind_4_def_L']
            b["bones_toes_def_1_L"] = ['toe_lit_fix_up_1_L', 'toe_lit_fix_low_1_L', 'toe_lit_fix_up_2_L', 'toe_lit_fix_low_2_L', 'toe_big_fix_up_1_L', 'toe_big_fix_low_1_L', 'toe_big_fix_up_2_L', 'toe_big_fix_low_2_L', 'toe_fourth_fix_up_1_L', 'toe_fourth_fix_low_1_L', 'toe_fourth_fix_up_2_L', 'toe_fourth_fix_low_2_L', 'toe_fourth_fix_up_3_L', 'toe_fourth_fix_low_3_L', 'toe_mid_fix_up_1_L', 'toe_mid_fix_low_1_L', 'toe_mid_fix_up_2_L', 'toe_mid_fix_low_2_L', 'toe_mid_fix_up_3_L', 'toe_mid_fix_low_3_L', 'toe_ind_fix_up_1_L', 'toe_ind_fix_low_1_L', 'toe_ind_fix_up_2_L', 'toe_ind_fix_low_2_L', 'toe_ind_fix_up_3_L', 'toe_ind_fix_low_3_L']
            b["bones_toes_ctrl_2_L"] = ['toe_lit_2_L', 'toe_lit_3_L', 'toe_big_2_L', 'toe_big_3_L', 'toe_fourth_2_L', 'toe_fourth_3_L', 'toe_fourth_4_L', 'toe_mid_2_L', 'toe_mid_3_L', 'toe_mid_4_L', 'toe_ind_2_L', 'toe_ind_3_L', 'toe_ind_4_L']
            b["bones_toes_ctrl_1_L"] = ['toe_lit_ik_L', 'toe_fourth_ik_L', 'toe_mid_ik_L', 'toe_ind_ik_L', 'toe_big_ik_L', 'toes_spread_L', 'toe_lit_ctrl_L', 'toe_big_ctrl_L', 'toe_fourth_ctrl_L', 'toe_mid_ctrl_L', 'toe_ind_ctrl_L']
            b["bones_no_toes_def_L"] = ['toe_2_def_L', 'toe_1_def_L', 'toe_fix_up_1_L', 'toe_fix_low_1_L']
            b["bones_no_toes_ctrl_L"] = ['toes_ik_ctrl_mid_L', 'toe_1_fk_L', 'toe_2_fk_L']
            b["bones_ik_foot_L"] = ['toes_ik_ctrl_mid_L', 'toes_ik_ctrl_L', 'toe_roll_2_L', 'toe_roll_1_L', 'toe_lit_ik_L', 'toe_fourth_ik_L', 'toe_mid_ik_L', 'toe_ind_ik_L', 'toe_big_ik_L']
            b["bones_ik_L"] = ['knee_pole_L', 'knee_line_L', 'foot_roll_ctrl_L', 'sole_pivot_point_L', 'foot_ik_ctrl_L', 'sole_ctrl_L']
            b["bones_fk_foot_L"] = ['']
            b["bones_fk_L"] = ['thigh_fk_L', 'shin_fk_L', 'tarsal_fk_L', 'foot_fk_L']
            b["curved_leg_L"] = 0.0
            b["curved_leg_tweak_L"] = 0.11999999731779099
            b["flex_foot_scale_L"] = 1.0
            b["flex_leg_uniform_scale_L"] = 1.0
            b["flex_shin_length_L"] = 1.0
            b["flex_shin_width_L"] = 1.0
            b["flex_thigh_length_L"] = 1.0
            b["flex_thigh_width_L"] = 1.0
            b["flex_foot_loc_L"] = 0.0
            b["realistic_joints_ankle_L"] = 0.024000000208616257
            b["realistic_joints_foot_L"] = 0.004000000189989805
            b["realistic_joints_knee_L"] = 0.035999998450279236
        if b.name == 'master_torso':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 1
        if b.name == 'master_torso_pivot_point':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 1
        if b.name == 'torso_fk_ctrl':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'torso_ik_ctrl':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'spine_3_inv_ctrl':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}}
            b["ROT_MODE"] = 5
        if b.name == 'spine_3_inv':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["ROT_MODE"] = 2
        if b.name == 'torso_inv_ctrl':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}}
            b["ROT_MODE"] = 2
        if b.name == 'spine_2_inv':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': 'Percentage in which Torso_inv_ctrl influences rotation', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["ROT_MODE"] = 2
            b["fk_follow_main"] = 0.30000001192092896
        if b.name == 'spine_1_inv':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': 'Percentage in which Torso_inv_ctrl influences rotation', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["ROT_MODE"] = 2
            b["fk_follow_main"] = 0.5
        if b.name == 'pelvis_inv':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': 'Percentage in which Torso_inv_ctrl influences rotation', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["ROT_MODE"] = 5
            b["fk_follow_main"] = 0.800000011920929
        if b.name == 'pelvis_ctrl':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 5
        if b.name == 'spine_1_fk':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': 'Percentage in which Torso_fk_ctrl influences rotation', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["ROT_MODE"] = 2
            b["fk_follow_main"] = 0.10000000149011612
        if b.name == 'spine_1_def_bbone':
            b["_RNA_UI"] ={'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["fk_follow_main"] = 0.30000001192092896
        if b.name == 'spine_2_fk':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': 'Percentage in which Torso_fk_ctrl influences rotation', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["ROT_MODE"] = 2
            b["fk_follow_main"] = 0.30000001192092896
        if b.name == 'spine_3_fk':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': 'Percentage in which Torso_fk_ctrl influences rotation', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["ROT_MODE"] = 2
            b["fk_follow_main"] = 0.5
        if b.name == 'neck_fk_ctrl':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 3
        if b.name == 'head_ik_ctrl':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'neck_1_fk':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["fk_follow_main"] = 0.5
            b["ROT_MODE"] = 3
        if b.name == 'neck_2_fk':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["fk_follow_main"] = 0.5
            b["ROT_MODE"] = 3
        if b.name == 'neck_3_fk':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["fk_follow_main"] = 0.800000011920929
            b["ROT_MODE"] = 3
        if b.name == 'head_fk':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'fk_follow_main': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["ROT_MODE"] = 5
        if b.name == 'nose_frown_ctrl_L':
            b["_RNA_UI"] ={'UP_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Upwards range for nose frown action', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["UP_LIMIT_L"] = 0.019999999552965164
        if b.name == 'nose_frown_ctrl_R':
            b["_RNA_UI"] ={'UP_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Upwards range for nose frown action', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["UP_LIMIT_R"] = 0.019999999552965164
        if b.name == 'mouth_ctrl':
            b["_RNA_UI"] ={'SMILE_LIMIT': {'max': 100.0, 'min': 0.0, 'description': 'Smile rate for mouth_ctrl roatation', 'soft_max': 100.0, 'soft_min': 0.0}, 'IN_LIMIT': {'max': 10.0, 'min': 0.0, 'description': 'Inwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'AUTO_CHEEK': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'JAW_ROTATION': {'max': 180.0, 'min': 0.0, 'description': 'Jaw rotation rate for mouth_ctrl vertical movement', 'soft_max': 180.0, 'soft_min': 0.0}, 'OUT_LIMIT': {'max': 10.0, 'min': 0.0, 'description': 'Outwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'U_ACTION_TOGGLE': {'max': 1.0, 'min': 0.0, 'description': 'Turn action on or off', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["OUT_LIMIT"] = 0.10000000149011612
            b["IN_LIMIT"] = 0.014999999664723873
            b["SMILE_LIMIT"] = 0.05
            b["JAW_ROTATION"] = 60.0
            b["U_ACTION_TOGGLE"] = 1.0
        if b.name == 'maxi':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}, 'ACTION_UP_DOWN_TOGGLE': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'JAW_UP_LIMIT': {'max': 180.0, 'min': 0.0, 'description': 'Jaw upwards rotation limit', 'soft_max': 180.0, 'soft_min': 0.0}, 'JAW_DOWN_LIMIT': {'max': 180.0, 'min': 0.0, 'description': 'Jaw downwards rotation limit', 'soft_max': 180.0, 'soft_min': 0.0}}
            b["ROT_MODE"] = 6
            b["JAW_DOWN_LIMIT"] = 30.0
            b["JAW_UP_LIMIT"] = 20.0
            b["ACTION_UP_DOWN_TOGGLE"] = 1
        if b.name == 'mouth_frown_ctrl_L':
            b["_RNA_UI"] ={'DOWN_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Downwards range for mouth frown action', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["DOWN_LIMIT_L"] = 0.019999999552965164
        if b.name == 'mouth_frown_ctrl_R':
            b["_RNA_UI"] ={'DOWN_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Downwards range for mouth frown action', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["DOWN_LIMIT_R"] = 0.019999999552965164
        if b.name == 'tongue_2_ik':
            b["_RNA_UI"] ={'follow_chain': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'repel_chain': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["follow_chain"] = 0.25
        if b.name == 'tongue_1_ik':
            b["_RNA_UI"] ={'follow_chain': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}, 'repel_chain': {'max': 1.0, 'min': 0.0, 'description': '', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["follow_chain"] = 0.20000000298023224
        if b.name == 'mouth_corner_L':
            b["_RNA_UI"] ={'ACTION_DOWN_TOGGLE_L': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'ACTION_BACK_TOGGLE_L': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'FORW_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Forwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'ACTION_IN_TOGGLE_L': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'CORNER_IN_ACTION_TOGGLE': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'UP_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Upwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'AUTO_BACK_L': {'max': 1000.0, 'min': -1000.0, 'description': 'Automatic backwards movement when corner moves out', 'soft_max': 1000.0, 'soft_min': -1000.0}, 'ACTION_UP_TOGGLE_L': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'IN_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Inwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'DOWN_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Downwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'ACTION_OUT_TOGGLE_L': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'ACTION_FORW_TOGGLE_L': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'BACK_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Backwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'OUT_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Outwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["IN_LIMIT_L"] = 0.014999999664723873
            b["OUT_LIMIT_L"] = 0.10000000149011612
            b["UP_LIMIT_L"] = 0.05999999865889549
            b["DOWN_LIMIT_L"] = 0.03999999910593033
            b["FORW_LIMIT_L"] = 0.04500000178813934
            b["BACK_LIMIT_L"] = 0.04500000178813934
            b["AUTO_BACK_L"] = -140.0
            b["ACTION_UP_TOGGLE_L"] = 1
            b["ACTION_DOWN_TOGGLE_L"] = 1
            b["ACTION_FORW_TOGGLE_L"] = 1
            b["ACTION_BACK_TOGGLE_L"] = 1
            b["ACTION_IN_TOGGLE_L"] = 1
            b["ACTION_OUT_TOGGLE_L"] = 1
        if b.name == 'cheek_ctrl_L':
            b["_RNA_UI"] ={'ACTION_CHEEK_TOGGLE_L': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'AUTO_SMILE_L': {'max': 1.0, 'min': 0.0, 'description': 'Automaic movement range for when mouth corner moves up', 'soft_max': 1.0, 'soft_min': 0.0}, 'CHEEK_DOWN_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Downwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'CHEEK_UP_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Upwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["CHEEK_UP_LIMIT_L"] = 0.029999999329447746
            b["CHEEK_DOWN_LIMIT_L"] = 0.014999999664723873
            b["AUTO_SMILE_L"] = 0.5
            b["ACTION_CHEEK_TOGGLE_L"] = 1
        if b.name == 'lip_low_ctrl_1_mstr_L':
            b["_RNA_UI"] ={'CORNER_FOLLOW_Y_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_X_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_L"] = 30.0
            b["CORNER_FOLLOW_Y_L"] = 10.0
            b["CORNER_FOLLOW_Z_L"] = 10.0
        if b.name == 'lip_low_ctrl_2_mstr_L':
            b["_RNA_UI"] ={'CORNER_FOLLOW_Y_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_X_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_L"] = 50.0
            b["CORNER_FOLLOW_Y_L"] = 25.0
            b["CORNER_FOLLOW_Z_L"] = 30.0
        if b.name == 'lip_low_ctrl_3_mstr_L':
            b["_RNA_UI"] ={'CORNER_FOLLOW_Y_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_X_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_L"] = 80.0
            b["CORNER_FOLLOW_Y_L"] = 60.0
            b["CORNER_FOLLOW_Z_L"] = 70.0
        if b.name == 'lip_up_ctrl_1_mstr_L':
            b["_RNA_UI"] ={'CORNER_FOLLOW_Y_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_X_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_L"] = 30.0
            b["CORNER_FOLLOW_Y_L"] = 10.0
            b["CORNER_FOLLOW_Z_L"] = 10.0
        if b.name == 'lip_up_ctrl_2_mstr_L':
            b["_RNA_UI"] ={'CORNER_FOLLOW_Y_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_X_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_L"] = 50.0
            b["CORNER_FOLLOW_Y_L"] = 25.0
            b["CORNER_FOLLOW_Z_L"] = 30.0
        if b.name == 'lip_up_ctrl_3_mstr_L':
            b["_RNA_UI"] ={'CORNER_FOLLOW_Y_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_X_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_L"] = 80.0
            b["CORNER_FOLLOW_Y_L"] = 60.0
            b["CORNER_FOLLOW_Z_L"] = 70.0
        if b.name == 'mouth_corner_R':
            b["_RNA_UI"] ={'AUTO_BACK_R': {'max': 1000.0, 'min': -1000.0, 'description': 'Automatic backwards movement when corner moves out', 'soft_max': 1000.0, 'soft_min': -1000.0}, 'UP_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Upwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'OUT_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Outwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'ACTION_UP_TOGGLE_R': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'FORW_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Forwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'ACTION_OUT_TOGGLE_R': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'IN_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Inwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'ACTION_FORW_TOGGLE_R': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'ACTION_IN_TOGGLE_R': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'ACTION_BACK_TOGGLE_R': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}, 'DOWN_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Downwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'CORNER_IN_ACTION_TOGGLE': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'BACK_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Backwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'ACTION_DOWN_TOGGLE_R': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}}
            b["IN_LIMIT_R"] = 0.014999999664723873
            b["OUT_LIMIT_R"] = 0.10000000149011612
            b["UP_LIMIT_R"] = 0.05999999865889549
            b["DOWN_LIMIT_R"] = 0.03999999910593033
            b["FORW_LIMIT_R"] = 0.04500000178813934
            b["BACK_LIMIT_R"] = 0.04500000178813934
            b["AUTO_BACK_R"] = -140.0
            b["ACTION_UP_TOGGLE_R"] = 1
            b["ACTION_DOWN_TOGGLE_R"] = 1
            b["ACTION_FORW_TOGGLE_R"] = 1
            b["ACTION_BACK_TOGGLE_R"] = 1
            b["ACTION_IN_TOGGLE_R"] = 1
            b["ACTION_OUT_TOGGLE_R"] = 1
        if b.name == 'cheek_ctrl_R':
            b["_RNA_UI"] ={'CHEEK_DOWN_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Downwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'AUTO_SMILE_R': {'max': 1.0, 'min': 0.0, 'description': 'Automaic movement range for when mouth corner moves up', 'soft_max': 1.0, 'soft_min': 0.0}, 'CHEEK_UP_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Upwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'ACTION_CHEEK_TOGGLE_R': {'max': 1, 'min': 0, 'description': 'Turn action on or off', 'soft_max': 1, 'soft_min': 0}}
            b["CHEEK_UP_LIMIT_R"] = 0.029999999329447746
            b["CHEEK_DOWN_LIMIT_R"] = 0.014999999664723873
            b["AUTO_SMILE_R"] = 0.5
            b["ACTION_CHEEK_TOGGLE_R"] = 1
        if b.name == 'lip_low_ctrl_2_mstr_R':
            b["_RNA_UI"] ={'CORNER_FOLLOW_X_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Y_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_R"] = 50.0
            b["CORNER_FOLLOW_Y_R"] = 25.0
            b["CORNER_FOLLOW_Z_R"] = 30.0
        if b.name == 'lip_low_ctrl_1_mstr_R':
            b["_RNA_UI"] ={'CORNER_FOLLOW_X_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Y_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_R"] = 30.0
            b["CORNER_FOLLOW_Y_R"] = 10.0
            b["CORNER_FOLLOW_Z_R"] = 10.0
        if b.name == 'lip_low_ctrl_3_mstr_R':
            b["_RNA_UI"] ={'CORNER_FOLLOW_Y_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_X_L': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_L"] = 80.0
            b["CORNER_FOLLOW_Y_L"] = 60.0
            b["CORNER_FOLLOW_Z_L"] = 70.0
        if b.name == 'lip_up_ctrl_2_mstr_R':
            b["_RNA_UI"] ={'CORNER_FOLLOW_X_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Y_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_R"] = 50.0
            b["CORNER_FOLLOW_Y_R"] = 25.0
            b["CORNER_FOLLOW_Z_R"] = 30.0
        if b.name == 'lip_up_ctrl_1_mstr_R':
            b["_RNA_UI"] ={'CORNER_FOLLOW_X_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Y_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_R"] = 30.0
            b["CORNER_FOLLOW_Y_R"] = 10.0
            b["CORNER_FOLLOW_Z_R"] = 10.0
        if b.name == 'lip_up_ctrl_3_mstr_R':
            b["_RNA_UI"] ={'CORNER_FOLLOW_X_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner X movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Y_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Y movement', 'soft_max': 100.0, 'soft_min': 0.0}, 'CORNER_FOLLOW_Z_R': {'max': 100.0, 'min': 0.0, 'description': 'Percentage in which controller follows mouth corner Z movement', 'soft_max': 100.0, 'soft_min': 0.0}}
            b["CORNER_FOLLOW_X_R"] = 80.0
            b["CORNER_FOLLOW_Y_R"] = 60.0
            b["CORNER_FOLLOW_Z_R"] = 70.0
        if b.name == 'hand_ik_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'hand_ik_pivot_point_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'palm_bend_ik_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'elbow_pole_R':
            b["_RNA_UI"] ={'FOLLOW_TORSO_R': {'max': 1.0, 'min': 0.0, 'description': 'Make pole follow torso or be free', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["FOLLOW_TORSO_R"] = 1.0
        if b.name == 'shoulder_R':
            b["_RNA_UI"] ={'SHLDR_AUTO_FORW_R': {'max': 100.0, 'min': -100.0, 'description': 'Shoulder automatic movement with arm in IK', 'soft_max': 100.0, 'soft_min': -100.0}, 'SHLDR_AUTO_BACK_R': {'max': 100.0, 'min': -100.0, 'description': 'Shoulder automatic movement with arm in IK', 'soft_max': 100.0, 'soft_min': -100.0}, 'SHLDR_AUTO_UP_R': {'max': 100.0, 'min': -100.0, 'description': 'Shoulder automatic movement with arm in IK', 'soft_max': 100.0, 'soft_min': -100.0}, 'SHLDR_AUTO_DOWN_R': {'max': 100.0, 'min': -100.0, 'description': 'Shoulder automatic movement with arm in IK', 'soft_max': 100.0, 'soft_min': -100.0}}
            b["SHLDR_AUTO_BACK_R"] = -10.0
            b["SHLDR_AUTO_DOWN_R"] = -4.0
            b["SHLDR_AUTO_FORW_R"] = 10.0
            b["SHLDR_AUTO_UP_R"] = 10.0
        if b.name == 'arm_fk_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 5
        if b.name == 'hand_ik_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'hand_ik_pivot_point_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'palm_bend_ik_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'elbow_pole_L':
            b["_RNA_UI"] ={'FOLLOW_TORSO_L': {'max': 1.0, 'min': 0.0, 'description': 'Make pole follow torso or be free', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["FOLLOW_TORSO_L"] = 1.0
        if b.name == 'shoulder_L':
            b["_RNA_UI"] ={'SHLDR_AUTO_BACK_L': {'max': 100.0, 'min': -100.0, 'description': 'Shoulder automatic movement with arm in IK', 'soft_max': 100.0, 'soft_min': -100.0}, 'SHLDR_AUTO_FORW_L': {'max': 100.0, 'min': -100.0, 'description': 'Shoulder automatic movement with arm in IK', 'soft_max': 100.0, 'soft_min': -100.0}, 'SHLDR_AUTO_UP_L': {'max': 100.0, 'min': -100.0, 'description': 'Shoulder automatic movement with arm in IK', 'soft_max': 100.0, 'soft_min': -100.0}, 'SHLDR_AUTO_DOWN_L': {'max': 100.0, 'min': -100.0, 'description': 'Shoulder automatic movement with arm in IK', 'soft_max': 100.0, 'soft_min': -100.0}}
            b["SHLDR_AUTO_BACK_L"] = -10.0
            b["SHLDR_AUTO_DOWN_L"] = -4.0
            b["SHLDR_AUTO_FORW_L"] = 10.0
            b["SHLDR_AUTO_UP_L"] = 10.0
        if b.name == 'arm_fk_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 5
        if b.name == 'master_body_str':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 1
        if b.name == 'sole_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 3
        if b.name == 'sole_pivot_point_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 5
        if b.name == 'foot_roll_ctrl_R':
            b["_RNA_UI"] ={'TOE_2_ROLL_START_R': {'max': 180.0, 'min': 0.0, 'description': 'Angle for toe 2 to start rolling', 'soft_max': 180.0, 'soft_min': 0.0}, 'TOE_1_ROLL_START_R': {'max': 180.0, 'min': 0.0, 'description': 'Angle for toe 1 to start rolling', 'soft_max': 180.0, 'soft_min': 0.0}, 'FOOT_ROLL_AMPLITUD_R': {'max': 180.0, 'min': 0.0, 'description': 'Foot roll max rotation range', 'soft_max': 180.0, 'soft_min': 0.0}}
            b["FOOT_ROLL_AMPLITUD_R"] = 90.0
            b["TOE_1_ROLL_START_R"] = 50.0
            b["TOE_2_ROLL_START_R"] = 70.0
        if b.name == 'knee_pole_R':
            b["_RNA_UI"] ={'FOLLOW_FOOT_R': {'max': 1.0, 'min': 0.0, 'description': 'Make pole follow foot or be free', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["FOLLOW_FOOT_R"] = 1.0
        if b.name == 'thigh_fk_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'sole_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 3
        if b.name == 'sole_pivot_point_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 5
        if b.name == 'foot_roll_ctrl_L':
            b["_RNA_UI"] ={'TOE_2_ROLL_START_L': {'max': 180.0, 'min': 0.0, 'description': 'Angle for toe 2 to start rolling', 'soft_max': 180.0, 'soft_min': 0.0}, 'TOE_1_ROLL_START_L': {'max': 180.0, 'min': 0.0, 'description': 'Angle for toe 1 to start rolling', 'soft_max': 180.0, 'soft_min': 0.0}, 'FOOT_ROLL_AMPLITUD_L': {'max': 180.0, 'min': 0.0, 'description': 'Foot roll max rotation range', 'soft_max': 180.0, 'soft_min': 0.0}}
            b["FOOT_ROLL_AMPLITUD_L"] = 90.0
            b["TOE_1_ROLL_START_L"] = 50.0
            b["TOE_2_ROLL_START_L"] = 70.0
        if b.name == 'knee_pole_L':
            b["_RNA_UI"] ={'FOLLOW_FOOT_L': {'max': 1.0, 'min': 0.0, 'description': 'Make pole follow foot or be free', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["FOLLOW_FOOT_L"] = 1.0
        if b.name == 'thigh_fk_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'hand_fk_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'palm_bend_fk_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'fing_thumb_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'fing_lit_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'fing_ring_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'fing_ind_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'fing_mid_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
            b["ik_arm_L"] = 0.0
            b["ik_arm_R"] = 0.0
            b["ik_fing_all_L"] = 0.0
            b["ik_fing_all_R"] = 0.0
            b["ik_fing_ind_L"] = 0.0
            b["ik_fing_ind_R"] = 0.0
            b["ik_fing_lit_L"] = 0.0
            b["ik_fing_lit_R"] = 0.0
            b["ik_fing_mid_L"] = 0.0
            b["ik_fing_mid_R"] = 0.0
            b["ik_fing_ring_L"] = 0.0
            b["ik_fing_ring_R"] = 0.0
            b["ik_fing_thumb_L"] = 0.0
            b["ik_fing_thumb_R"] = 0.0
            b["ik_foot_L"] = 0.0
            b["ik_foot_R"] = 0.0
            b["ik_head"] = 0.0
            b["ik_leg_L"] = 0.0
            b["ik_leg_R"] = 0.0
            b["ik_torso"] = 0.0
        if b.name == 'hand_accessory_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}}
            b["ROT_MODE"] = 1
        if b.name == 'hand_fk_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'palm_bend_fk_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'fing_thumb_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 2
        if b.name == 'fing_lit_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'fing_ring_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'fing_ind_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'fing_mid_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'hand_accessory_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}}
            b["ROT_MODE"] = 1
        if b.name == 'foot_fk_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_big_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_lit_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_fourth_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_mid_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_ind_ctrl_R':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'foot_fk_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_lit_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_big_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_fourth_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_mid_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'toe_ind_ctrl_L':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 6, 'min': -1, 'description': '', 'soft_max': 6, 'soft_min': -1}}
            b["ROT_MODE"] = 6
        if b.name == 'look_L':
            b["_RNA_UI"] ={'FLESHY_EYE_L': {'max': 1.0, 'min': 0.0, 'description': 'Influence of lattice deformation for eye movement', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["FLESHY_EYE_L"] = 0.02500000037252903
        if b.name == 'eyelid_up_ctrl_L':
            b["_RNA_UI"] ={'EYE_UP_FOLLOW_L': {'max': 10.0, 'min': 0.0, 'description': 'Automatic movement for when eye looks up', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYELID_ACTION_TOGGLE': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'EYELID_UP_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Upwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYE_DOWN_FOLLOW_L': {'max': 10.0, 'min': 0.0, 'description': 'Automatic movement for when eye looks down', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYELID_DOWN_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Downwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["EYELID_UP_LIMIT_L"] = 0.007000000216066837
            b["EYELID_DOWN_LIMIT_L"] = 0.02500000037252903
            b["EYE_UP_FOLLOW_L"] = 0.02
            b["EYE_DOWN_FOLLOW_L"] = 0.06
        if b.name == 'eyelid_low_ctrl_L':
            b["_RNA_UI"] ={'EYE_UP_FOLLOW_L': {'max': 10.0, 'min': 0.0, 'description': 'Automatic movement for when eye looks up', 'soft_max': 10.0, 'soft_min': 0.0}, 'AUTO_CHEEK_L': {'max': 100, 'min': 0, 'description': 'Automaic movement range for when cheek moves up', 'soft_max': 100, 'soft_min': 0}, 'EYELID_ACTION_TOGGLE': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'EYELID_UP_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Upwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYE_DOWN_FOLLOW_L': {'max': 10.0, 'min': 0.0, 'description': 'Automatic movement for when eye looks down', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYELID_DOWN_LIMIT_L': {'max': 10.0, 'min': 0.0, 'description': 'Downwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["EYELID_UP_LIMIT_L"] = 0.02500000037252903
            b["EYELID_DOWN_LIMIT_L"] = 0.007000000216066837
            b["EYE_UP_FOLLOW_L"] = 0.02
            b["EYE_DOWN_FOLLOW_L"] = 0.02
            b["AUTO_CHEEK_L"] = 25
        if b.name == 'look_R':
            b["_RNA_UI"] ={'FLESHY_EYE_R': {'max': 1.0, 'min': 0.0, 'description': 'Influence of lattice deformation for eye movement', 'soft_max': 1.0, 'soft_min': 0.0}}
            b["FLESHY_EYE_R"] = 0.02500000037252903
        if b.name == 'eyelid_low_ctrl_R':
            b["_RNA_UI"] ={'EYELID_DOWN_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Downwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'AUTO_CHEEK_R': {'max': 100, 'min': 0, 'description': 'Automaic movement range for when cheek moves up', 'soft_max': 100, 'soft_min': 0}, 'EYE_DOWN_FOLLOW_R': {'max': 10.0, 'min': 0.0, 'description': 'Automatic movement for when eye looks down', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYE_UP_FOLLOW_R': {'max': 10.0, 'min': 0.0, 'description': 'Automatic movement for when eye looks up', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYELID_ACTION_TOGGLE': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'EYELID_UP_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Upwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["EYELID_UP_LIMIT_R"] = 0.02500000037252903
            b["EYELID_DOWN_LIMIT_R"] = 0.007000000216066837
            b["EYE_UP_FOLLOW_R"] = 0.02
            b["EYE_DOWN_FOLLOW_R"] = 0.02
            b["AUTO_CHEEK_R"] = 25
        if b.name == 'eyelid_up_ctrl_R':
            b["_RNA_UI"] ={'EYELID_DOWN_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Downwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYE_UP_FOLLOW_R': {'max': 10.0, 'min': 0.0, 'description': 'Automatic movement for when eye looks up', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYELID_ACTION_TOGGLE': {'max': 1, 'min': 0, 'description': '', 'soft_max': 1, 'soft_min': 0}, 'EYE_DOWN_FOLLOW_R': {'max': 10.0, 'min': 0.0, 'description': 'Automatic movement for when eye looks down', 'soft_max': 10.0, 'soft_min': 0.0}, 'EYELID_UP_LIMIT_R': {'max': 10.0, 'min': 0.0, 'description': 'Upwards movement limit', 'soft_max': 10.0, 'soft_min': 0.0}}
            b["EYELID_UP_LIMIT_R"] = 0.007000000216066837
            b["EYELID_DOWN_LIMIT_R"] = 0.02500000037252903
            b["EYE_UP_FOLLOW_R"] = 0.02
            b["EYE_DOWN_FOLLOW_R"] = 0.06
        if b.name == 'accessory':
            b["_RNA_UI"] ={'ROT_MODE': {'max': 8, 'min': 0, 'description': '', 'soft_max': 8, 'soft_min': 0}}
            b["ROT_MODE"] = 1

