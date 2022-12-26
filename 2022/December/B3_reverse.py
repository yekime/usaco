# Eric Kim 12/25
# December 2022: Bronze 3: Reverse Engineering
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1253

""" 
    Note:   By unanimous pair, I mean a position/value pair such that all inputs sharing the 
            bit position/value return 0 or return 1. For example:
            001 1
            101 1
            010 0
            A uninamous pair would be position 1 value 0 returns 1,
            while position 0 would be contested (bit value and return aren't 1-to-1)

    Simple solution:
        For each test case, do the following:
            For each bit (and each possible value per bit), count how many inputs return 0 and 1
                For a unanimous pair (position, value), delete the inputs.
                If no unanimous pair exists, then return "LIE".
                If there are no more inputs, then return "OK".
    


    This unravels the program line by line, as the first (used) line of the program
    will result in a unanimous pair. Let's say the pair is bit position 1 and value 0. 
    Every input with value 0 in position 1 will all return 1 or 0, as the program would
    have short-circuited and returned. Delete all of these inputs, which lets us ignore
    this first line. If the inputs can encode a program, then there should be no 
    unanimous pairs left. Otherwise, we will end up with only contested bits.
"""

T = int(input())


def get_unanimous(counts):
    for bit in range(2):
        for pos in range(len(counts)):
            if len(counts[pos][bit][0]) > 0 and len(counts[pos][bit][1]) == 0:
                return list(counts[pos][bit][0])
            if len(counts[pos][bit][1]) > 0 and len(counts[pos][bit][0]) == 0:
                return list(counts[pos][bit][1])
    return []


result = []
for t in range(T):
    input()
    N, M = tuple(map(int, input().split(" ")))
    inputs = set()
    counts = [[[set() for accpt in range(2)] for bit in range(2)] for pos in range(N)]

    for m in range(M):
        inp, accept = tuple(input().split(" "))
        inputs.add((inp, int(accept)))

    for inp, accept in inputs:
        for pos, bit in enumerate(str(inp)):
            counts[pos][int(bit)][accept].add((inp, accept))

    unanimous_inputs = get_unanimous(counts)

    while unanimous_inputs:
        for inp, accept in unanimous_inputs:
            for pos, bit in enumerate(str(inp)):
                counts[pos][int(bit)][accept].remove((inp, accept))

        for inp in unanimous_inputs:
            inputs.remove(inp)

        unanimous_inputs = get_unanimous(counts)

    result.append("LIE" if inputs else "OK")

print("\n".join(result))
