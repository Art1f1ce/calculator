A python 3 calculator used from the terminal

## What it will do
add, subtract, multiply and divide two numbers and display the result

## How to run it
enter the first number, operator (+, -, *, /), then second number.
the program prints the result, followed by the answer
run: python3 calculator.py
OR run via script: run.sh
to stop: ^C

## How to test it 
check requirements.md for test requirements
run -> source /opt/python-venv/sccm-4910/bin/activate
this activates the supplied SCCM4910 virtual environment to keep pytest seperate from the system Python
run -> python3 -m pytest --version
this checks that pytest is installed



finally run -> python3 -m pytest -v
followed by -> echo $?
this runs the test and checks the error status after

ALTERNITIVELY
run -> check.sh
script that runs local quality gate

## Test expectations
5 successes to pass and a '0' error status is expected
