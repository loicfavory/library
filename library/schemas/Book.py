#!/usr/bin/python

from SQLiteManager import DB

class Book:
    def __init__(self, title):
        self.title = title
        print "Book title is " + title
