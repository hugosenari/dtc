'''
Created on Jun 30, 2012

@author: hugosenari
'''
from plugnplay import Plugin
from dtc.core.interfaces.indictable import Indictable
from dtc.core.interfaces.module import Module
from dtc.core.interfaces.starter import Starter
from dtc.core.interfaces.visible import Visible
from dtc.core.interfaces.runnable import Runnable

class Start(Plugin):
    '''
    Start app
    '''
    implements = [Module, Starter]

    #methods for Module
    @property
    def version(self, *arg, **vargs):
        return 1
       
    @property
    def require(self, *args, **vargs):
        return ('indictable',)
        
    @property
    def priority(self, *args, **vargs):
        return 1
    
    @property
    def title(self, *args, **vargs):
        return "Start dtc for linux"
    
    @property
    def description(self, *args, **vargs):
        return "Implement startup algol for dtc on linux"
    
    @property
    def author(self, *args, **vargs):
        return "hugosenari <hugosenari@gmail.com>"
    
    #methods for Starter
    def start(self, *arg, **args):
        tray = Indictable
        user_modules = []
        user_modules.extend(Visible.implementors())
        user_modules.extend(Runnable.implementors())
        for user_module in user_modules:
            if (Module in user_module.implements):
                tray.appendItem(user_module.title,
                                self.get_callback(user_module),
                                user_module.description)
        tray.show()

    def get_callback(self, item):
        ## I don't know why but define callback at start don't work
        def callback(*args, **kws):
            if hasattr(item,'show'):
                item.show(*args, **kws)
            elif hasattr(item,'run'):
                item.run(*args, **kws)
        return callback