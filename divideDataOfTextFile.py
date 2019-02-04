target = open('x.txt', 'r')

lines = target.readlines()

target_problem = open('problemDataSet.txt', 'w')

target_not_problem = open('notProblemDataSet.txt', 'w')

i = 1
for line in iter(lines):
    if line[0] == '1':
        target_problem.write('problem ' + line[2:])
    if line[0] == '0':
        target_not_problem.write('noProblem '+line[2:])
    print(i)
    i += 1

target.close()
target_problem.close()
target_not_problem.close()
