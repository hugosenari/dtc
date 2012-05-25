import plugnplay
import logging

from pig import Pig

def __main__(*args, **kws):
    logging.basicConfig(level=logging.DEBUG)
    
    #from dbus.mainloop.glib import DBusGMainLoop
    import gobject
    #DBusGMainLoop(set_as_default=True)
    loop = gobject.MainLoop()

    Pig().run(logger=logging, mainloop=loop);
    
    loop.run();
    
if __name__ == '__main__':
    __main__()