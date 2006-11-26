# Copyright (c) 2005, the Lawrence Journal-World
# Copyright (c) 2005 Allan Saddi <allan@saddi.com>
# Copyright (c) 2006 L. C. Rees
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#    
#    2. Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#    3. Neither the name of Django nor the names of its contributors may be used
#       to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''Thread-safe in-memory cache backend.'''

import copy
import time
try:
    import threading
except ImportError:
    import dummy_threading as threading
from shove.cache.simple import SimpleCache
from shove import synchronized

__all__ = ['MemoryCache']

class MemoryCache(SimpleCache):

    '''Thread-safe in-memory cache backend.'''    

    def __init__(self, *a, **kw):
        super(MemoryCache, self).__init__(*a, **kw)
        self._lock = threading.Condition()

    @synchronized
    def __setitem__(self, key, value):
        '''Set a value in the cache.  

        @param key Keyword of item in cache.
        @param value Value to be inserted in cache.        
        '''
        super(MemoryCache, self).__setitem__(key, value)

    @synchronized        
    def __getitem__(self, key):
        '''Fetch a given key from the cache.

        @param key Keyword of item in cache.
        '''        
        now, exp = time.time(), self._expire_info.get(key)
        if exp < now: del self[key]
        return copy.deepcopy(self._cache[key])        

    @synchronized
    def __delitem__(self, key):
        '''Delete a key from the cache, failing silently.

        @param key Keyword of item in cache.
        '''
        super(MemoryCache, self).__delitem__(key)        

    @synchronized        
    def get(self, key, default=None):
        '''Fetch a given key from the cache.  If the key does not exist, return
        default, which itself defaults to None.

        @param key Keyword of item in cache.
        @param default Default value (default: None)
        '''        
        now, exp = time.time(), self._expire_info.get(key)
        if exp is None:
            return default
        # Return default value if item expired
        elif exp < now:
            del self._cache[key]
            return default
        else:
            return copy.deepcopy(self._cache[key])