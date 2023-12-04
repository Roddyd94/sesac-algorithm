import sys
sys.stdin = open(f"input-{4831}.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    stops = [0] * (N + 1)

    for i in chargers:
        stops[i] = 1
    
    answer = 0
    last_checkpoint = 0
    current_position = 0
    tries_left = K

    while last_checkpoint + tries_left < len(stops) - 1:
        if tries_left < 1:
            answer = 0
            break

        current_position = last_checkpoint + tries_left

        if stops[current_position] == 1:
            last_checkpoint = current_position
            answer += 1
            tries_left = K
        else:
            tries_left -= 1

    print(f'#{test_case} {answer}')
    # ///////////////////////////////////////////////////////////////////////////////////
