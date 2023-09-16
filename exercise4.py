import re
open_file = open("C:\Python Program\mbox.txt")
count = 0
number_sum = 0

for line in open_file:
    line = line.rstrip()
    x = re.search('^New Revision: \d+', line)
    if x:
        number = x.group()
        find_num = int(number.split()[-1])
        count += 1
        number_sum += find_num

average = number_sum / count
print("Total %d lines are matched" % count)
print("Average: ", average)