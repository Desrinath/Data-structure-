a = [1, 2, 3, 4, 5, 6, 3, 0]
t = 3

s = 0
e = len(a) - 1

while s < e:
    mid = (s + e) // 2
    if a[mid] < a[mid + 1]:
        s = mid + 1
    else:
        e = mid
print(e)  


if a[e] == t:
    print(e, "yes found!")


a_s = 0
a_e = e - 1
found_a = False

while a_s <= a_e:
    a_m = (a_s + a_e) // 2
    if a[a_m] == t:
        print(a_m, "yes found in ASC")
        found_a = True
        break
    elif t < a[a_m]:
        a_e = a_m - 1
    else:
        a_s = a_m + 1

if found_a:
    print("no more going")
else:
    print("no found going to DESC")

    d_s = e + 1
    d_e = len(a) - 1
    found_d = False  

    while d_s <= d_e:
        d_m = (d_s + d_e) // 2
        if a[d_m] == t:
            print(d_m, "yes found in DESC")
            found_d = True
            break
        elif t > a[d_m]:  
            d_e = d_m - 1
        else:
            d_s = d_m + 1

    if found_d:
        print("finally!")
    else:
        print("aapdi oru elemenat eh ila da")