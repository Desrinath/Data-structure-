n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = 7
s = 0
e = len(n) - 1

while s <= e:
    mid = (s + e) // 2
    if n[mid] == t:
        print("Found at index:", mid)
        break
    elif n[mid] < t:
        s = mid + 1
    else:
        e = mid - 1
else:
    print("Not found")
