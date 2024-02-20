import rhinoscriptsyntax as rs
import Rhino.Geometry as rc


#block_ob=rs.ExplodeBlockInstance(rs.BlockInstances("Sch_V_F_00"))

# Block_Names=[]
# Block_Obj=[]
def blockExploder(b_obj):  
    """
        input: list of objects inside of first block level
        output: objects from all exploded nested blocks
        
    """
    for j in (b_obj):
        # Block_Obj.append([])
        if rs.ObjectType(j) == 4096: 
            Ins_n=rs.BlockInstanceName(j) 
            # Block_Names.append(Ins_n)
            obj=rs.ExplodeBlockInstance(j)
            # Block_Obj[i].append(obj)
            for l in (obj):
                if  rs.ObjectType(l) == 4096:
                    blockExploder([l])
                else:
                    rs.ObjectName(l,Ins_n)
        # else:
        #     rs.ObjectName(j,rs.ObjectLayer(j))          
            
    
    # return Block_Names,Block_Obj   



if __name__ == '__main__':
    pass