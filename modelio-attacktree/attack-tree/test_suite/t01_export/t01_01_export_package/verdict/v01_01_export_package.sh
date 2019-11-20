#!/bin/bash

difference=$(diff -r /attack-tree/test_suite/t01_export/t01_01_export_package/test/result /attack-tree/test_suite/t01_export/t01_01_export_package/verdict/expected_result)
if [ $(wc -c < $(echo $difference)) -eq 0 ]; then echo $difference > /errors_output/t01_01_export_package.err; fi

