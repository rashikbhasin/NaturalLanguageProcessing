# target1 = open('new_problem_set_1.txt', 'r')
target1 = open('new_problem_set_-1.txt', 'r')
lines = target1.readlines()

# target_problem1 = open('newProblemDataSet.txt', 'w')
target_problem1 = open('newNoProblemDataSet.txt', 'w')

i = 1
line_count = 1
for line in iter(lines):
    print line_count
    target_problem1.write("0,"+line)
    line_count = line_count + 1

target1.close()
target_problem1.close()
