

def shortest(*args):
    return min(len(i) for i in args)

string = 'abcdefg'
nums_tuple = (10, 20, 30, 40, 50)
some_list = [1, 5, 7, 9, 12]

pairs_list = ((string[i], nums_tuple[i], some_list[i]) for i in range(shortest(string, nums_tuple, some_list)))

print(pairs_list)

for i in pairs_list:
    print(i)