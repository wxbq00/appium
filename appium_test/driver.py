from appium import webdriver
import os
import sys
import time
import logging
import logging.config
import threading

two=[]
ip=[]
def server(self):
    PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
    desired_caps={}

