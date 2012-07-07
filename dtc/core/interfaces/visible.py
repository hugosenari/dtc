'''
Created on May 14, 2012

@author: hugosenari
'''

from plugnplay import Interface, Plugin
from dtc.core.interfaces.module import _CoreModule

class Visible(Interface):
    '''
    Define one module that can be visible
    '''
    
    def show(self, *args, **vargs):
        pass
    
    def hide(self, *args, **vargs):
        pass


class _CoreVisible(Plugin):
    implements = [_CoreModule]

    def execute_modules(self, *args, **vargs):
        pass