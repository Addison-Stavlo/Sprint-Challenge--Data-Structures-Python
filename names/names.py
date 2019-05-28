import time
from heap_sort import heap_sort

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# --ORIGINAL SOLUTION--  O(n^2) - 12sec runtime
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# --FIRST PASS UPGRADE-- solution ~ 2sec runtime.
# duplicates = [i for i in names_2 if i in names_1]

# --STRETCH SOLUTION-- using only arr's.
# since heap only uses lists/arrays to function
# O(nlog(n)), 0.4 sec runtime
# sorted_1 = heap_sort(names_1)
# sorted_2 = heap_sort(names_2)

# duplicates = []

# i = 0
# j = 0

# while i < len(names_1) and j < len(names_2):
#     if sorted_1[i] == sorted_2[j]:
#         duplicates.append(sorted_1[i])
#         i += 1
#         j += 1
#     elif sorted_1[i] < sorted_2[j]:
#         j += 1
#     else:
#         i += 1


# -- BEST SOLUTION--, O(n).  hash table for the win.
# 0.01sec runtime
names_table = {}
duplicates = []
for name in names_1:
    names_table[name] = True

for name in names_2:
    if name in names_table:
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

