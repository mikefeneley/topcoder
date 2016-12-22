
class MovingAverages:

    def calculate(self, times, n):

        averages = []

        for i in range(0, len(times) - n + 1):
            avg = 0
            
            for j in range(i, i + n):
                time = times[j]
                split_time = time.split(':')
               
                hours = split_time[0]
                minutes = split_time[1]
                seconds = split_time[2]
                total = 3600 * int(hours) + 60 * int(minutes) + int(seconds)
                avg += total
            
            averages.append(avg / n)
        
        return averages
