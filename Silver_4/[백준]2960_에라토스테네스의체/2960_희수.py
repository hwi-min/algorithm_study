n, k = map(int, input().split())

nums = [0] * (n + 1) # 숫자 순서 저장할 리스트
num = 2 # 소수, 2부터 시작
a = 0 # 숫자
idx = 0 # 순서

while True:
    idx += 1
    a += num # 배수

    if nums[a] == 0: # 중복 안된 숫자면
        nums[a] = idx # 해당 숫자 인덱스에 순서 값 저장
    else:
        idx -= 1 # 중복이면 패스 배수 한 번 더

    if idx == k: # k 번째 순서 됐으면 출력 + 끝내기
        print(a)
        break

    if a + num > n: # 배수가 n보다 크면 숫자 초기화, 다음 소수로
        a = 0
        num += 1