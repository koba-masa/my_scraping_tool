import os

class Result:
  DEFAULT_RESULT_CSV = 'tmp/result/result.csv'

  @classmethod
  def output(self, results, result_csv_path=DEFAULT_RESULT_CSV):
    directory_path = os.path.dirname(result_csv_path)
    if not os.path.exists(directory_path):
      os.makedirs(directory_path)

    with open(result_csv_path, mode='w') as f:
      f.write('\n'.join(results))
    return
