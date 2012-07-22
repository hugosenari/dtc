'''
Created on Jun 30, 2012

@author: hugosenari
'''
import plugnplay
import logging
from os import path

from dtc.core import interfaces
from dtc.core.interfaces.module import _CoreModule
from dtc.core.interfaces.mainloop import MainLoop
from dtc import modules


class Dtc(object):
    def __init__(self, dirs = []):
        self.loaded_dirs = []
        def set_plugin_dirs(arg, dirpath, files):
            logging.debug('add dir: %s to path', dirpath)
            self.loaded_dirs.append(dirpath)

        path.walk(interfaces.__path__[0], set_plugin_dirs, None)
        path.walk(modules.__path__[0], set_plugin_dirs, None)
        
        for directory in dirs:
            path.walk(directory, set_plugin_dirs, None)
        
        plugnplay.set_plugin_dirs(*self.loaded_dirs)
        logging.debug('Set up plugnplay')
        
    def run(self, logger=logging, *args, **vargs):
        logging.debug('load modules')
        plugnplay.load_plugins(logger)
        
        
        #get mainloop implementation
        mainloop = vargs.get('mainloop', None)
        if not mainloop:
            loops = MainLoop.implementors()
            if len(loops) > 0:
                mainloop = loops[0]
                vargs['mainloop'] = mainloop
        
        for module in _CoreModule.implementors():
            logging.debug('execute core module: %s', module)
            module.execute_modules(*args, **vargs)
        
        if mainloop:
            mainloop.run()