class Solution:
    def totalMoney(self, n):
        total = 0
        week = 0

        for day in range(n):
            total += week + (day % 7) + 1
            if day % 7 == 6:
                week += 1

        return total
