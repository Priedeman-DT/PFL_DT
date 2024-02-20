import rhinoscriptsyntax as rs
import Rhino.Geometry as rc
import block_finder_ref
import blockExploderSingle
import block_exploder



def blockExplode():
    blocksInstIds=block_finder_ref.block_finder()[1]
    block_exploder.blockExploder(blocksInstIds)

if __name__ == '__main__':
    pass