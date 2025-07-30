from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque()
    total_time = 0

    for city in cities:
        city = city.lower()

        if city in cache:
            cache.remove(city) 
            total_time += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            total_time += 5

        cache.append(city)

    return total_time