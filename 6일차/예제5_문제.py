# 랜덤 0 ~200 사이의 10개 난수 생성
# 삽입정렬[내림차순으로 정렬] 사용

import random

def insertionsort( ary ) :
    for end in range( 1 , len(ary) ) :
        for cur in range( end , 0 , -1 ) :
            if ary[cur-1] < ary[cur] :      # > 오름차순  / < 내림차순
                ary[cur-1] , ary[cur] = ary[cur] , ary[cur-1]
    return ary


randomary = [ random.randint( 0 , 200 ) for _ in range(10) ]
# random.randint( 0 , 200 )  0~200 사이의난수 발생
print("정렬 전 : " , randomary )
randomary = insertionsort( randomary )
print("정렬 후 : " , randomary )

