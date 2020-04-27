n = int(input())
for i in range(n):
    x = input()
    y = input()
    ok = 0
    if(x[0] == 'o' or y[0] == 'o'):
        if (x[1] == 'b' or y[1] == 'b') and (x[2] == 'b' or y[2] == 'b'):
            ok = 1
    if(x[1] == 'o' or y[1] == 'o'):
        if (x[0] == 'b' or y[0] == 'b') and (x[2] == 'b' or y[2] == 'b'):
            ok = 1
    if(x[2] == 'o' or y[2] == 'o'):
        if (x[1] == 'b' or y[1] == 'b') and (x[0] == 'b' or y[0] == 'b'):
            ok = 1
    if ok == 1:
        print('yes')
    else:
        print('no')
