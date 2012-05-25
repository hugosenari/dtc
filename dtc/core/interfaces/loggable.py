'''
Created on May 14, 2012

@author: hugosenari
'''

from plugnplay import Interface, Plugin
from pig.core.interfaces.module import _CoreModule

class Loggable(Interface):
    '''
    classdocs
    '''

    def info(self, title, message, *args, **vargs):
        '''
        Show info popup to user
        '''
        
    def warn(self, title, message, *args, **vargs):
        '''
        Show warn popup to user
        '''
        
    def error(self, title, message, *args, **vargs):
        '''
        Show error popup to user 
        '''
    
    def debug(self, title, message, *args, **vargs):
        '''
        Show debug messages for users
        '''


class _CoreLoggable(Plugin):
    implements = [_CoreModule]

    def execute_modules(self, *args, **vargs):
        pass