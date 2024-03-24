import pytest
from app import postproccess

def test_postprocess():
    assert postproccess([]) == ''
    assert postproccess([{"entity_group": '1'}, {"entity_group": '2'}]) == "1 2"
