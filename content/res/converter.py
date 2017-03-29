#!/usr/bin/env python3
def perct2gp(per):
    '''Convert percentage to grade points'''
    p=[0, 60, 61, 64, 65, 68, 72, 75, 78, 82, 85, 90, 95, 100.1]
    gp=[0, 1, 1.3, 1.5, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 4.3]
    n=len(gp)
    if per<0 or per>100:
        return -1
    per=round(per)
    for i in range(n):
        if p[i] <= per < p[i+1]:
            return gp[i]
if __name__=='__main__':
    for i in range(-1,105):
        print(i,perct2gp(i))
