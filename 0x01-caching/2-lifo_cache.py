#!/usr/bin/env python3
"""
A python class
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A class that inherits from base_cache and has methods
    """
    def __init__(self):
        """
        The class' init method
        """
        super().__init__()
        self.seq = []

    def put(self, key, item):
        """
        Cache in LIFO order
        """
        if key is None or item is None:
            return
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.seq[-1]))
                del self.cache_data[self.seq[-1]]
                del self.seq[-1]
            self.seq.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
