from itertools import cycle
count = 0
for i in cycle([1, 2, 3]):
    if count == 5:
        break
print(i, end=&#39; &#39;)
count += 1
