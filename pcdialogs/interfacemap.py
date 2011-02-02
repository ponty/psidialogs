from readsxc import OOSpreadData
from attribdict import attribdict

oosxc = OOSpreadData('interfacemap.ods',trim=1, strip=1)
header = oosxc[0]
indexdict = dict([ (s,i) for i,s in zip(range(len(header)), header)])
interfmapdict = []
for row in oosxc[1:]: 
    row = map(str,row)
    row += [''] * len(header)
    args = row[indexdict['parameter1']:]
    # rstrip
    args = [x for (x,y) in filter( lambda (x,y):bool(y) , zip(args, [''.join(args[x:]) for x in range(len(args))]) )]
##    args = ' '.join(args).split()
    try:
        group = int(row[indexdict['group']]    )
    except:
        group = None
    api = row[indexdict['api']]    
    function = row[indexdict['function']] 
    returntype = row[indexdict['returntype']] 
    if api and group and function:
        interfmapdict += [attribdict(dict(group=group, api=api, function=function, args=args, returntype=returntype))]
        
##print interfmapdict
COMMON = 'common'

def _select1(func):
    global interfmapdict
    rows = filter( func, interfmapdict)
#    print rows
#    assert( len(rows)<=1) 
    if len(rows):
        return rows[0]
    else:
        return None

def _selectMore(func):
    global interfmapdict
    rows = filter( func, interfmapdict)
##    assert( len(rows)>1) 
    return rows
    
def commonApiFunctions():
    rows = _selectMore( lambda r: r.api==COMMON)
    for row in rows:
        defrow = _select1( lambda r: r.api=='default' and r.group==row.group)
        if defrow:
            row.defaults = defrow.args;
        else:
            row.defaults = [None] * len(row.args);        
        row.defaults = ['None' if x is None else x for x in row.defaults]
    return [ (row.function , (row.args, row.returntype, row.defaults)) for row in rows]
    
class MapCommonApi2SelectedApi:
    def __init__(self, selectedName, inverse=0):
        self.api1 = COMMON
        self.api2 = selectedName
        if inverse:
            self.api1 ,  self.api2 = self.api2 ,  self.api1
    def func(self, api2_funcname):
        row2 = _select1( lambda r: r.api==self.api2  and r.function==api2_funcname)
        if row2:
            row1 = _select1( lambda r: r.api==self.api1  and r.group==row2.group)
            if row1:
                argmap = dict(zip(row2.args, row1.args))
                for (k,v) in argmap.items():
                    if not k or not v:
                        del argmap[k]
                return (row1.function , argmap)
        return (None , None)
    def allfunc(self):
        rows = _selectMore( lambda r: r.api==self.api2 )
        return [ (row.function) for row in rows]
                
    
