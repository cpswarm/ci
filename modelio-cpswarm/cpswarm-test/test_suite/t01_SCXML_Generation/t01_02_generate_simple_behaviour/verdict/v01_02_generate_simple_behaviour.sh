#!/bin/bash

GENERATED_FILE=/cpswarm-test/workspace/cpswarm_test_project/generated/Behavior_2.xml

if [test -f $GENERATED_FILE ]; then 
    difference=$(diff -r  $GENERATED_FILE /cpswarm-test/test_suite/t01_SCXML_Generation/t01_02_generate_simple_behaviour/verdict/expected_result/generated/Behavior_2.xml)
    if [ $(echo $difference | wc -c ) -gt 1 ]; then echo $difference > /errors_output/t01_02_generate_simple_behaviour.err; fi
else
    echo $GENERATED_FILE  " NOT FOUND !" > /errors_output/t01_02_generate_simple_behaviour.err
fi
