#!/bin/bash

# Deploy module on modelio test project
echo "------------->running deploy-module.py jython script" 
xvfb-run --auto-servernum --server-num=1 modelio-open-source3.8 -consoleLog -workspace /attack-tree/workspace/ -project modelio_test_project -batch /attack-tree/deploy-module.py

# Execute tests
for folder1 in /attack-tree/test_suite/*; do
    for folder2 in $folder1/*; do
        for script in $folder2/test/*.py; do
            [ -f "$script" ] || break
            echo "------------->running jython script : " $script
            xvfb-run --auto-servernum --server-num=1 modelio-open-source3.8 -consoleLog -workspace /attack-tree/workspace/ -project modelio_test_project -batch $script

        done
    done
done

# Verdicts
for f1 in /attack-tree/test_suite/*; do
    for f2 in $f1/*; do
        for s in $f2/verdict/*; do
            [ -f "$s" ] || break
            
            if [[ $s == *.py ]]; 
            then 
                echo "------------->running jython script : " $s
                xvfb-run --auto-servernum --server-num=1 modelio-open-source3.8 -consoleLog -workspace /attack-tree/workspace/ -project modelio_test_project -batch $s
            fi

            if [[ $s == *.sh ]]; 
            then 
                echo "------------->running bash script : " $s
                bash $s
            fi
        done
    done
done
