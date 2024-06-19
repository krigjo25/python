# Importing Responsories
import sys
import pytest


from seasons import Date_to_min

def test_exceptions():

  with pytest.raises(SystemExit) as e:
    Date_to_min('25-02-1994')

  assert "Invalid date format, use YYYY-MM-DD" in str(e.value)

  with pytest.raises(SystemExit) as e:
    Date_to_min('199402-25')

  assert "Invalid date format, use YYYY-MM-DD" in str(e.value)

  with pytest.raises(SystemExit) as e:
    Date_to_min('1994-0225')

  assert "Invalid date format, use YYYY-MM-DD" in str(e.value)

  with pytest.raises(SystemExit) as e:
    Date_to_min('19940225')

  assert "Invalid date format, use YYYY-MM-DD" in str(e.value)


  with pytest.raises(SystemExit) as e:
    Date_to_min('1994-25-02')

  assert "Invalid date format, use YYYY-MM-DD" in str(e.value)
