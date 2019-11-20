#!/bin/bash

difference=$(diff -r /attack-tree/test_suite/t01_export/t01_02_export_tree/test/result /attack-tree/test_suite/t01_export/t01_02_export_tree/verdict/expected_result)
if [ $(echo $difference | wc -c ) -ne 0 ]; then echo $difference > /errors_output/t01_02_export_tree.err; fi

