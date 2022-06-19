# 난수 0~200 사이의 20개 생성 -> 내림차순 정렬
# 몇번 정렬이 이뤄 졌는지 정렬 횟수 출력

import random

def bubbleSort( ary ) :
    global count
    for end in range( len(ary)-1 , 0 , -1 ) :
        changeYN = False
        for cur in range( 0 , end ) :
            count +=1
            if ary[cur] > ary[cur+1] :
                ary[cur] , ary[cur+1] = ary[cur+1] , ary[cur]
                changeYN =True
        if not changeYN :
            break
    return ary
count = 0
dataAry = [ random.randint(0,200) for _ in range(20) ]
print(" 정렬 전 : " , dataAry )
dataAry = bubbleSort( dataAry )
print(" 정렬 후 : " , dataAry )
print(" 정렬 횟수 : " , count )
