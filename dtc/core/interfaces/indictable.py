'''
Created on May 14, 2012

@author: hugosenari
'''

from plugnplay import Interface, Plugin
from pig.core.interfaces.module import _CoreModule

class Indictable(Interface):
    '''
    Interface to create trat menus
    '''

    def appendItem(self, title, on_click, menu_id=None, alt=None, *args, **vargs):
        '''
        Must return an item id for
        '''
        
    def removeItem(self, item_id, menu_id=None, *args, **vargs):
        '''
        Remove one item from menu
        '''

class _CoreNotifiable(Plugin):
    implements = [_CoreModule]

    def execute_modules(self, *args, **vargs):
        pass