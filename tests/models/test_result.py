import pytest
import os
import shutil

from models.result import Result

OUTPUT_DIR = 'tmp/result/test'
RESULT_DATA = [
    "col1-1,col1-2,col1-3"
  , "col2-1,col2-2,"
  , "col3-1,col3-2"
]

def delete():
  if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)

def test_create_instance():
  result = Result()
  assert type(result) is Result

def test_output():
  delete()
  Result.output(RESULT_DATA)
  assert os.path.exists(Result.DEFAULT_RESULT_CSV)

  file_path = 'tmp/result/test/test_result_1.csv'
  Result.output(RESULT_DATA, file_path)
  assert os.path.exists(file_path)

  file_path = 'tmp/result/test/test_result_2.csv'
  Result.output(RESULT_DATA, file_path)
  assert os.path.exists(file_path)
  delete()
