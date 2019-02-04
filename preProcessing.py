from nltk.tokenize import RegexpTokenizer

# target = open('problemDataSetTraining.txt', 'r')
target = open('problemDataSetTesting.txt', 'r')
lines = target.readlines()

tokenizer = RegexpTokenizer(r'\w+')
# tokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!')

# target_problem = open('problemDataSetTrainingProcessed.txt', 'w')
target_problem = open('problemDataSetTestingProcessed.txt', 'w')

i = 1
for line in iter(lines):
    y = tokenizer.tokenize(line)
    y = map(str.lower, y)
    x = " ".join(y)
    target_problem.write(x + "\n")
    print(i)
    i += 1

target.close()
target_problem.close()
