import os
import sys
import time
from Simulator import *


#function to run by the daemon
def write_to_file():
    f = open("out.txt", 'w')
    for i in range(1,5):
        f.write("Writing i = " + str(i))
        time.sleep(2)

#function to double fork
def spawnDaemon(func):
    # do the UNIX double-fork magic, see Stevens' "Advanced
    # Programming in the UNIX Environment" for details (ISBN 0201563177)
    try:
        pid = os.fork()
        if pid > 0:
            # parent process, return and keep running
            return
    except OSError, e:
        print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1)

    os.setsid()

    # do second fork
    try:
        pid = os.fork()
        if pid > 0:
            # exit from second parent
            sys.exit(0)
    except OSError, e:
        print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1)

    # do stuff
    func()

    # all done
    os._exit(os.EX_OK)


if __name__ == "__main__":
    #spawnDaemon(write_to_file)
    spawnDaemon(Server().run)
