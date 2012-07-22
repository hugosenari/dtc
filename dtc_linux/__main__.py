'''
Created on Jun 2, 2012

@author: hugosenari
'''
from dtc.__main__ import main as dtc_main
from dtc_linux.core import utils
from dtc_linux import modulares as modules

def main(*args, **kws):
    dirs = kws.get('dirs', [])
    dirs.append(modules.__path__[0])
    user_modules = utils.CoreConfigs.get_cfg_dir("modules", **kws)
    for directory in user_modules:
        print directory
        dirs.append(directory) 
    kws['dirs'] = dirs 
    dtc_main(**kws)

if __name__ == '__main__':
    main()

