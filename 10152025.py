# Mid term review
#8.5/20
# #5 c or d
# #8 a
# 10 a
# 11 False
# 12 False
# 13 True
# 14 True
# 15 True
# 16 num
# 17 >=
# 18 [0]
# 19 append
# 20 <

# Resource Section
# reflection.md - missed points, labeled it program5.py

# Program 1
def getstudentwith highscore(scores):
    current_high_score=0
    current_high_score_student="blank"
    for name in scores:
        score=scores[name]
        if score>=current_high_score
        current_high_score=score
        current_high_score_student=name
    return current_high_score_student

scores={}
while true
    name=input("name (type done to stop): ")
    if name == "done":
        break
    score=int(input("int score (0-100): "))
    score[name]
print(f"There are {len(scores)} students")
if len(scores) == 0:
    print("No Students")
else:
    high_scorer=get_high_score_student(scores)
    print(f"{high_scorer} scored the most with {scores{high_scorer}}")
print(scores)