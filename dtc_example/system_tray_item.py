'''
Created on Jul 2, 2012

@author: hugosenari
'''
from plugnplay import Plugin
from dtc.core.interfaces.module import Module
from dtc.core.interfaces.runnable import Runnable

class ItemOnSysTray(Plugin):
    implements = implements = [Module, Runnable]
    
    def __init__(self):
        self.running
    
    #methods for Module
    @property
    def version(self, *arg, **vargs):
        return 1
       
    @property
    def require(self, *args, **vargs):
        return None
        
    @property
    def priority(self, *args, **vargs):
        return 1
    
    @property
    def title(self, *args, **vargs):
        return "System tray item example"
    
    @property
    def description(self, *args, **vargs):
        return "Implement system tray item"
    
    @property
    def author(self, *args, **vargs):
        return "hugosenari <hugosenari@gmail.com>"
    
    #methods for Runnable
    def run(self, *args, **vargs):
        print "running"
        pass

    def rerun(self, *args, **vargs):
        print "rerunning"
        pass
    
    def kill(self, *args, **vargs):
        print "killing"
        pass
    
    def is_running(self, *args, **vargs):
        return False
