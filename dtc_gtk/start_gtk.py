'''
Created on Jun 30, 2012

@author: hugosenari
'''
import gtk
from plugnplay import Plugin
from dtc.core.interfaces import module, starter, loggable

class Start(Plugin):
    '''
    Start gtk
    '''
    implements = [module.Module, starter.Starter]

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
        return "Start dtc-gtk for linux"
    
    @property
    def description(self, *args, **vargs):
        return "Implement startup algol for dtc-gtk"
    
    @property
    def author(self, *args, **vargs):
        return "hugosenari <hugosenari@gmail.com>"
    
    #methods for Starter
    def start(self, *arg, **args):
        loggable.Loggable.debug("dtc gtk", "start")
        gtk.main()