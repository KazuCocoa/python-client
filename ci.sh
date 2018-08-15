#!/bin/bash

result=$(python -m autopep8 -r -d .)
if [[ $result ]] ; then
  echo $result
  echo "Please apply `python -m autopep8 -r -i .` and commit the result"
  exit 1
fi

python -m pylint --rcfile .pylintrc appium test --py3k
python -m pytest test/unit/*
