#!/usr/bin/python3
import jsonrpclib
colorserver = jsonrpclib.Server('http://127.0.0.1:6711')
#print("Connected to color server with functions: %s" % (', '.join(colorserver.system.listMethods())))

def makefilter():
    return {
        'offeredInputs': input('space separated list of [txhash:index] entries: '),
        'quantityOffered': input('quantity offered: '),
        'requestedAsset': input('requested asset: '),
        'price': input('price: '),
        'kyc': input('kyc: '),
        'commitment': ''
    }

try:
    while True:
        cmd = input("\nType command ([G]et vout color, [M]ake transaction, [Q]uit)\n")
        if 'q' == cmd.lower(): break
        if 'g' == cmd.lower():
            print(colorserver.getvoutcolor(input("txhash:voutidx: ")))
            continue
        if 'm' == cmd.lower():
            print(colorserver.makeconversion(makefilter()))
            continue
except KeyboardInterrupt:
    from sys import exit
    exit(0)
