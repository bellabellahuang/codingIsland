import sys
import argparse
import re


DATE_REGEX = re.compile('^\d{4}\/\d{2}\/\d{2}$')

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('report', default=None, help='The report for duplication check.')
  parser.add_argument('date', default=None,
    help='The day for which to check duplication (YYYY/MM/DD format)')

  args = parser.parse_args()
  if not DATE_REGEX.match(args.date):
    print(f'[ERROR] : Invalid date "{args.date}". Please use the YYYY/MM/DD format.')

  return args

class Main:
  def __init__(self):
    args = get_args()
    self.run()

  def run(self):
    print('do something here')

if __name__ == '__main__':
  try:
    Main()
  except Exception as e:
    print(f'[ERROR] : {e}')
    sys.exit(1)