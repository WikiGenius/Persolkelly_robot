#!usr/bin/bash

# Reviewed  by Muhammed El-Yamani
# Date: 27/07/2022

for f in data/input*

do
echo "python test_v2.py $f"
python test_v2.py < $f

done
