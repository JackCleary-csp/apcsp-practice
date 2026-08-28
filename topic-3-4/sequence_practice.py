"""
Topic 3-4: Sequence Practice
Required list and string operations, done in order, with predictions
made BEFORE running so I can check my mental model against reality.
"""

# ---------------------------------------------------------------------------
# PART 1: Starter data (checkpoint version)
# ---------------------------------------------------------------------------
scores = [72, 85, 91, 68, 88]
title = "weekly score report"

# Step 1: print the first, third, and last score using indexes
# Prediction: 72, 91, 88
print(scores[0])
print(scores[2])
print(scores[-1])

# Step 2: change the second score from 85 to 86, then print the list
# Prediction: [72, 86, 91, 68, 88]
scores[1] = 86
print(scores)

# Step 3: add 93 to the end with scores.append(93)
# Prediction: [72, 86, 91, 68, 88, 93]
scores.append(93)
print(scores)

# Step 4: create and print the substrings "weekly" and "report" from title
# title = "weekly score report"
#          0123456789...
# "weekly" is characters 0-5, "report" is the last 6 characters
# Prediction (WRONG on purpose, kept to show what I got wrong):
#   I first predicted report_part = title[12:] would give "report".
#   When I ran it, title[12:] actually printed " report" (with a leading
#   space) because index 12 lands on the space right before "report", not
#   on the "r". Counting "weekly score " character by character showed the
#   "r" in "report" is really at index 13. That's why the corrected slice
#   below uses title[13:] instead of title[12:].
weekly_part = title[0:6]
report_part = title[13:]
print(weekly_part)
print(report_part)

# Step 5: build a new label by concatenating a substring, ": ", and the
# number of scores converted with str()
# Prediction: "weekly: 6"
new_label = weekly_part + ": " + str(len(scores))
print(new_label)

# Step 6: print a clear report containing the new label and the list
print(new_label + " -> " + str(scores))

# Step 7: why can the list element be replaced but not a character in the string?
# A list in Python is mutable, so scores[1] = 86 is allowed: it reassigns
# the item stored at that position without creating a new list. A string
# is immutable, so title[0] = "W" would raise a TypeError -- you cannot
# change one character in place. To "edit" a string you have to build a
# brand new string (like the slicing/concatenation above) and assign that
# new string to the variable instead of modifying the old one.

# ---------------------------------------------------------------------------
# Boundary test: what does scores[len(scores)] do?
# ---------------------------------------------------------------------------
# Prediction: I expect this to return the last score, since len(scores) is
# "how many scores there are." Running it will show whether that's right.
try:
    print(scores[len(scores)])
except IndexError as error:
    print("IndexError:", error)
    # Actual result: this crashes with IndexError, not the last item.
    # len(scores) is 6, but valid indexes only go up to 5 (index 0-5 for a
    # 6-item list) because indexing starts at 0. len(scores) is one
    # position PAST the last real item, so it's out of range. My
    # prediction was wrong -- the correct way to get the last score is
    # scores[len(scores) - 1] (or just scores[-1], used in step 1 above).
    # The line below is the fixed version instead of leaving it broken:
    print(scores[len(scores) - 1])

# ---------------------------------------------------------------------------
# PART 2: My own meaningful example (after the checkpoint)
# ---------------------------------------------------------------------------
# Same required operations, applied to data that actually means something
# to me: my last five game scores from ranked matches, plus a title for
# the report.
game_scores = [14, 22, 9, 31, 18]
title2 = "ranked match kill report"

# Step 1: first, third, and last score using indexes
print(game_scores[0])
print(game_scores[2])
print(game_scores[-1])

# Step 2: change the second score, then print the list
game_scores[1] = 25
print(game_scores)

# Step 3: append a new score to the end
game_scores.append(27)
print(game_scores)

# Step 4: substrings from the title
ranked_part = title2[0:6]
kill_part = title2[13:17]
print(ranked_part)
print(kill_part)

# Step 5: concatenated label with a converted number
label2 = ranked_part + ": " + str(len(game_scores))
print(label2)

# Step 6: final report
print(label2 + " -> " + str(game_scores))

# Step 7 (repeated for this data set): game_scores[1] = 25 works because
# lists are mutable, but I could not do title2[0] = "R" the same way,
# because strings are immutable -- I would have to slice/concatenate a new
# string instead, exactly like ranked_part and kill_part above.
