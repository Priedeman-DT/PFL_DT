import rhinoscriptsyntax as rs
import Rhino.Geometry as rc
import block_finder_ref
import blockExploderSingle
import block_exploder
rc.Brep.BrepClash()


def blockClashSrf():
    blocksInst=block_finder_ref.block_finder()[1]
    rs.AddLayer("clash")
    blocklistUnpcks=[]
    blocklistUnpcksMesh=[]
    for i,blIns in enumerate(blocksInst):
        blocklistUnpcks.append(blockExploderSingle.blockExploder(blIns,"ps")[0])
        blocklistUnpcksMesh.append(blockExploderSingle.blockExploder(blIns,"ps")[1])
        # blocklistUnpcks.append(rs.ExplodeBlockInstance(blIns,True))
        
    
    for brpElmentsList in blocklistUnpcks:
        intersected=[]
        for brpElment in brpElmentsList:
                for brpElments in brpElmentsList:
                    if brpElment!=brpElments:
                        intersecting=(rs.ObjectName(brpElments),rs.ObjectName(brpElment))
                        if intersecting not in intersected:
                            try:
                                intersection=rs.BooleanIntersection(brpElment,brpElments,False)
                                intType=rs.ObjectType(intersection)
                                intTest=rs.IsObject(intersection)
                                if intTest and intType==16 :
                                    # how to intersect all objects only once?
                                    interSected=(rs.ObjectName(brpElment),rs.ObjectName(brpElments))
                                    intersected.append(interSected)
                                    rs.ObjectLayer(intersection,"clash")
                                    print ("clash")
                                else:
                                    print ("no clash")    
                            except:
                                pass
                        else:
                            print ("clash already found")
            # if brpElment!=brpElments:
            #     intersecting=(rs.ObjectName(brpElments),rs.ObjectName(brpElment))
            #     if intersecting not in intersected:
            #         try:
            #             intersection=rs.BooleanIntersection(brpElment,brpElments,False)
            #             intType=rs.ObjectType(intersection)
            #             intTest=rs.IsObject(intersection)
            #             if intTest and intType==16 :
            #                 # how to intersect all objects only once?
            #                 interSected=(rs.ObjectName(brpElment),rs.ObjectName(brpElments))
            #                 intersected.append(interSected)
            #                 rs.ObjectLayer(intersection,"clash")
            #                 print ("clash")
            #             else:
            #                 print ("no clash")    
            #         except:
            #             pass
            #     else:
            #         print ("clash already found")    
    rs.HideObjects(blocklistUnpcks)           

def blockClashFst(blocksInst):
    for blIns in blocksInst:
        blocklistUnpcks=blockExploderSingle.blockExploder(blIns,'all')
        
        for brpElments in blocklistUnpcks:
            
                for brpElment in blocklistUnpcks:
                    if brpElment!=brpElments:
                        try:
                            intersection=rs.CurveBrepIntersect(brpElment,brpElments,0.01)
                            pt=rs.AddPoint(intersection[1][0])
                            coord=(intersection[1][0])
                            print (coord)
                            rs.AddTextDot("missing hole",coord)
                            if len(intersection[1])==2:
                                print ("Missing hole")
                        except:
                            pass

        rs.HideObjects(blocklistUnpcks)                    

# blocksInstIds=block_finder_ref.block_finder()[1]
# print (blocksInstIds)

if __name__ == '__main__':
    pass