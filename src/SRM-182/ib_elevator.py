
class IBEvaluator:

    def getSummary(self, predictedGrades, actualGrades):
        
        num_predictions = len(predictedGrades)
        diff_holder = []

        for i in range(0, 7):
            diff_holder.append(0)

        for idx, grade in enumerate(predictedGrades):
            diff = abs(grade - actualGrades[idx])
            diff_holder[diff] += 1

        for idx, element in enumerate(diff_holder):
            diff_holder[idx] = diff_holder[idx] / float(num_predictions) * 100
        
        return tuple(diff_holder)
