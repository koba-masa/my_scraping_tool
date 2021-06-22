import pytest
import os

from models.result import Result

RESULT_CSV_TEST = 'tests/test_result.csv'
RESULT_DATA = [
    "col1-1,col1-2,col1-3"
  , "col2-1,col2-2,"
  , "col3-1,col3-2"
]

def before():
  pass

def delete_file(target_path):
  if os.path.exists(target_path):
    os.remove(target_path)

def test_create_instance():
  result = Result()
  assert type(result) is Result

def test_output():
  assert Result.output(RESULT_DATA) is None
  assert os.path.exists(Result.DEFAULT_RESULT_CSV)

@pytest.mark.parametrize(
  "file_path, expect_file_path",
  [
      ("", Result.DEFAULT_RESULT_CSV)
    , (None, Result.DEFAULT_RESULT_CSV)
    , (RESULT_CSV_TEST, RESULT_CSV_TEST)
  ]

)
def test_output_with_file_path(file_path, expect_file_path):
  delete_file(expect_file_path)
  assert Result.output(RESULT_DATA, file_path) is None
  assert os.path.exists(expect_file_path)
  delete_file(expect_file_path)
