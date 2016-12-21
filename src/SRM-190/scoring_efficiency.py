
class ScoringEfficiency:

    def getPointsPerShot(self, gameLog):
        
        points = 0
        free_attempted = 0
        field_attempted = 0

        for shot in gameLog:

            if('free' in shot and 'Missed' in shot):
                free_attempted += 1
            elif('free' in shot and 'Made' in shot):
                free_attempted += 1
                points += 1
            elif('2' in shot and 'Missed' in shot):
                field_attempted += 1
            elif('2' in shot and 'Made' in shot):
                field_attempted += 1
                points += 2
            elif('3' in shot and 'Missed' in shot):
                field_attempted += 1
            elif('3' in shot and 'Made' in shot):
                field_attempted += 1
                points += 3

        points_per_shot = float(points) / (field_attempted + 0.5 * free_attempted)
        return points_per_shot
