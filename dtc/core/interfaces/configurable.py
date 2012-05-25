'''
Created on May 14, 2012

@author: hugosenari
'''
from plugnplay import Interface, Plugin
from pig.core.interfaces.module import _CoreModule

class Configurable(Interface):
    '''
    Define configure
    '''

    def options(self, *args, **vargs):
        pass
    
    def saveOptions(self, *args, **vargs):
        pass
    
    def openWindow(self, *args, **vargs):
        pass


class _CoreConfigurable(Plugin):
    implements = [_CoreModule]

    def execute_modules(self, *args, **vargs):
        pass