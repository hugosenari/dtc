'''
Created on Jun 30, 2012

@author: hugosenari
'''
import plugnplay
import logging
from os import path

from dtc.core import interfaces
from dtc.core.interfaces.module import _CoreModule
from dtc import modules


class Dtc(object):
    def __init__(self, dirs = []):
        self.loaded_dirs = []
        def set_plugin_dirs(arg, dirpath, files):
            logging.debug('addind dir: %s to path', dirpath)
            self.loaded_dirs.append(dirpath)

        path.walk(interfaces.__path__[0], set_plugin_dirs, None)
        path.walk(modules.__path__[0], set_plugin_dirs, None)
        
        for directory in dirs:
            path.walk(directory, set_plugin_dirs, None)
        
        plugnplay.set_plugin_dirs(*self.loaded_dirs)
        logging.debug('Set up plugnplay')
        
    def run(self, logger=logging, *args, **vargs):
        plugnplay.load_plugins(logger)
        logging.debug('execute modules')
        for module in _CoreModule.implementors():
            module.execute_modules(*args, **vargs)
