#!/usr/local/python/bin/python
# coding=utf-8

import os
import sys
import fcntl

class Lock:    
    def __init__(self, filename):        
        self.filename = filename    
        try:            
            self.handle = open(filename)        
        except IOError, e:            
            self.handle = open(filename, 'w')
    def acquire(self):
        fcntl.flock(self.handle, fcntl.LOCK_EX)
    def release(self):
        fcntl.flock(self.handle, fcntl.LOCK_UN)
        
    def __del__(self):
        self.handle.close()