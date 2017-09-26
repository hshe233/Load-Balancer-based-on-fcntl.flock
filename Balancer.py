#!/usr/local/python/bin/python
# coding=utf-8

from job.base import Config
from job.base import Lock
import sys
import logging
import os

def getHost():

    try:
        lock = Lock.Lock(Config.NODE_FILE)
        lock.acquire()
        
        # get current Config.NODE number
        f1 = open(Config.NODE_FILE, 'r')  
        currVal = f1.read()
        f1.close()
         
        # Config.NODE number + 1
        f2 = open(Config.NODE_FILE, 'w')
        try:
            if int(currVal) >= int(Config.NODE_NUM):
                nextVal = '1'
                f2.write(nextVal)
            else:
                nextVal = str(int(currVal) + 1)
                f2.write(nextVal)
        except Exception, e:
                print(e.message)
                nextVal = '1'
                f2.write(nextVal)
        
        f2.close()
    
    finally:
        # release lock
        lock.release()
    
    node = 'NODE' + nextVal
    
    writeLog(eval('Config.' + node))
    
    return eval('Config.' + node)

def writeLog(message):
    logger=logging.getLogger()
    filename='/usr/local/python2.7/lib/python2.7/site-packages/job/base/log'
    handler=logging.FileHandler(filename)
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    logger.info(message)