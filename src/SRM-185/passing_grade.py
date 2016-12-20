
class PassingGrade:

    def pointsNeeded(self, pointsEarned, pointsPossible, finalExam):
       
        max_points = sum(pointsPossible) + finalExam
        earned_points = sum(pointsEarned)

        for i in range(0, finalExam + 1):
            final_score = earned_points + i
            final_grade = float(final_score) / float(max_points)
            
            if(final_grade >= 0.65):
                return i
        
        return -1
