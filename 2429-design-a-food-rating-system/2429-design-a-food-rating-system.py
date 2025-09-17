import heapq

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.food_info = {}   
        self.cuisine_map = {} 
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [c, r]
            if c not in self.cuisine_map:
                self.cuisine_map[c] = []
            heapq.heappush(self.cuisine_map[c], (-r, f))

    def changeRating(self, food, newRating):
        cuisine, _ = self.food_info[food]
        self.food_info[food][1] = newRating
        heapq.heappush(self.cuisine_map[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_map[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_info[food][1]:
                return food
            heapq.heappop(heap)  
