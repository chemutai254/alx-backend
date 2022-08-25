#!/usr/bin/env python3
"""Class that inherist from Baseclass"""
from base_caching import BaseCaching 


class BasicCache(BaseCaching):
    def put(self, key, item):
        """Assign item to the dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked with the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
