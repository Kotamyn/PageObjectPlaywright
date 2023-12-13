#!/usr/bin/env sh

GENERAL_DIR=$(dirname $(pwd))

TESTS_DIR=$GENERAL_DIR/pop/tests/
PATH_ALLURE=$GENERAL_DIR/allure/bin/allure
PATH_RESULT_ALLURE=$GENERAL_DIR/allure_result/

pytest $TESTS_DIR --alluredir=$PATH_RESULT_ALLURE
sh $PATH_ALLURE serve --port 8080 $PATH_RESULT_ALLURE
