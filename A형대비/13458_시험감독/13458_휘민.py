import math
"""
N개의 시험장
- 감독관: 감독할 수 있는 응시자 수 B명
- 부감독관: 감독할 수 있는 응시자의 수 C명

## 조건
- 한 시험장에 총감독관은 1명만 있어야함
- 부감독관은 여러명 있어도 됨
"""
N = int(input()) # 시험장 개수
test_rooms = list(map(int, input().split())) # 각 시험장의 학생 수 리스트
# 총감독관이 감시할 수 있는 응시자 수 / 부감독관이 감시할 수 있는 응시자 수
spectator_ability, sub_spect_ability = map(int, input().split())

# 최소 감독관의 수
min_spectator = N # 한 시험장에 총감독관은 꼭 1명 들어가야하니까

# 전체 시험장을 순회하며 처리
for stu_cnt in test_rooms:
    stu_cnt -= spectator_ability # 각 값에서 총감독관이 감시할 수 있는 인원을 미리 빼고 시작
    # 아직 감시해야할 학생이 남은 반만
    if stu_cnt > 0:

        # 만약 부감독관이 감시할 수 있는 인원수가 반의 학생보다 많으면 감독관 +1
        if stu_cnt <= sub_spect_ability: min_spectator += 1
        
        # 이외의 경우는 
        else: min_spectator += math.ceil(stu_cnt / sub_spect_ability)
    
print(min_spectator)