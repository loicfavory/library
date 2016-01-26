#!/usr/bin/python

import sqlite3

class DB:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def tableExists(self, name):
        name = (name,)
        test = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", name)
        return test.fetchone() != None