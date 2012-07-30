'''
Created on Jul 2, 2012

@author: hugosenari
'''

from plugnplay import Interface, Plugin
from dtc.core.interfaces.module import _CoreModule

class Element(Interface):
    '''
    Basic object for user interface
    '''
    
    def bind(self, event=None, fn=None, *args, **kws):
        '''
         Bind one event to one callback
        '''
        
    def bindList(self):
        '''
        Return one list with binded functions
        '''
        
    def label(self, text=None):
        '''
        Set or get label for this element
        '''
        
    def addClass(self):
        '''
        Insert one class in class list
        To use like class attr in html
        '''
    
    def rmClass(self):
        '''
        Remove one class in class list
        '''
        
    def classList(self):
        '''
        Return a list of classes
        '''
        
    def attr(self, name, val=None):
        '''
        Set, get attr
        '''
        
    def rmAttr(self, name):
        '''
        Remove a attr
        '''
        
    def style(self, prop=None, *args, **kws):
        '''
        Set, get style attr
        '''


class _CoreElement(Plugin):
    implements = [_CoreModule]

    def execute_modules(self, *args, **vargs):
        pass
    
    