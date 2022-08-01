# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result


diction = {}
def calculating_math_func(data, my_dict=dict()):
    result = 1
    if data in diction:
        result = result[data]
    else:
        for index in range(1, data + 1):
            result *= index
            my_dict[index] = id(result)
    result /= data ** 3
    result = result ** 10
    return result, my_dict


res, diction = calculating_math_func(5)
res2, diction = calculating_math_func(4)
print(diction)
print(res2)

