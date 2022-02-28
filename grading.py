import csv
import sys

if len(sys.argv) != 4 or (sys.argv[3] != 'A' and sys.argv[3] != 'B' and sys.argv[3] != 'C'):
  print("usage: ", sys.argv[0], " <lab> <github-name> <grade>\n\t<grade> must be A B or C.")
  exit(1)

with open('github2pokename.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  github2pokename = {};
  for row in csv_reader:
    github2pokename[row[0]] = row[1]

if not bool(github2pokename):
  print("ERROR: Run the grading file in the pf2-summer-2022 repository.")
  exit(1)

if sys.argv[2] in github2pokename:
  pokename = github2pokename[sys.argv[2]]
  pokefilename = pokename + ".csv"
  with open(pokefilename, 'a') as pokefile:
    csv_line = sys.argv[1] + ", " + sys.argv[3] + "\n"
    pokefile.write(csv_line)
    print("Wrote `" + csv_line[:-1] + "` in `" + pokefilename + "`.")
else:
  print("ERROR: Github nickname not recognized.")
  exit(1)
