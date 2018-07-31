import pytest


pytest.main(
    ['./tests/', '--junitxml=./test_report.xml']
)
