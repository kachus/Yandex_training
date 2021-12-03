station_num, a, b = input().split()
station_num=int(station_num)
a=int(a)
b=int(b)
if a>=b:
    station_1=b
    station_2=a
else:
    station_1=a
    station_2=b
if station_num<=100 and a!=b:
    st_ind_1=station_1-1
    st_ind_2=station_num - station_2
    di=(station_2-station_1) - 1
    dj=st_ind_2 + st_ind_1
    if di<=dj:
        print(di)
    else:
        print(dj)