#!/usr/bin/env python
# Original idea and script by: artem [at] dinaburg [dot] org
# contact me: artem [at] dinaburg [dot] org
# 20110915 - Nick White, Added ability to enter domain as google.com or google .com
#   also added count to end of output

import sys
import socket

def bitflip(num, pos):
    shiftval = 1 << pos

    if num & shiftval > 0:
        return num & (~shiftval)
    else:
        return num | shiftval

def is_valid(charnum):
    if  (charnum >= ord('0') and charnum <= ord('9')) or\
        (charnum >= ord('a') and charnum <= ord('z')) or\
        (charnum >= ord('A') and charnum <= ord('Z')) or\
        charnum == ord('-'):
        return True
    else:
        return False

def usage():
    print "Usage:"
    print "bitsquat.py <domain name>.<extension>"
    print "bitsquat.py <domain name> <extension>"
    print ""
    print "example:"
    print "bitsquat.py google.com"
    print "or"
    print "bitsquat.py google .com"
    print ""

if __name__ == "__main__":

    if len(sys.argv) is 2:
        try:
            dn =[]
            dn = sys.argv[1].split('.')
            (name, suffix) = dn[:2]
            suffix = '.' + suffix
        except:
            name = sys.argv[1]
            suffix = ''
    elif len(sys.argv) is 3:
        name = sys.argv[1]
        suffix = sys.argv[2]
    else:
        usage()
        sys.exit()

    count = 0
    for i in range(0, len(name)):
        val = name[i]
        for bit in range(0,8):
            newval = bitflip(ord(val), bit)
            if is_valid(newval) and val.lower() != chr(newval).lower():
                newname = name[:i] + chr(newval)
                if i + 1 < len(name):
                    count += 1
                    newname += name[i+1:]
                    sys.stdout.write('%s%s\n' % (newname, suffix) )

                try:
                    ipaddr = socket.gethostbyname(newname + suffix)
                    sys.stdout.write('%s%s: is taken (%s)\n' % (newname, suffix, ipaddr,))
                except:
                    sys.stdout.write('%s%s might be available!\n' % (newname, suffix,))

    sys.stdout.write('\n%s: posible domains\n' % (count) )
