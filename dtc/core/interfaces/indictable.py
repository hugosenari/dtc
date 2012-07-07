'''
Created on May 14, 2012

@author: hugosenari
'''

from plugnplay import Interface, Plugin
from dtc.core.interfaces.module import _CoreModule

class Indictable(Interface):
    '''
    Interface to create trat menus
    '''

    def appendItem(self, title, on_click, alt=None, menu_id=None, *args, **vargs):
        '''
        Must return an item id for
        '''
        
    def removeItem(self, item_id, menu_id=None, *args, **vargs):
        '''
        Remove one item from menu
        '''
    
    def show(self, *args, **vargs):
        '''
        Show hide tray icon
        '''
        

class _CoreIndictable(Plugin):
    implements = [_CoreModule]

    def execute_modules(self, *args, **vargs):
        pass