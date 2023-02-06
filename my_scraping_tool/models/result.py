import os

class Result:
  DEFAULT_RESULT_CSV = 'tmp/result.csv'

  @classmethod
  def output(self, results, result_csv_path=DEFAULT_RESULT_CSV):
    result_csv = result_csv_path if not result_csv_path is None and not result_csv_path == "" else self.DEFAULT_RESULT_CSV
    with open(result_csv, mode='w') as f:
      f.write('\n'.join(results))
    return
