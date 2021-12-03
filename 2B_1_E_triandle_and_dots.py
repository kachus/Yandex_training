d=int(input())
x,y=(int(i) for i in (input().split()))
Ax, Ay = 0, 0
Bx, By = d, 0
Cx, Cy = 0, d 
if (x<=d and y<=d) and (x**2+y**2 <= d**2) and(x>=0 and y>=0):
    print (0)
else:
    A_dist=((x-Ax)**2 + (y-Ay)**2)**0.5
    B_dist=((x-Bx)**2 + (y-By)**2)**0.5
    C_dist=((x-Cx)**2 + (y-Cy)**2)**0.5
    dist=[A_dist,B_dist, C_dist]
    if min(dist) == A_dist:
        print(1)
    elif min(dist) == B_dist:
        print(2)
    elif min(dist) == C_dist:
        print(3)