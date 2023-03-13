import csv
import sys
import os

def make_stats():
  return {
    "hacking_in_bash": [0,0,0],
    "hello_world": [0,0,0],
    "the_card_game": [0,0,0],
    "space_exploration": [0,0,0],
    "pokedeck": [0,0,0],
    "dynamic_array": [0,0,0],
    "linked_list": [0,0,0],
    "generics": [0,0,0],
    "hash_table": [0,0,0],
    "btree": [0,0,0]
  }

num_reviews = 0
stats = make_stats()
students = 0
successful_students = 0
files = os.listdir()
for file in files:
  if file.endswith(".csv") and not file.endswith("github2pokename.csv"):
    students = students + 1
    with open(file) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      student_stat = make_stats()
      for row in csv_reader:
        if row[0] == "connect4":
          row[0] = "the_card_game"
        elif row[0] == "zoo":
          row[0] = "space_exploration"
        elif row[0] == "rpg":
          continue
        num_reviews = num_reviews + 1
        if "A" in row[1]:
          student_stat[row[0]][0] = student_stat[row[0]][0] + 1
        if "B" in row[1]:
          student_stat[row[0]][1] = student_stat[row[0]][1] + 1
        if "C" in row[1]:
          student_stat[row[0]][2] = student_stat[row[0]][2] + 1
      for x in student_stat:
        if student_stat[x][0] > 0:
          stats[x][0] = stats[x][0] + 1
        elif student_stat[x][1] > 0:
          stats[x][1] = stats[x][1] + 1
        elif student_stat[x][2] > 0:
          stats[x][2] = stats[x][2] + 1

print("There are ", num_reviews, " reviews.")

import matplotlib.pyplot as plt

names = list(stats.keys())
values_a = [x[0] for x in stats.values()]
values_bc = [x[1] + x[2] for x in stats.values()]
# values_c = [x[2] for x in stats.values()]

values_abc = [x[0] + x[1] + x[2] for x in stats.values()]

values_none = [students - x for x in values_abc]

plt.bar(range(len(stats)), values_a, color='g', tick_label=names)
plt.bar(range(len(stats)), values_bc, color='r', bottom=values_a, tick_label=names)
# plt.bar(range(len(stats)), values_none, color='b', bottom=values_abc, tick_label=names)
# plt.bar(range(len(stats)), values_c, color='r', bottom=values_b, tick_label=names)
plt.show()
