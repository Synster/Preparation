#!/bin/python3

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    result = []
    seq = [list() for _ in range(n)]
    lastAnswer = 0
    for query in queries:
        q, x, y = query
        if q == 1:
            seq[(x ^ lastAnswer) % n].append(y)
        else:
            s = seq[(x ^ lastAnswer) % n]
            lastAnswer = s[y % len(s)]
            result.append(lastAnswer)
            print(lastAnswer)

    return result


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
