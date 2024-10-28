import pytest


@pytest.mark.xfail(reason="not implemented yet")
def test_backend():
    assert "not implemented yet" == "should fail"  # noqa: PLR0133
