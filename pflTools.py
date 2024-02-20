
# import sys
# sys.path.append("C:\\Users\\Tomas.Mena\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib\\PFL")
from block_exploder import *
from block_finder_ref import *
from blockExploderSingle import *
from blockClash import *
from blockExplode import *

def __reverse_module_search(func_name):
    if func_name is None: return None
    if not isinstance(func_name, basestring): return None
    g_lower = dict((k.lower(),(k,v)) for k,v in globals().items())
    f_lower = func_name.lower()
    if f_lower in g_lower:
        f_data = g_lower[f_lower]
        if f_data[1]:
            try:
                full_module_name = f_data[1].__module__
                if full_module_name: return (f_data[0],full_module_name)
            except:
                return None
            
