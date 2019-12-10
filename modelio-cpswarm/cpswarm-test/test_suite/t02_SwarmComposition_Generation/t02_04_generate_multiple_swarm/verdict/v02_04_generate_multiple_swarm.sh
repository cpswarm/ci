#!/bin/bash

GENERATED_FILE=/cpswarm-test/workspace/cpswarm_test_project/generated/Swarm4.xml

if test -f "$GENERATED_FILE"; then 
    difference=$(diff -r  $GENERATED_FILE /cpswarm-test/test_suite/t02_SwarmComposition_Generation/t02_04_generate_multiple_swarm/verdict/expected_result/generated/Swarm4.xml)
    if [ $(echo $difference | wc -c ) -gt 1 ]; then echo $difference > /errors_output/t02_04_generate_multiple_swarm.err; fi
else
    echo "$GENERATED_FILE NOT FOUND !" > /errors_output/t02_04_generate_multiple_swarm.err
fi