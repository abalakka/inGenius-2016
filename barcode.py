#!/usr/bin/python
from sys import argv
import zbar

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video0'
if len(argv) > 1:
    device = argv[1]

#proc.request_size(800,480)

proc.init(device, False)

# enable the preview window
proc.visible = False 

# read at least one barcode (or until window closed)
proc.process_one()

# hide the preview window
proc.visible = False

# extract results
for symbol in proc.results:
    # do something useful with results
    print '%s' % symbol.data

file = open('barcodeON', 'w')
file.write(symbol.data + "\n")
file.close()

execfile("mainScript2.py")
