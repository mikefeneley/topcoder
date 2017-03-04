
class CoinFlipsDiv2:

    def countCoins(self, state):
        if len(state) <= 1:
            return 0

        interesting = 0
        for idx, coin in enumerate(state):
            if idx == 0:
                if state[idx+1] != coin:
                    interesting += 1
            elif idx == len(state) - 1:
                if state[idx -1] != coin:
                    interesting += 1
            else:
                if state[idx -1] != coin or state[idx + 1] != coin:
                    interesting += 1
        return interesting 
