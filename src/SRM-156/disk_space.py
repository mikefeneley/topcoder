class DiskSpace:

    def minDrives(self, used, total):
        free = sorted(total, reverse=True)
        total_data = sum(used)
        i = 0
        for data in free:
            total_data -= data
            i += 1
            if(total_data <= 0):
                return i
        return i
