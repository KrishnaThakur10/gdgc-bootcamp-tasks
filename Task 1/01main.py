def calculate_result(a, b):
    if len(a[0]) != len(b):
        return -1
    result = []
    for i in a:
        let = 0
        for j in range(len(i)):
            let += (i[j] * b[j])
        result.append(let)
    return result

a = [[1, 2], [2, 4]]
b = [1, 2]
print(calculate_result(a, b))