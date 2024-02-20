import rhinoscriptsyntax as rs
import Rhino.Geometry as rc


#block_ob=rs.ExplodeBlockInstance(rs.BlockInstances("Sch_V_F_00"))


def blockExploder(bobj,objType):
    """
        input: Block instance ID nesting other block instances.
        object type str: object type to filter from the exploded blocks ps for polysurface and crv for curves
        output: Objects from all exploded nested blocks.
    """
    if objType=='ps':
        objType=16
    if objType=='crv':
        objType=4

    Block_Obj=[]
    

    if rs.ObjectType(bobj) == 4096:
        obj=rs.ExplodeBlockInstance(bobj,True)
        for k,l in enumerate(obj):
            if objType=='all':
                Block_Obj.append(l)
            if rs.ObjectType(l)==objType:
                brep=rs.coercebrep(l)
                Block_Obj.append(l)
    

    return Block_Obj


if __name__ == '__main__':
    pass