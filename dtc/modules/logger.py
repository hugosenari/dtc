'''
Created on May 15, 2012

@author: hugosenari
'''
import logging


from plugnplay import Plugin
from pig.core.interfaces import loggable, module

logging.basicConfig(level=logging.INFO)

class Logger(Plugin):
    implements = [loggable.Loggable, module.Module]
    
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
        return "loggin system"
    
    @property
    def description(self, *args, **vargs):
        return "Implement logger using stdout, stderr"
     
    @property
    def author(self, *args, **vargs):
        return "hugosenari <hugosenari@gmail.com>"
    
    #methods for loggable
    def info(self, title, message, *arg, **vargs):
        logging.info("%s :: %s" % (title, message), *arg, **vargs)
    
    def warn(self, title, message, *arg, **vargs):
        logging.warn("%s :: %s" % (title, message), *arg, **vargs)
    
    def error(self, title, message, *arg, **vargs):
        logging.error("%s :: %s" % (title, message), *arg, **vargs)
    
    def debug(self, title, message, *arg, **vargs):
        logging.debug("%s :: %s" % (title, message), *arg, **vargs)
