#!/bin/bash

foo=$(curl -s http://localhost/radiator -o - | grep -A 2 "class='$1 '" | tail -1 | cut -d\> -f2 | cut -d\< -f1)
bar=$(curl -s http://localhost/radiator -o - | grep -A 2 "class='total '" | tail -1 | cut -d\> -f2 | cut -d\< -f1)

echo $(echo "scale=4; $foo/$bar" | bc)
