# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:30:35 2020
Modified on: 5 August 2020 4:30 pm
@author: Ashish
"""

class MaxSizeList(object):
    
    def __init__(self, max_val):
        self.max_size = max_val
        self.innerlist = []
    
    # append
    def push(self, obj):
        self.innerlist.append(obj)
        if len(self.innerlist) > self.max_size:
            self.innerlist.pop(3)

    def get_list(self):
        return self.innerlist
          
a = MaxSizeList(3)
a.push(10)
a.push(20)
a.push(30)
a.push(40)
print(a.get_list())
