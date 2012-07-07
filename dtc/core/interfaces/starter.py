'''
Created on May 14, 2012

@author: hugosenari
'''
from plugnplay import Interface, Plugin
from dtc.core.interfaces.module import _CoreModule


class Starter(Interface):
    '''
    For modules that start main program
    '''
    
    def start(self, *arg, **args):
        '''
        Start this class, this are called when app run
        '''
        pass


class _CoreStarter(Plugin):
    implements = [_CoreModule]
    
    def execute_modules(self, *args, **vargs):
        Starter.start(*args, **vargs);
