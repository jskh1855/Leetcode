class Solution:

    def getOppositeParty(self, party: str) -> str:

        return 'R' if party == 'D' else 'D'

    def predictPartyVictory(self, senate: str) -> str:

        total_remain = {'R':0, 'D': 0}
        total_banned = {'R':0, 'D': 0}

        win = ''

        while True:

            next_round = []

            for senator in senate:

                oppos_senator = self.getOppositeParty(senator)

                if total_banned[senator] == 0:

                    total_remain[senator] += 1
                    total_banned[oppos_senator] += 1
                    next_round.append(senator)

                else:

                    total_banned[senator] -= 1

            total_remain['R'] -= total_banned['R']
            total_remain['D'] -= total_banned['D']

            senate = next_round

            if total_remain['R'] <= 0 or total_remain['D'] <= 0:

                break
                
        return "Radiant" if total_remain['R'] > total_remain['D'] else "Dire"
