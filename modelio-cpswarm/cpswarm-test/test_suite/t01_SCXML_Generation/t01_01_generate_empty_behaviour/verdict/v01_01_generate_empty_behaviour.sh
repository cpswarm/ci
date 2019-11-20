#!/bin/bash

difference=$(diff -r /cpswarm-test/workspace/cpswarm_test_project/generated/Behavior.xml /cpswarm-test/test_suite/t01_SCXML_Generation/t01_01_generate_empty_behaviour/verdict/expected_result/generated/Behavior.xml)
if [ $(echo $difference | wc -c ) -gt 1 ]; then echo $difference > /errors_output/t01_01_generate_empty_behaviour.err; fi

