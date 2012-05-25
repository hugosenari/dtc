'''
Created on May 14, 2012

@author: hugosenari
'''
from plugnplay import Interface


class Module(Interface):
    '''
    Interface for all modules
    '''
    @property
    def version(self, *args, **vargs):
        '''
        Return version of module
        '''
        return 1
    
    @property
    def require(self, *args, **vargs):
        '''
        Return others modules requirements
        '''
        return None
        
    @property
    def priority(self, *args, **vargs):
        '''
        Return priority of module
        '''
        return 1
    
    @property
    def title(self, *args, **vargs):
        '''
        Return name to display for modules list
        '''
        pass
    
    @property
    def description(self, *args, **vargs):
        '''
        Return description to show in modules list
        '''
        pass
    
    @property
    def icon(self, *args, **vargs):
        '''
        Return url or icon name for modules list
        '''
        pass
     
    @property
    def author(self, *args, **vargs):
        '''
        Return author information
        '''
        pass
        

class _CoreModule(Interface):
    '''
    Core Module for Modules
    '''
    def execute_modules(self, pnp=None, *args, **vargs):
        pass
    
    