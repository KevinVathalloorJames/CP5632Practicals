
score = float(input("Enter score: "))
while score < 0:
    print("invalid score")
    score = float(input("Enter score: "))
if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

