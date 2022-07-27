#!usr/bin/bash

for f in input*

do
echo "python test_v2.py $f"
python test_v2.py < $f

done
