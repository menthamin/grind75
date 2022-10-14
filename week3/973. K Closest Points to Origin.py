# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/
# 위상 정렬 문제?


# Fail
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
sqrt_res = []
res = []

for x, y in points:
    value = x ** 2 + y ** 2
    if len(sqrt_res) == k:
        if max(sqrt_res) > value:
            idx = sqrt_res.index(max(sqrt_res))
            sqrt_res[idx] = value
            res[idx] = [x, y]
    else:
        sqrt_res.append(value)
        res.append([x, y])

return res

# Min heap
import heapq

heap = []

for (x, y) in points:
    dist = -(x ** 2 + y ** 2)
    if len(heap) == K:
        heapq.heappushpop(heap, (dist, x, y))
    else:
        heapq.heappush(heap, (dist, x, y))

return [(x, y) for (dist, x, y) in heap]
