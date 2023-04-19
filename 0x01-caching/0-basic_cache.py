#!/usr/bin/env python3
"""
A python class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class that inherits from BaseCaching class
    """
    def __init__(self):
        """
        Init method for the class
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        A method that assigns to the dictionary self.cache_data
        the item value for the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        return self.cache_data
   
    def get(self, key):
        """
        A method that returns the value in self.cache_data lined to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
