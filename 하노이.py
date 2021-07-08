From='A'
tmp='B'
to='C'
n=int(input('구하려는 원반의 갯수: '))


def honoi_tower(n,From,tmp,to):
    if n==1:
        print('원반 1을 %s에서 %s로 옮긴다. \n' %(From,to))
    else:
        honoi_tower(n-1,From,to,tmp)
        print("원반 %s를 %s에서 %s로 옮긴다. \n" %(n,From,to))
        honoi_tower(n-1,tmp,From,to)




print('원반이 %s개 있을 때 하노이 탑의 결과 \n\n' %n)
honoi_tower(n,From,tmp,to)
