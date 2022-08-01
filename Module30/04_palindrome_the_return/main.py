import collections


def can_be_poly(str) -> bool:
    str = collections.deque(str)
    for _ in range(len(str) // 2):
        if str[0] == str[-1]:
            str.pop()
            str.popleft()
        else:
            return False
    return True


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))