# Eric Kim 12/26
# December 2022: Bronze 2: Feeding the Cows
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1252

"""
Try to put the G/H grass on the rightmost possible empty grass.
"""

T = int(input())
output = []

for t in range(T):
    N, K = tuple(map(int, input().split(" ")))
    cows = input()

    grass = list("." * N)
    count = 0

    last_g = float("-inf")
    last_h = float("-inf")

    for i, cow in enumerate(cows):

        # If our last G/H already covers the current grass, ignore
        if (cow == "G" and last_g + K >= i) or (cow == "H" and last_h + K >= i):
            continue

        for j in range(min(N - 1, i + K), max(i - K - 1, -1), -1):
            if grass[j] == ".":
                grass[j] = cow
                count += 1
                if cow == "G":
                    last_g = j
                else:
                    last_h = j
                break

    output.append(str(count))
    output.append("".join(grass))

print("\n".join(output))
