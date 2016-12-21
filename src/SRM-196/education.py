
class Education:

    def minimize(self, desire, tests):
        
        point_goal = -1
        if 'A' in desire:
            point_goal = 90
        elif 'B' in desire:
            point_goal = 80
        elif 'C' in desire:
            point_goal = 70
        elif 'D' in desire:
            point_goal = 60

        total = sum(tests)
        num_grades = len(tests) + 1

        for i in range(0, 101):
            final = total + i
            
            grade = final / num_grades

            if(grade >= point_goal):
                return i
        return -1
