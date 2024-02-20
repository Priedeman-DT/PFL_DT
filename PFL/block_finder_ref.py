
import rhinoscriptsyntax as rs
import Rhino.Geometry as rc
import scriptcontext as sc


def block_finder():
    """
    input => Gets all block instances name from Rhino active Doc
    returns => Block instances Names list
    
    """
    bl_inst=[]
    bl_inst_names=[]
    
    
    # Getting block names 
    bInstNames=rs.GetObjects("Select block instances", 4096, True, True)
    
    # prof_bnames= rs.BlockNames()        
    
    # Filtering Named block
    
    for i in bInstNames: 
        inst=(rs.BlockInstanceName(i))
        if inst:                        
            bl_inst.append(i)
            bl_inst_names.append(inst)     
    return bl_inst_names,bl_inst



# if __name__ == '__main__':
    
    
   
   