i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('{}*{}={} '.format(i,j,i*j),end='')
        j += 1
    print('')
    i += 1

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={} '.format(j,i,i*j),end='')
    print('')