'''
Created on Jun 30, 2012

@author: hugosenari
'''
import gtk
from plugnplay import Plugin
from dtc.core.interfaces.module import Module
from dtc.core.interfaces.mainloop import MainLoop
from dtc.core.interfaces.loggable import Loggable

class Start(Plugin):
    '''
    Start gtk
    '''
    implements = [Module, MainLoop]
    
    def __init__(self):
        self._running = False

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
    
    #methods for MainLoop
    def run(self, *arg, **args):
        Loggable.debug("dtc mainloop gtk", "start")
        try:
            gtk.main()
            self._running = True
        except:
            self._running = False
        
    def quit(self, *arg, **args):
        gtk.main_quit()
        self._running = False
        
    @property
    def running(self):
        return self._running


