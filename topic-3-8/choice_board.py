#Making choice board to track handicap in golf
handicap = 2
scores = [71, 72, 80, 75, 81, 70, 77, 79, 76, 79, 80, 85, 83, 74, 80]
low_scores = sorted(scores)[0:8]
differentials = []

for i in range(0, len(low_scores), 1):
    differentials.append(low_scores[i] - 72)
handicap = differentials[i] / 8

score_avg = scores[i] / len(scores) + 72

print(handicap)
print(score_avg)

#assuming all courses are par 72 and rating of 72, this is the handicap I get, for my Upgrade, I will be adding course ratings and different pars which means the differentials are different depending on the difficulty of the course