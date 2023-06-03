import pytest
from working import convert # assuming the code is in a file named convert.py

# Define a fixture to provide the input and expected output for each test case
@pytest.fixture(params=[
  # (input, output)
  ("12:00 AM to 1:00 AM", "00:00 to 01:00"), # normal case
  ("11:55 PM to 12:05 AM", "23:55 to 00:05"), # crossing midnight
  ("1:30 PM to 2:30 PM", "13:30 to 14:30"), # same meridiem
  ("12 PM to 1 PM", "12:00 to 13:00"), # omitting minutes
  ("1 AM to 2 AM", "01:00 to 02:00"), # omitting leading zero
])
def time_case(request):
  return request.param

# Define a test function that uses the fixture and asserts the output matches the expected output
def test_convert(time_case):
  input_time, expected_output = time_case
  assert convert(input_time) == expected_output

# Define a fixture to provide the invalid input for each test case that should raise a ValueError
@pytest.fixture(params=[
  # input
  ("12:00 AM"), # missing "to"
  ("13:00 AM to 14:00 PM"), # invalid hour
  ("12:60 AM to 1:60 PM"), # invalid minute
])
def invalid_time(request):
  return request.param

# Define a test function that uses the fixture and asserts a ValueError is raised
def test_convert_invalid(invalid_time):
  with pytest.raises(ValueError):
    convert(invalid_time)
