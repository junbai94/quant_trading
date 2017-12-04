# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:07:44 2017

@author: j291414
"""

import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    socket.send("Server message to client3")
    msg = socket.recv()
    print msg
    time.sleep(1)