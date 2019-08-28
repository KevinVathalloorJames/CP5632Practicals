def main():
    score = float(input("Enter score: "))
    while score < 0:
        print("invalid score")
        score = float(input("Enter score: "))
    print(validate_score(score))


def validate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"


main()


