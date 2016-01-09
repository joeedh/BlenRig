import bpy

############################ Add Armature Groups ############################ 

def add_armature_groups(self, context):
   
    bgroups = bpy.context.object.pose.bone_groups

    bgroups.new('GEN')
    bgroups['GEN'].color_set = 'THEME04'
    bgroups['GEN'].colors.active[0] = 0.3686274588108063
    bgroups['GEN'].colors.active[1] = 0.7568628191947937
    bgroups['GEN'].colors.active[2] = 0.9372549653053284
    bgroups['GEN'].colors.select[0] = 0.21176472306251526
    bgroups['GEN'].colors.select[1] = 0.40392160415649414
    bgroups['GEN'].colors.select[2] = 0.874509871006012
    bgroups['GEN'].colors.normal[0] = 0.03921568766236305
    bgroups['GEN'].colors.normal[1] = 0.21176472306251526
    bgroups['GEN'].colors.normal[2] = 0.5803921818733215
    bgroups.new('FK_L')
    bgroups['FK_L'].color_set = 'THEME01'
    bgroups['FK_L'].colors.active[0] = 0.9686275124549866
    bgroups['FK_L'].colors.active[1] = 0.03921568766236305
    bgroups['FK_L'].colors.active[2] = 0.03921568766236305
    bgroups['FK_L'].colors.select[0] = 0.7411764860153198
    bgroups['FK_L'].colors.select[1] = 0.06666667014360428
    bgroups['FK_L'].colors.select[2] = 0.06666667014360428
    bgroups['FK_L'].colors.normal[0] = 0.6039215922355652
    bgroups['FK_L'].colors.normal[1] = 0.0
    bgroups['FK_L'].colors.normal[2] = 0.0
    bgroups.new('FK_R')
    bgroups['FK_R'].color_set = 'CUSTOM'
    bgroups['FK_R'].colors.active[0] = 0.8705883026123047
    bgroups['FK_R'].colors.active[1] = 0.03921568766236305
    bgroups['FK_R'].colors.active[2] = 0.03921568766236305
    bgroups['FK_R'].colors.select[0] = 0.658823549747467
    bgroups['FK_R'].colors.select[1] = 0.06666667014360428
    bgroups['FK_R'].colors.select[2] = 0.06666667014360428
    bgroups['FK_R'].colors.normal[0] = 0.501960813999176
    bgroups['FK_R'].colors.normal[1] = 0.0
    bgroups['FK_R'].colors.normal[2] = 0.0
    bgroups.new('IK_L')
    bgroups['IK_L'].color_set = 'CUSTOM'
    bgroups['IK_L'].colors.active[0] = 0.5137255191802979
    bgroups['IK_L'].colors.active[1] = 0.9372549653053284
    bgroups['IK_L'].colors.active[2] = 0.11372549831867218
    bgroups['IK_L'].colors.select[0] = 0.3490196168422699
    bgroups['IK_L'].colors.select[1] = 0.7176470756530762
    bgroups['IK_L'].colors.select[2] = 0.04313725605607033
    bgroups['IK_L'].colors.normal[0] = 0.06666667014360428
    bgroups['IK_L'].colors.normal[1] = 0.4392157196998596
    bgroups['IK_L'].colors.normal[2] = 0.0
    bgroups.new('IK_R')
    bgroups['IK_R'].color_set = 'CUSTOM'
    bgroups['IK_R'].colors.active[0] = 0.458823561668396
    bgroups['IK_R'].colors.active[1] = 0.8352941870689392
    bgroups['IK_R'].colors.active[2] = 0.10196079313755035
    bgroups['IK_R'].colors.select[0] = 0.3019607961177826
    bgroups['IK_R'].colors.select[1] = 0.6196078658103943
    bgroups['IK_R'].colors.select[2] = 0.03529411926865578
    bgroups['IK_R'].colors.normal[0] = 0.09803922474384308
    bgroups['IK_R'].colors.normal[1] = 0.4705882668495178
    bgroups['IK_R'].colors.normal[2] = 0.027450982481241226
    bgroups.new('TOON_L')
    bgroups['TOON_L'].color_set = 'THEME09'
    bgroups['TOON_L'].colors.active[0] = 0.9529412388801575
    bgroups['TOON_L'].colors.active[1] = 1.0
    bgroups['TOON_L'].colors.active[2] = 0.0
    bgroups['TOON_L'].colors.select[0] = 0.9333333969116211
    bgroups['TOON_L'].colors.select[1] = 0.760784387588501
    bgroups['TOON_L'].colors.select[2] = 0.21176472306251526
    bgroups['TOON_L'].colors.normal[0] = 0.9568628072738647
    bgroups['TOON_L'].colors.normal[1] = 0.7882353663444519
    bgroups['TOON_L'].colors.normal[2] = 0.0470588281750679
    bgroups.new('TOON_R')
    bgroups['TOON_R'].color_set = 'CUSTOM'
    bgroups['TOON_R'].colors.active[0] = 0.8588235974311829
    bgroups['TOON_R'].colors.active[1] = 0.9019608497619629
    bgroups['TOON_R'].colors.active[2] = 0.0
    bgroups['TOON_R'].colors.select[0] = 0.8313726186752319
    bgroups['TOON_R'].colors.select[1] = 0.6784313917160034
    bgroups['TOON_R'].colors.select[2] = 0.1882353127002716
    bgroups['TOON_R'].colors.normal[0] = 0.8588235974311829
    bgroups['TOON_R'].colors.normal[1] = 0.7058823704719543
    bgroups['TOON_R'].colors.normal[2] = 0.04313725605607033
    bgroups.new('SCALE_L')
    bgroups['SCALE_L'].color_set = 'THEME06'
    bgroups['SCALE_L'].colors.active[0] = 0.529411792755127
    bgroups['SCALE_L'].colors.active[1] = 0.3921568989753723
    bgroups['SCALE_L'].colors.active[2] = 0.8352941870689392
    bgroups['SCALE_L'].colors.select[0] = 0.3294117748737335
    bgroups['SCALE_L'].colors.select[1] = 0.22745099663734436
    bgroups['SCALE_L'].colors.select[2] = 0.6392157077789307
    bgroups['SCALE_L'].colors.normal[0] = 0.26274511218070984
    bgroups['SCALE_L'].colors.normal[1] = 0.0470588281750679
    bgroups['SCALE_L'].colors.normal[2] = 0.4705882668495178
    bgroups.new('SCALE_R')
    bgroups['SCALE_R'].color_set = 'CUSTOM'
    bgroups['SCALE_R'].colors.active[0] = 0.46666669845581055
    bgroups['SCALE_R'].colors.active[1] = 0.3450980484485626
    bgroups['SCALE_R'].colors.active[2] = 0.7333333492279053
    bgroups['SCALE_R'].colors.select[0] = 0.27843138575553894
    bgroups['SCALE_R'].colors.select[1] = 0.19215688109397888
    bgroups['SCALE_R'].colors.select[2] = 0.5372549295425415
    bgroups['SCALE_R'].colors.normal[0] = 0.20784315466880798
    bgroups['SCALE_R'].colors.normal[1] = 0.03529411926865578
    bgroups['SCALE_R'].colors.normal[2] = 0.37254902720451355
    bgroups.new('FACIAL_L')
    bgroups['FACIAL_L'].color_set = 'CUSTOM'
    bgroups['FACIAL_L'].colors.active[0] = 0.9686275124549866
    bgroups['FACIAL_L'].colors.active[1] = 0.03921568766236305
    bgroups['FACIAL_L'].colors.active[2] = 0.03921568766236305
    bgroups['FACIAL_L'].colors.select[0] = 0.7411764860153198
    bgroups['FACIAL_L'].colors.select[1] = 0.06666667014360428
    bgroups['FACIAL_L'].colors.select[2] = 0.06666667014360428
    bgroups['FACIAL_L'].colors.normal[0] = 0.6470588445663452
    bgroups['FACIAL_L'].colors.normal[1] = 0.0
    bgroups['FACIAL_L'].colors.normal[2] = 0.0
    bgroups.new('FACIAL_R')
    bgroups['FACIAL_R'].color_set = 'CUSTOM'
    bgroups['FACIAL_R'].colors.active[0] = 0.8705883026123047
    bgroups['FACIAL_R'].colors.active[1] = 0.03529411926865578
    bgroups['FACIAL_R'].colors.active[2] = 0.03529411926865578
    bgroups['FACIAL_R'].colors.select[0] = 0.6392157077789307
    bgroups['FACIAL_R'].colors.select[1] = 0.05882353335618973
    bgroups['FACIAL_R'].colors.select[2] = 0.05882353335618973
    bgroups['FACIAL_R'].colors.normal[0] = 0.545098066329956
    bgroups['FACIAL_R'].colors.normal[1] = 0.0
    bgroups['FACIAL_R'].colors.normal[2] = 0.0
    bgroups.new('FACIAL_MAIN_L')
    bgroups['FACIAL_MAIN_L'].color_set = 'THEME10'
    bgroups['FACIAL_MAIN_L'].colors.active[0] = 1.0
    bgroups['FACIAL_MAIN_L'].colors.active[1] = 1.0
    bgroups['FACIAL_MAIN_L'].colors.active[2] = 1.0
    bgroups['FACIAL_MAIN_L'].colors.select[0] = 0.2823529541492462
    bgroups['FACIAL_MAIN_L'].colors.select[1] = 0.2980392277240753
    bgroups['FACIAL_MAIN_L'].colors.select[2] = 0.33725491166114807
    bgroups['FACIAL_MAIN_L'].colors.normal[0] = 0.11764706671237946
    bgroups['FACIAL_MAIN_L'].colors.normal[1] = 0.125490203499794
    bgroups['FACIAL_MAIN_L'].colors.normal[2] = 0.1411764770746231
    bgroups.new('FACIAL_MAIN_R')
    bgroups['FACIAL_MAIN_R'].color_set = 'CUSTOM'
    bgroups['FACIAL_MAIN_R'].colors.active[0] = 0.9019608497619629
    bgroups['FACIAL_MAIN_R'].colors.active[1] = 0.9019608497619629
    bgroups['FACIAL_MAIN_R'].colors.active[2] = 0.9019608497619629
    bgroups['FACIAL_MAIN_R'].colors.select[0] = 0.20000001788139343
    bgroups['FACIAL_MAIN_R'].colors.select[1] = 0.20784315466880798
    bgroups['FACIAL_MAIN_R'].colors.select[2] = 0.2352941334247589
    bgroups['FACIAL_MAIN_R'].colors.normal[0] = 0.03529411926865578
    bgroups['FACIAL_MAIN_R'].colors.normal[1] = 0.03529411926865578
    bgroups['FACIAL_MAIN_R'].colors.normal[2] = 0.03921568766236305
    bgroups.new('CLOTH')
    bgroups['CLOTH'].color_set = 'THEME06'
    bgroups['CLOTH'].colors.active[0] = 0.529411792755127
    bgroups['CLOTH'].colors.active[1] = 0.3921568989753723
    bgroups['CLOTH'].colors.active[2] = 0.8352941870689392
    bgroups['CLOTH'].colors.select[0] = 0.3294117748737335
    bgroups['CLOTH'].colors.select[1] = 0.22745099663734436
    bgroups['CLOTH'].colors.select[2] = 0.6392157077789307
    bgroups['CLOTH'].colors.normal[0] = 0.26274511218070984
    bgroups['CLOTH'].colors.normal[1] = 0.0470588281750679
    bgroups['CLOTH'].colors.normal[2] = 0.4705882668495178
    bgroups.new('STR')
    bgroups['STR'].color_set = 'THEME01'
    bgroups['STR'].colors.active[0] = 0.9686275124549866
    bgroups['STR'].colors.active[1] = 0.03921568766236305
    bgroups['STR'].colors.active[2] = 0.03921568766236305
    bgroups['STR'].colors.select[0] = 0.7411764860153198
    bgroups['STR'].colors.select[1] = 0.06666667014360428
    bgroups['STR'].colors.select[2] = 0.06666667014360428
    bgroups['STR'].colors.normal[0] = 0.6039215922355652
    bgroups['STR'].colors.normal[1] = 0.0
    bgroups['STR'].colors.normal[2] = 0.0
    bgroups.new('STR_EYEBROWS')
    bgroups['STR_EYEBROWS'].color_set = 'THEME02'
    bgroups['STR_EYEBROWS'].colors.active[0] = 0.9803922176361084
    bgroups['STR_EYEBROWS'].colors.active[1] = 0.6000000238418579
    bgroups['STR_EYEBROWS'].colors.active[2] = 0.0
    bgroups['STR_EYEBROWS'].colors.select[0] = 0.9647059440612793
    bgroups['STR_EYEBROWS'].colors.select[1] = 0.4117647409439087
    bgroups['STR_EYEBROWS'].colors.select[2] = 0.07450980693101883
    bgroups['STR_EYEBROWS'].colors.normal[0] = 0.9686275124549866
    bgroups['STR_EYEBROWS'].colors.normal[1] = 0.250980406999588
    bgroups['STR_EYEBROWS'].colors.normal[2] = 0.0941176563501358
    bgroups.new('STR_EYES')
    bgroups['STR_EYES'].color_set = 'THEME04'
    bgroups['STR_EYES'].colors.active[0] = 0.3686274588108063
    bgroups['STR_EYES'].colors.active[1] = 0.7568628191947937
    bgroups['STR_EYES'].colors.active[2] = 0.9372549653053284
    bgroups['STR_EYES'].colors.select[0] = 0.21176472306251526
    bgroups['STR_EYES'].colors.select[1] = 0.40392160415649414
    bgroups['STR_EYES'].colors.select[2] = 0.874509871006012
    bgroups['STR_EYES'].colors.normal[0] = 0.03921568766236305
    bgroups['STR_EYES'].colors.normal[1] = 0.21176472306251526
    bgroups['STR_EYES'].colors.normal[2] = 0.5803921818733215
    bgroups.new('STR_FACE')
    bgroups['STR_FACE'].color_set = 'THEME01'
    bgroups['STR_FACE'].colors.active[0] = 0.9686275124549866
    bgroups['STR_FACE'].colors.active[1] = 0.03921568766236305
    bgroups['STR_FACE'].colors.active[2] = 0.03921568766236305
    bgroups['STR_FACE'].colors.select[0] = 0.7411764860153198
    bgroups['STR_FACE'].colors.select[1] = 0.06666667014360428
    bgroups['STR_FACE'].colors.select[2] = 0.06666667014360428
    bgroups['STR_FACE'].colors.normal[0] = 0.6039215922355652
    bgroups['STR_FACE'].colors.normal[1] = 0.0
    bgroups['STR_FACE'].colors.normal[2] = 0.0
    bgroups.new('STR_FACE_MECH')
    bgroups['STR_FACE_MECH'].color_set = 'THEME06'
    bgroups['STR_FACE_MECH'].colors.active[0] = 0.529411792755127
    bgroups['STR_FACE_MECH'].colors.active[1] = 0.3921568989753723
    bgroups['STR_FACE_MECH'].colors.active[2] = 0.8352941870689392
    bgroups['STR_FACE_MECH'].colors.select[0] = 0.3294117748737335
    bgroups['STR_FACE_MECH'].colors.select[1] = 0.22745099663734436
    bgroups['STR_FACE_MECH'].colors.select[2] = 0.6392157077789307
    bgroups['STR_FACE_MECH'].colors.normal[0] = 0.26274511218070984
    bgroups['STR_FACE_MECH'].colors.normal[1] = 0.0470588281750679
    bgroups['STR_FACE_MECH'].colors.normal[2] = 0.4705882668495178
    bgroups.new('STR_INNER_MOUTH')
    bgroups['STR_INNER_MOUTH'].color_set = 'THEME09'
    bgroups['STR_INNER_MOUTH'].colors.active[0] = 0.9529412388801575
    bgroups['STR_INNER_MOUTH'].colors.active[1] = 1.0
    bgroups['STR_INNER_MOUTH'].colors.active[2] = 0.0
    bgroups['STR_INNER_MOUTH'].colors.select[0] = 0.9333333969116211
    bgroups['STR_INNER_MOUTH'].colors.select[1] = 0.760784387588501
    bgroups['STR_INNER_MOUTH'].colors.select[2] = 0.21176472306251526
    bgroups['STR_INNER_MOUTH'].colors.normal[0] = 0.9568628072738647
    bgroups['STR_INNER_MOUTH'].colors.normal[1] = 0.7882353663444519
    bgroups['STR_INNER_MOUTH'].colors.normal[2] = 0.0470588281750679
    bgroups.new('STR_HANDS')
    bgroups['STR_HANDS'].color_set = 'THEME09'
    bgroups['STR_HANDS'].colors.active[0] = 0.9529412388801575
    bgroups['STR_HANDS'].colors.active[1] = 1.0
    bgroups['STR_HANDS'].colors.active[2] = 0.0
    bgroups['STR_HANDS'].colors.select[0] = 0.9333333969116211
    bgroups['STR_HANDS'].colors.select[1] = 0.760784387588501
    bgroups['STR_HANDS'].colors.select[2] = 0.21176472306251526
    bgroups['STR_HANDS'].colors.normal[0] = 0.9568628072738647
    bgroups['STR_HANDS'].colors.normal[1] = 0.7882353663444519
    bgroups['STR_HANDS'].colors.normal[2] = 0.0470588281750679




