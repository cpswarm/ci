#!/bin/bash

for script in /attack-tree/jython_scripts/*.py; do
    [ -f "$script" ] || break
    Xvfb :1 -screen 0 1024x768x16 & DISPLAY=:1.0 modelio-open-source3.8 -consoleLog -workspace /attack-tree/workspace/ -project test_AttackTrees1 -batch $script

done
