
class ProgressBar:

    def showProgress(self, taskTimes, tasksCompleted):
        
        total_time = sum(taskTimes)
        elapsed = 0
        
        for i in range(0, tasksCompleted):
            elapsed += taskTimes[i]
            percent_elapsed = float(elapsed) / float(total_time)
            
            pounds = int(percent_elapsed * 20)
            periods = 20 - pounds
            progress = pounds * '#' + periods * '.'
        
        return progress    
