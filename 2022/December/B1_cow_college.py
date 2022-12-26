# Eric Kim 12/24
# December 2022: Bronze 1: Cow College
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1251

"""
Simply sort the cows by tuition (descending).
The total revenue by setting the tuition to the i-th cow's maximum
would be the number of cows up to the current cow (inclusive) times
that maximum tuition of the i-th cow. Find the maximum such value,
and note the price. Note that the equality in Line 20 allows lower
prices (but same totals) to overwrite alternative maximum revenues
with smaller price points, as the problem requests the smallest 
price point that yields optimal revenue.
"""

N = int(input())
tuitions = sorted(list(map(int, input().split(" "))), reverse=True)
total = price = 0
for i, t in enumerate(tuitions):
    if t * (i + 1) >= total:
        total = t * (i + 1)
        price = t

print(total, price)
