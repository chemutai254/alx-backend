#!/usr/bin/env python3
"""FIFO Cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Calls the Parent init"""
    def __init__(self):
        super().__init__()
        self._keys = []

    def put(self, key, item):
        """Discard the first item put in cache (FIFO algorithm)"""
        if key is None or item is None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
                if key not in self.cache_data.keys():
                    print("DISCARD: {}".format(self._keys[0]))
                    self.cache_data.pop(self._keys[0])
                    self._keys.pop(0)
            self.cache_data[key] = item
            if key not in self._keys:
                self._keys.append(key)

    def get(self, key):
        """Returns the value of self.cache linked to the key
        Returns None if key is none or does not exist"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
