#!/bin/bash

difference=$(diff -r /attack-tree/test_suite/t01_export/t01_02_export_tree/test/result /attack-tree/test_suite/t01_export/t01_02_export_tree/verdict/expected_result)
if [ $(echo $difference | wc -c ) -gt 1 ]; then echo $difference > /errors_output/t01_02_export_tree.err; fi

