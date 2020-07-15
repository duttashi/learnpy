# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:32:49 2020

@author: Ashish

Class Composition Fundamentals
Typically, in pythin orogramming you'll be dealing with class composition more than class inheritance
"""

class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"BookShelf with {len(self.books)} books"
    
class Book:
    def __init__(self, name:str):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"
    
book = Book("Harry Potter")
book2 = Book("Python 101")

shelf = BookShelf(book, book2)

print(shelf)
        

