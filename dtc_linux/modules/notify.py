'''
Created on May 15, 2012

@author: hugosenari
'''

import pynotify
from plugnplay import Plugin
from dtc.core.interfaces.module import Module
from dtc.core.interfaces.notifiable import Notifiable

class Notify(Plugin):
    implements = [Module, Notifiable]
    
    def __init__(self, *args, **vargs):
        pynotify.init('Pig Notifier')
    
    #methods for module
    @property
    def version(self, *arg, **vargs):
        return 1
       
    @property
    def require(self, *args, **vargs):
        return None
        
    @property
    def priority(self, *args, **vargs):
        return 1
    
    @property
    def title(self, *args, **vargs):
        return "Notification system"
    
    @property
    def description(self, *args, **vargs):
        return "Implement notification using pynotify"
     
    @property
    def author(self, *args, **vargs):
        return "hugosenari <hugosenari@gmail.com>"

    #methods for notifiable
    def info(self, title, message, *args, **vargs):
        '''
        Show info popup to user
        '''
        self.notify(title, message, 'dialog-information')
       
        
    def warn(self, title, message, *args, **vargs):
        '''
        Show warn popup to user
        '''
        self.notify(title, message, 'dialog-warning')
        
    def error(self, title, message, *args, **vargs):
        '''
        Show error popup to user 
        '''
        self.notify(title, message, 'dialog-error')
        
    def notify(self, title, message, icon, *args, **vargs):
        '''
        Show custon popup to user
        '''
        n = pynotify.Notification (title, message, icon)
        n.show()