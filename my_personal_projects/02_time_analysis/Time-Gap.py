'''
Time Gap
'''

# if time in pm means add 12 edge case 12:00 pm
def is_pm_in_time(x):
    if "pm" in x.lower():
        st = x.split()[0]
        time = st.split(":")
        time = list(map(int, time))
        if time[0] != 12:
            time[0] += 12
        return time
    elif "am" in x.lower():
        st = x.split()[0]
        time = st.split(":")
        time = list(map(int, time))
        if time[0] == 12:
            time[0] = 0
        return time

# initial time input
t1 = input("Enter initial time (ex: 8:22 am): ")
t1_new = is_pm_in_time(t1)

# final time input
t2 = input("Enter final time (ex: 7:15 pm): ")
t2_new = is_pm_in_time(t2)

# hours
if t2_new[0] < t1_new[0]:
    t2_new[0] += 24

# minutes
if t2_new[1] < t1_new[1]:
    t2_new[0] -= 1
    t2_new[1] += 60

# finding time gap
time_gap_hr = t2_new[0] - t1_new[0]
time_gap_min = t2_new[1] - t1_new[1]

# final result
print(f"time gap: {time_gap_hr} hr {time_gap_min} min")
