# A도시는 전기버스를 운행하려고 한다. 
# 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 
# 중간에 충전기가 설치된 정류장을 만들기로 했다.

# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 
# 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 
# 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
import sys
sys.stdin = open('sample_input (2).txt','r')

t = int(input())
for tc in range(1, t+1) :
    # n : 정류장 개수, k : 한 번 충전으로 가는 양, m : 충전소 개수
    k, n, m = map(int, input().split())
    # 충전소 번호
    chargers = list(map(int, input().split()))
    # 충전 횟수
    count = 0
   
    # 각 충전소 별로 다음 충전소 까지의 거리를 잰다
    # 도착 시 현재 내 상태가 다음 충전소 까지 갈 수 있다면 pass
    # 아니면 충전. 마지막 충전소는 도착지점을 기준으로 함
    move_distance = 0
    battery = k
    for i in range(len(chargers)):
        # 이동량 계산
        if i == 0 : move_distance = chargers[i]
        else : move_distance = chargers[i] - chargers[i-1]
        
        # 다음 스테이션까지의 요구량 계산
        if i == len(chargers) - 1: 
            need_to_next_station = n - chargers[i]
        else : 
            need_to_next_station = chargers[i+1] - chargers[i]
        
        # 남은 배터리양 계산
        battery -= move_distance
        print(chargers[i], need_to_next_station, battery)
        # 종료 조건
        # 현재 상태에서 충전 해도 다음 정류장에 갈 수 없다면
        if need_to_next_station > k: count = 0; break
        else: # 충전 조건
            # 다음 정류소까지 갈 수 있고,
            # 현재 배터리가 다음 충전소까지 부족하다면 충전
            if battery < need_to_next_station:
                battery = k
                count += 1
            # 다음배터리까지 갈 수 있다면
            elif battery >= need_to_next_station:
                continue
        
    print(f'#{tc} {count}')