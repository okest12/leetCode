import heapq
def median_after_each_input(datas):
    minHeap = []
    maxHeap = []
    median = 0
    for data in datas:
        if data >= median:
            heapq.heappush(minHeap, data)
        else:
            heapq.heappush(maxHeap, -data)

        if len(maxHeap) >= len(minHeap) + 2:
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        elif len(minHeap) >= len(maxHeap) + 2:
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))

        if len(maxHeap) == len(minHeap):
            median = (-maxHeap[0] + minHeap[0])/2
        elif len(maxHeap) > len(minHeap):
            median = -maxHeap[0]
        else:
            median = minHeap[0]
        print(data, end=':')
        print(median)


median_after_each_input([5,4,2,-3,7,9,0,1,3,8])
