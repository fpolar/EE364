import numpy as np
import matplotlib.pyplot as plt

#simulates an individual answering a question
#with probability of correctness p
def sim_question(p):
    return 1 if np.random.random() < p else 0

#N = class size
N = 100000
num_questions = 20
exp1 = [[sim_question(.9) for i in range(num_questions)] for a in range(N)]

num_above_90 = 0;

percents1 = []
for i in range(N):
	sum = 0
	for a in range(num_questions):
		sum += exp1[i][a]
	avg = sum/num_questions
	avg *= 100
	if avg >= 90:
		num_above_90 += 1
	percents1.append(avg)

print(num_above_90)

num_bins = 100
n, bins, patches = plt.hist(percents1, num_bins, facecolor='blue')

plt.xlabel('Score')
plt.ylabel('Number of students')
plt.title('Histogram of Scores on EE 364 Final \n with students correct %90 of the time')

plt.show()