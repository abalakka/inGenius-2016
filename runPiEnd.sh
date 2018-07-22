#!/bin/sh

python barcode.py > barcode.txt

python lineGrab.py

if ['python ./Matcher.py' == "1"]

then 
echo "Its A Match"

else 
echo "Not A Match"

fi
