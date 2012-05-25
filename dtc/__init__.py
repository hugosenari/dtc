'''
Created on May 14, 2012

@author: hugosenari
'''

import plugnplay
import logging
from os.path import walk
from pig.core import interfaces
from pig.core.interfaces import module
from pig.core.interfaces.module import _CoreModule
from pig import modules


class Pig(object):
    def __init__(self):
        dirs = []
        def set_plugin_dirs(arg, dirpath, files):
            dirs.append(dirpath)

        walk(interfaces.__path__[0], set_plugin_dirs, None)
        walk(modules.__path__[0], set_plugin_dirs, None)
        
        plugnplay.set_plugin_dirs(*dirs)
        
    def run(self, logger=logging, *args, **vargs):
        plugnplay.load_plugins(logger)
        _CoreModule.execute_modules(*args, **vargs)