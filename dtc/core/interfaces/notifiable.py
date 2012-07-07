'''
Created on May 14, 2012

@author: hugosenari
'''

from plugnplay import Interface, Plugin
from dtc.core.interfaces.module import _CoreModule

class Notifiable(Interface):
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
        
    def notify(self, title, message, icon, *args, **vargs):
        '''
        Show custon popup to user
        '''

class _CoreNotifiable(Plugin):
    implements = [_CoreModule]

    def execute_modules(self, *args, **vargs):
        pass