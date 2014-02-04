#!/bin/bash

curl -s http://localhost/radiator -o - | grep -A 2 "class='$1 '" | tail -1 | cut -d\> -f2 | cut -d\< -f1
