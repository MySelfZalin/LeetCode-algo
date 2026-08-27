class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        traffik = []
        for passengers, from_station, to_station in trips:
            traffik.append((from_station, passengers))
            traffik.append((to_station, -passengers))
        
        traffik.sort(key=lambda traffic: (traffic[0], traffic[1]))
        curr_people = 0
        
        for _, passengers in traffik:
            curr_people += passengers
            
            if curr_people > capacity:
                return False
        
        return True
        