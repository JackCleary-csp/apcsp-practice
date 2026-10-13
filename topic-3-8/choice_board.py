#Making choice board to track handicap in golf
handicap = 1.7
scores = [71, 72, 80, 75, 81, 70, 77, 79, 76, 79, 80, 85, 83, 74, 80]
course_rating = [73.7, 70.5, 73.1, 73.1, 70.6, 74.1, 69.7, 72.9, 73.7, 70.5, 73.1, 74.1, 75.2, 70.5, 73.4]
par = [72, 73, 71, 71, 72, 70, 72, 72, 71, 72, 71, 70, 71, 68, 72]
low_differentials =[]
low_scores = sorted(scores)[0:8]
differentials = []
max_score = scores[0]
min_score = scores[0]
avg_differential = 0

for i in range(0, len(scores), 1):
    low_differentials.append(scores[i] - course_rating[i])
    low_differentials = sorted(low_differentials)[0:8]

for i in range(0, len(low_scores), 1):
    differentials.append(scores[i] -72)
handicap = low_differentials[i] / 8

for i in range(0, len(scores), 1):
    if scores[i] > max_score:
        max_score = scores[i]
    if scores[i] < min_score:
        min_score = scores[i]

score_avg = scores[i] / len(scores) + 72
avg_differential = (sum(scores) / len(scores)) - (sum(course_rating) / len(scores))

print(handicap)
print(score_avg)
print(max_score)
print(min_score)
print(low_differentials)
print(avg_differential)
#assuming all courses are par 72 and rating of 72, this is the handicap I get, for my Upgrade, I will be adding course ratings and different pars which means the differentials are different depending on the difficulty of the course

#Now I will be trying to add the ratings for courses and different differntials based on the difficulty of the course