class Solution:
    def findingUsersActiveMinutes(self, logs, k):
        user_minutes = {}
        
        # Step 1: Collect unique minutes per user
        for user, time in logs:
            if user not in user_minutes:
                user_minutes[user] = set()
            user_minutes[user].add(time)
        
        # Step 2: Prepare result array
        answer = [0] * k
        
        # Step 3: Count UAM frequencies
        for minutes in user_minutes.values():
            uam = len(minutes)
            if uam <= k:
                answer[uam - 1] += 1
        
        return answer
