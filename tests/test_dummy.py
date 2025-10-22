import pytest

def test_dummy_passes():
    assert True

def test_report_generation_trigger():
    # This doesn't test anything functional.
    # It's only here to ensure the report contains multiple test cases.
    assert 1 + 1 == 2

@pytest.mark.parametrize("x", [1, 2, 3])
def test_parametrized(x):
    assert x in [1, 2, 3]