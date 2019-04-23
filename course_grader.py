def course_grader(test_scores):
   
    average_score = sum(test_scores)/len(test_scores)
    if all(avg_grade >= 50 and average_score >= 70 for avg_grade in test_scores):
        return "Pass"
        return "pass"

    else:
        return "Fail"
        return "fail"
