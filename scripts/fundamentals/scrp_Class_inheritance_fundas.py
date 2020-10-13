# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:01:11 2020

@author: Ashish

Inhertiance in class: an example
"""
class Device:
    
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected")
        
# Inheritance
## Note: Inheritance in Python3 works by placing the class name in brackets for another class as shown below
class Printer(Device):
    
    def __init__(self, name, connected_by, capacity):
        # super() helps to inherit the Parent class methods
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
   
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print("Printing {pages} pages")
        self.remaining_pages -= pages
            
    
        
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()

