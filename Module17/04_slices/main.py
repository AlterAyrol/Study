alphabet = 'abcdefg'

print(alphabet[:])
print(alphabet[::-1])
print(alphabet[::2])
print(alphabet[1::2])
print(alphabet[:1])

print(alphabet[:len(alphabet) - 2:-1])
print(alphabet[3:4])
print(alphabet[4:])
print(alphabet[3:5])
print(alphabet[4:2:-1])

# 1: abcdefg
# 2: gfedcba
# 3: aceg
# 4: bdf
# 5: a
# 6: g
# 7: d
# 8: efg
# 9: de
# 10: ed