
class LevelUp:

    def toNextLevel(self, expNeeded, received):
        for idx, level in enumerate(expNeeded):
            if level > received:
                return level - received
