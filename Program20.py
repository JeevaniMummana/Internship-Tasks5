from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))

    previous = float('inf')
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()

        if current > previous:
            possible = False
            break

        previous = current

    if possible:
        print("Yes")
    else:
        print("No")