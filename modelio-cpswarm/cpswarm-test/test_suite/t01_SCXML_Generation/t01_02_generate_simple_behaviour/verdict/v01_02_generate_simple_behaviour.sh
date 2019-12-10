#!/bin/bash

difference=$(diff -r /cpswarm-test/workspace/cpswarm_test_project/generated/Behavior.xml /cpswarm-test/test_suite/t01_SCXML_Generation/t01_02_generate_simple_behaviour/verdict/expected_result/generated/Behavior_2.xml)
if [ $(echo $difference | wc -c ) -gt 1 ]; then echo $difference > /errors_output/t01_01_generate_empty_behaviour.err; fi

