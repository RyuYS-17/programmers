def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while (scoville[0]<K):
        if len(scoville) < 2: return -1
        new = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, new)
        answer += 1

    return answer
    
if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    assert solution(scoville, K) == 2