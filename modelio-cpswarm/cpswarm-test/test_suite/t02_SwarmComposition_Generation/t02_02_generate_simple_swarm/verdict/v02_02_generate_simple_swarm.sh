#!/bin/bash

GENERATED_FILE=/cpswarm-test/workspace/cpswarm_test_project/generated/Swarm2.xml

if test -f "$GENERATED_FILE"; then 
    difference=$(diff -r  $GENERATED_FILE /cpswarm-test/test_suite/t02_SwarmComposition_Generation/t02_02_generate_simple_swarm/verdict/expected_result/generated/Swarm2.xml)
    if [ $(echo $difference | wc -c ) -gt 1 ]; then echo $difference > /errors_output/t02_02_generate_simple_swarm.err; fi
else
    echo "$GENERATED_FILE NOT FOUND !" > /errors_output/t02_02_generate_simple_swarm.err
fi