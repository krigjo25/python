import pytest
from numb3rs import validate

#   Failing to catch numb3rs.py by only checking first byte of an IPV4address

def test_assertion_passes():

    #   Initializing variables, ips to be tested
    ip = '127.0.0.1'
    ip1 = '255.255.255.255'


    # Ensuring the test passes
    assert validate(ip) == True
    assert validate(ip1) == True

    return True

def test_exception():

    ip = '512.512.512.512'
    ip1 = '1.2.3.1000'
    ip2 = 'cat'
    ip3 = '2.'

    #   Ensure this raises an Exception
    with pytest.raises(Exception) as e:

        assert validate(ip) == e.value
        assert validate(ip1) == e.value
        assert validate(ip2) == e.value
        assert validate(ip3) == e.value

    return True
