target = open('problemDataSet.txt', 'r')

lines = target.readlines()

target_problem_train = open('problemDataSetTraining.txt', 'w')

target_problem_test = open('problemDataSetTesting.txt', 'w')

i = 1
for line in iter(lines):
    if i < 3478:
        target_problem_train.write(line)
    else:
        target_problem_test.write(line)
    print(i)
    i += 1

target.close()
target_problem_train.close()
target_problem_test.close()

target = open('notProblemDataSet.txt', 'r')

lines = target.readlines()

target_problem_train = open('notProblemDataSetTraining.txt', 'w')

target_problem_test = open('notProblemDataSetTesting.txt', 'w')

i = 1
for line in iter(lines):
    if i < 3146:
        target_problem_train.write(line)
    else:
        target_problem_test.write(line)
    print(i)
    i += 1

target.close()
target_problem_train.close()
target_problem_test.close()
