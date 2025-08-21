'''
Gap-Time
'''

def hr_min_extractor(t):
    hr, k = t.split(":")
    m, meridian = k.split()
    hr = int(hr)
    m = int(m)
    return list([hr, m, meridian])

t1 = input("Enter time (ex: 5:30 am): ")
t1_l = hr_min_extractor(t1)
print(t1_l)

gap = input("Enter gap (ex: 6 hr 17 min as 6:17 g): ")
gap_l = hr_min_extractor(gap)
print(gap_l)

while gap_l[0]>=12:
    gap_l[0] -= 12
    if t1_l[2] == "am":
        t1_l[2] = "pm"
    elif t1_l[2] == "pm":
        t1_l[2] = "am"

t2_hr = t1_l[0] + gap_l[0]
t2_m = t1_l[1] + gap_l[1]

if t2_m>=60:
    t2_m -= 60
    t2_hr += 1

if t2_hr>12:
    t2_hr -= 12
    if t1_l[0] < 12:
        if t1_l[2] == "am":
            t1_l[2] = "pm"
        elif t1_l[2] == "pm":
            t1_l[2] = "am"

print("The time after the gap is: ")
print(f"{t2_hr}:{t2_m:02d} {t1_l[2]}")
