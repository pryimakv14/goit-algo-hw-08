import heapq
import random

q = random.sample(range(1, 100), 20)

def merge(heap):
    if len(heap) == 1:
        res = heapq.heappop(heap)
        return res

    heapq.heapify(heap)
    print(heap)

    first_elem = heapq.heappop(heap)
    second_elem = heapq.heappop(heap)

    heapq.heappush(heap, first_elem + second_elem)

    return merge(heap)

print(merge(q))
