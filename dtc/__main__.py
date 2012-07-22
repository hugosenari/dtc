import logging

from dtc import Dtc

def main(*args, **kws):
    dirs = kws.get('dirs', [])
    logging.basicConfig(level=kws.get('log_level', logging.DEBUG))
    Dtc(dirs).run(logger=logging, **kws);
    logging.debug('end of dtc')
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)