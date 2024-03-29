import sys
import argparse
import re
import csv
import json


DATE_REGEX = re.compile('^\d{4}\/\d{2}\/\d{2}$')
# CHANNEL_REGEX = re.compile('^UC[\w-]+')
# INPUT_REGEX = re.compile('^s3:\/\/[-\/\w]+\.zip$')
# OUTPUT_REGEX = re.compile('^s3:\/\/[-\/\w]+\/$')

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

  def csvReader(self):
    with open('videos.csv') as file:
      reader = csv.reader(file)
      videos = [row[0] for row in reader]
      print(f'Found videos: {videos}')

  def csvWriter(self):
    with open('some_file.csv', mode='w') as some_file:
      file_writer = csv.writer(some_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      file_writer.writerow(['John Smith', 'Accounting', 'November'])

  def jsonReader(self):
    with open('config.json', 'r') as file:
      json.load(file)

  def error(message):
    print("ERROR: " + message, file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
  try:
    Main()
  except Exception as e:
    print(f'[ERROR] : {e}')
    sys.exit(1)