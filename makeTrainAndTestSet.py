# target = open('problemDataSet.txt', 'r')
target = open('newProblemDataSetMarkedProcessed.txt', 'r')

lines = target.readlines()

# target_problem_train = open('problemDataSetTraining.txt', 'w')
#
# target_problem_test = open('problemDataSetTesting.txt', 'w')
target_problem_train = open('newProblemDataSetMarkedProcessedTraining.txt', 'w')

target_problem_test = open('newProblemDataSetMarkedProcessedTesting.txt', 'w')

i = 1
for line in iter(lines):
    if i < 5507:
        target_problem_train.write(line)
    else:
        target_problem_test.write(line)
    print(i)
    i += 1

target.close()
target_problem_train.close()
target_problem_test.close()

target = open('newNotProblemDataSetMarkedProcessed.txt', 'r')

lines = target.readlines()

target_problem_train = open('newNotProblemDataSetMarkedProcessedTraining.txt', 'w')

target_problem_test = open('newNotProblemDataSetMarkedProcessedTesting.txt', 'w')

i = 1
for line in iter(lines):
    if i < 5942:
        target_problem_train.write(line)
    else:
        target_problem_test.write(line)
    print(i)
    i += 1

target.close()
target_problem_train.close()
target_problem_test.close()
