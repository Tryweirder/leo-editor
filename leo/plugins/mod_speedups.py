#@+leo-ver=4-thin
#@+node:ville.20090804155017.7590:@thin mod_speedups.py
#@<< docstring >>
#@+node:ville.20090804155017.7591:<< docstring >>
''' Experimental speedups

Various optimizations. Use at your own risk. 

If stuff breaks, disable this plugin before reporting bugs.


'''
#@-node:ville.20090804155017.7591:<< docstring >>
#@nl

__version__ = '0.0'
#@<< version history >>
#@+node:ville.20090804155017.7592:<< version history >>
#@@killcolor
#@+at
# 
# 0.1 VMV first version
#@-at
#@-node:ville.20090804155017.7592:<< version history >>
#@nl

#@<< imports >>
#@+node:ville.20090804155017.7593:<< imports >>
import leo.core.leoGlobals as g
import leo.core.leoPlugins as leoPlugins
import os.path

# Whatever other imports your plugins uses.
#@nonl
#@-node:ville.20090804155017.7593:<< imports >>
#@nl

#@+others
#@+node:ville.20090804155017.7594:init
def init ():

    ok = True # This might depend on imports, etc.

    return ok
#@-node:ville.20090804155017.7594:init
#@+node:ville.20090804155017.7596:g.toUnicodeFileEncoding
def speedup_toUnicodeFileEncoding(s, arg = None):
    #if g:
    #    print g.callers(5)
    return s    

import leo    

g.toUnicodeFileEncoding = speedup_toUnicodeFileEncoding



#@-node:ville.20090804155017.7596:g.toUnicodeFileEncoding
#@+node:ville.20090804155017.12332:os.path shortcuts
g.os_path_basename = os.path.basename
g.os_path_split = os.path.split
g.os_path_splitext = os.path.splitext
#g.os_path_expanduser = os.path.expanduser
g.os_path_abspath = os.path.abspath
#g.os_path_join = os.path.join
g.os_path_normpath = os.path.normpath
#g.os_path_finalize = os.path.abspath
#@nonl
#@-node:ville.20090804155017.12332:os.path shortcuts
#@+node:ville.20090804155017.12333:os_path_finalize caching

os_path_finalize_orig = g.os_path_finalize
os_path_finalize_join_orig = g.os_path_finalize_join

_finalized_cache = {}
_finalized_join_cache = {}

def os_path_finalize_cached (path,**keys):
    res = _finalized_cache.get(path)
    if res:
        return res
    res = os_path_finalize_orig(path, **keys)
    _finalized_cache[path] = res
    return res

def os_path_finalize_join_cached (*args,**keys):
    res = _finalized_join_cache.get(args)
    if res:
        #print "cache hit", args
        return res

    res = os_path_finalize_join_orig(*args, **keys)
    _finalized_join_cache[args] = res
    return res


g.os_path_finalize = os_path_finalize_cached



g.os_path_finalize_join = os_path_finalize_join_cached

#@-node:ville.20090804155017.12333:os_path_finalize caching
#@-others
#@nonl
#@-node:ville.20090804155017.7590:@thin mod_speedups.py
#@-leo
