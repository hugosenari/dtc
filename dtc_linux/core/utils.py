'''
Created on Jun 2, 2012

@author: hugosenari
'''
from xdg import BaseDirectory
import os

class CoreConfigs(object):
    @classmethod
    def get_cfg_dir(cls, component="", app_name='dtc', *args, **kws):
        return BaseDirectory.load_data_paths(os.path.join(app_name, component))