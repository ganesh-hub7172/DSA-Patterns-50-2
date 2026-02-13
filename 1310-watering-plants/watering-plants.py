class Solution:
    def wateringPlants(self, plants, capacity):
        steps = 0
        water = capacity
        
        for i in range(len(plants)):
            # Move from previous position to current plant
            steps += 1
            
            # If not enough water, go back to river and return
            if water < plants[i]:
                steps += 2 * i
                water = capacity
            
            # Water the plant
            water -= plants[i]
        
        return steps
