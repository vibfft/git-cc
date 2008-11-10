import sys
import rebase, checkin, init, load, lshistory, sync

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        usage()
    
    commands = {\
        'init': init.init,\
        'rebase': rebase.rebase,\
        'checkin': checkin.checkin,\
        'load': load.load,\
        'lshistory': lshistory.lshistory,\
        'sync': sync.sync,\
    }
    commands[args[0]](args[1:])

def usage():
    print """usage: gitc COMMAND [ARGS]
        
    init        Initialise gitcc with a clearcase directory
    rebase      Rebase from Clearcase
    lshistory   Perform lshistory with correct format for snapshot
    load        Load history from snapshot file
    checkin     Checkin new git changesets to Clearcase
    sync        Copy symlinked files from Clearcase to Git manually"""
    sys.exit(2)

if __name__ == '__main__':
    main()