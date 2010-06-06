# -*- coding: utf-8 -*-

# coding=utf-8
SYMBOLS = {'__call__':'()',
'__getattr__':'.*',
'__getitem__':'[]',
'__setitem__':'[]',
'__delitem__':'[]',
'__iter__':'for',
'__enter__':'with',
'__exit__':'with',
'__contains__':'in',
'__add__':'+',
'__radd__':'+',
'__iadd__':'+=',
'__sub__':'-',
'__rsub__':'-',
'__isub__':'-=',
'__mul__':'*',
'__rmul__':'*',
'__imul__':'*=',
'__div__':'/',
'__rdiv__':'/',
'__truediv__':'/',
'__rtruediv__':'/',
'__floordiv__':'/',
'__rfloordiv__':'/',
'__divmod__':'/',
'__rdivmod__':'/',
'__idiv__':'/=',
'__itruediv__':'/=',
'__ifloordiv__':'/=',
'__mod__':'%',
'__rmod__':'%',
'__divmod__':'%',
'__imod__':'%=',
'__pow__':'**',
'__rpow__':'**',
'__ipow__':'**=',
'__lshift__':'<<',
'__rlshift__':'<<',
'__ilshift__':'<<=',
'__rshift__':'>>',
'__rrshift__':'>>',
'__irshift__':'>>=',
'__and__':'&',
'__rand__':'&',
'__iand__':'&=',
'__xor__':'^',
'__rxor__':'^',
'__ixor__':'^=',
'__or__':'|',
'__ror__':'|',
'__ior__':'|=',
'__pos__':'+@',
'__neg__':'-@',
'__invert__':'~',
'__lt__':'<',
'__le__':'<=',
'__eq__':'==',
'__ne__':'!=',
'__gt__':'>',
'__ge__':'>=',
'__abs__':'abs()',
'__nonzero__':'bool()',
'__complex__':'complex()',
'__float__':'float()',
'__hex__':'hex()',
'__int__':'int()',
'__len__':'len()',
'__long__':'long()',
'__oct__':'oct()',
'__reversed__':'reversed()',
'__unicode__':'unicode()'}

###########
# helpers #
###########

def default(obj):
    return obj

def dicttolist(obj):
    return sorted([(x, y) for x, y in obj.iteritems()])

def listaddindex(obj):
    return zip(range(0, len(obj)), obj)

def classtolist(obj):
    return [("%s" % obj, vars(obj))]

def objtolist(obj):
    dic = vars(obj)
    temp = {}
    for k, v in vars(obj.__class__).iteritems():
        temp[k] = (k in dic and dic[k] or v)
    return [("%s" % obj, temp)]

def explored(t):
    return (t in (types.InstanceType, types.ClassType,
                 types.ListType, types.DictType))

###########
# print_r #
###########
import types

# depth
def print_r(obj=False, output = True, indent = 4, depth = 10):
    global TAB, MAXD
    if not obj:
        print "usage: print_r(object[, output[, indent[, depth]]])"
        return
    TAB = "".join([" " for x in range(0, indent)])
    MAXD = depth
    res = printtree(totree(obj))
    if output:
        print res
    return res

# make obj into a list
def totree(obj, depth = 0):
    if depth == MAXD:
        return "Max depth reached, change depth argument"
    tab = {types.InstanceType : objtolist,
           types.ClassType : classtolist,
           types.ModuleType : classtolist,
           types.ListType : listaddindex,
           types.DictType : dicttolist}
    if type(obj) not in tab:
        return obj
    return [{"name":x[0],
             "value":totree(x[1], depth + 1),
             "type":type(x[1])}
             for x in tab[type(obj)](obj)]

# print tree
def printtree(tree, tab = ""):
    if not (type(tree) is types.ListType):
        return tree
    return ((tab != "" and "\n" or "")
            +"\n".join([("%s%s = %s%s" %
                         (tab,
                          (x["name"] in SYMBOLS and
                           SYMBOLS[x["name"]] or
                           x["name"]),
                          explored(x["type"]) and x["type"] or "",
                          printtree(x["value"], tab + TAB)))
                        for x in tree]))
