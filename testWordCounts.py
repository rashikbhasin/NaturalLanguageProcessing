target1 = open('newProblemDataSetMarkedProcessed.txt', 'r')
target2 = open('newNotProblemDataSetMarkedProcessed.txt', 'r')
# target1 = open('newProblemDataSet.txt', 'r')
# target2 = open('newNoProblemDataSet.txt', 'r')
lines = target1.readlines()

target_problem1 = open('wordInProblemSet.txt', 'w')

i = 1
line_count = 1
problemDict = {}
for line in iter(lines):
    words = line.split(" ")
    for word in words:
        temp = word.strip()
        if temp in problemDict:
            problemDict[temp] = problemDict[temp]+1
        else:
            problemDict[temp] = 1
    print line_count
    line_count = line_count + 1

target1.close()

lines = target2.readlines()

target_problem2 = open('wordInNotProblemSet.txt', 'w')

i = 1
line_count = 1
notProblemDict = {}
for line in iter(lines):
    words = line.split(" ")
    for word in words:
        temp = word.strip()
        if temp in notProblemDict:
            notProblemDict[temp] = notProblemDict[temp]+1
        else:
            notProblemDict[temp] = 1
    print line_count
    line_count = line_count + 1

target2.close()


for key, value in problemDict.iteritems():
    if key in notProblemDict:
        if value - notProblemDict[key] > 50:
            target_problem1.write(str(key) + "," + str(value) + "," + str(notProblemDict[key])+ "\n")
    elif value > 50:
        target_problem1.write(str(key) + "," + str(value) + ",0" + "\n")

for key, value in notProblemDict.iteritems():
    if key in problemDict:
        if value - problemDict[key] > 50:
            target_problem2.write(str(key) + "," + str(value) + "," + str(problemDict[key])+ "\n")
    elif value > 50:
        target_problem2.write(str(key) + "," + str(value) + ",0" + "\n")

target_problem1.close()
target_problem2.close()

