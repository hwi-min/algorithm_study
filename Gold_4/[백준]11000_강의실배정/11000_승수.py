# Si에 시작해서 Ti에 끝나는 N개의 수업이 주어짐.
# 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 함.
# 수업이 끝난 직후에 다음 수업을 시작할 수 있다.
# 필요한 최소 강의실의 개수 구하기

import heapq

number_of_lectures = int(input())   # 강의 개수
lectures = []   # 강의들의 시작 시간, 종료 시간 담을 리스트
end_times = []  # 강의 종료 시간들을 담을 최소 힙

for _ in range(number_of_lectures):
    Si, Ti = map(int, input().split())
    lectures.append((Si, Ti))

# 시작 시간을 기준으로 정렬 (시작 시간 같으면 종료 시간 기준)
lectures.sort()

heapq.heappush(end_times, lectures[0][1])   # 시작 시간이 가장 빠른 강의를 최소 힙에 삽입

# 그 다음 강의부터 순회
for i in range(1, number_of_lectures):
    start_time, end_time = lectures[i][0], lectures[i][1]
    earliest_end_time = end_times[0]    # 최소 힙의 root (가장 빨리 끝나는 강의)

    if earliest_end_time <= start_time: # 가장 빨리 끝나는 시간보다 시작 시간이 늦다?
        heapq.heappop(end_times)        # 시작 시간보다 빨리 끝난 강의를 빼고
        heapq.heappush(end_times, end_time) # 시작 시간이 늦는 강의 삽입

    else:   # 가장 빨리 끝나는 시간이 시작 시간보다 늦다?
        heapq.heappush(end_times, end_time) # 그럼 (다른 강의는 안빼고) 그 강의도 최소 힙에 추가

print(len(end_times))   # 최소 힙의 길이가 필요한 최소 강의실의 개수
