import logging

from dtc.Dtc import Dtc

def main(*args, **kws):
    dirs = kws.get('dirs', [])
    logging.basicConfig(level=kws.get('log_level', logging.DEBUG))
    loop = kws.get('mainloop', None)
    if not loop:
        logging.debug('no mainloop found')
        try:
            import gobject
            loop = gobject.MainLoop()
            logging.debug('importing gobject')
        except:
            logging.debug('cant import gobject')
    Dtc(dirs).run(logger=logging, mainloop=loop, **kws);
    try:
        loop.run();
    except:
        logging.debug('end of dtc')
    return 0
    
if __name__ == '__main__':
    import sys
    main(sys.argv)