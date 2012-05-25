'''
Created on May 14, 2012

@author: hugosenari
'''
from plugnplay import Interface, Plugin
from pig.core.interfaces.module import _CoreModule


class Runnable(Interface):
    '''
    Define one runnable module
    '''

    def run(self, *args, **vargs):
        pass

    def rerun(self, *args, **vargs):
        pass
    
    def kill(self, *args, **vargs):
        pass
    
    def is_running(self, *args, **vargs):
        return False


class _CoreRunnable(Plugin):
    implements = [_CoreModule]

    def execute_modules(self, *args, **vargs):
        pass