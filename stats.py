import csv
import sys
import os

stats = {
  "hacking_in_bash": 0,
  "hello_world": 0,
  "connect4": 0,
  "zoo": 0,
  "pokedeck": 0,
  "rpg": 0,
  # "rpg_ii": 0,
  # "LOL2D": 0,
  "dynamic_array": 0,
  "linked_list": 0,
  "generic_ds": 0,
  # "hash_table": 0,
  # "btree": 0,
  # "graph": 0,
  # "complexity": 0
}

files = os.listdir()
for file in files:
  if file.endswith(".csv") and not file.endswith("github2pokename.csv"):
    with open(file) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
        if "A" in row[1]:
          stats[row[0]] = stats[row[0]] + 1

import matplotlib.pyplot as plt

names = list(stats.keys())
values = list(stats.values())

plt.bar(range(len(stats)), values, tick_label=names)
plt.show()
