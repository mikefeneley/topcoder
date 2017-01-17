
class Time:

    def whatTime(self, seconds):
        hours = seconds / 3600
        a = 3600
        leftover = seconds - hours * 3600
        minutes = leftover / 60
        final_sec = seconds - hours * 3600 - minutes * 60
        final = str(hours) + ":" + str(minutes)+ ":" + str(final_sec)
        return final
