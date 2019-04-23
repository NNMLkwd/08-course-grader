def course_grader(param):
    return ""
def course_grader(test_scores):
    if min(test_scores) <= 50:
        return "fail"
    if sum(test_scores) / len(test_scores) >= 70:
        return "pass"
    else:
        return "fail"
   
   
if __name__ == "__main__":
    main()
