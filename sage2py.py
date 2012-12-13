#!/usr/bin/env python
import optparse
import glob
import os
import subprocess

def main():
    p = optparse.OptionParser(description="Convert all Sages files in cur dir to Python",
                                prog="sage2py",
                                version="0.1a",
                                usage="%prog")
    options, arguments = p.parse_args()

    for cur_sage_file in glob.glob("*.sage"):
        subprocess.call('$SAGE_ROOT/sage -preparse '+cur_sage_file, shell=True)

if __name__ == '__main__':
    main()
