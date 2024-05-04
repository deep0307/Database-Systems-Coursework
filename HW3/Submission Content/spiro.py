import math
R=6
r=1
a=8
x={}
y={}
t=0.0
with open('sphw4.txt','w') as f:
    print("[",file=f)
    while t<=20*math.pi:
        x[t]=((R+r)*(math.cos((r/R)*t))-a*(math.cos((1+r/R)*t)))*0.0005
        y[t]=((R+r)*(math.sin((r/R)*t))-a*(math.sin((1+r/R)*t)))*0.0005
        x[t]=x[t] + 34.02065080511197
        y[t]=y[t] - 118.28548971781649
        print("{",file=f)
        print("},",file=f)
        t=t+0.1
    print("]",file=f)



