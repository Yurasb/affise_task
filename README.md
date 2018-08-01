# Affise test task
This is test task for Affise

#### Testing scope
Functional testing of endpoints `offers` and `pixel`.
Only 3 cases are covered:
1. positive scenario
2. wrong API key
3. wrong HTTP method

Assertion level - response status code.

#### Out of scope
1. different payload data cases
2. response data validation

## Local running
Follow steps below to run locally.

#### Preparation
You need `tox` to build virtual environment:
>sudo pip install tox

#### Launch
Simply run `tox` command from root project folder. This will prepare virtual environment,
launch tests and generate XML report.
