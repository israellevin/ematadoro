#!/usr/bin/python3
import xmlrpc.client
colorserver = xmlrpc.client.ServerProxy('http://127.0.0.1:6711')
print("Connected to message server with functions: %s" % (', '.join(colorserver.system.listMethods())))

try:
    while True:
        cmd = input("\nType command ([G]et vout color, [M]ake transaction, [Q]uit)\n")
        if 'q' == cmd.lower(): break
        if 'g' == cmd.lower():
            print(colorserver.getvoutcolor(input("txhash:voutidx: ")))
            continue
        if 'm' == cmd.lower():
            print(colorserver.makeconversion(input("convert: ")))
            continue
except KeyboardInterrupt:
    from sys import exit
    exit(0)
