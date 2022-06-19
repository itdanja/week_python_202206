# 삽입정렬 개선 #
def insertionsort( ary ) :
    n = len( ary )                          # 배열의 길이 변수
    for end in range( 1 , n ) :             # 인덱스 1부터 마지막 인덱스까지 반복
        for cur in range( end , 0 , -1 ) :  # end 부터 0까지 -1씩 감소 반복
            if ary[cur-1] > ary[cur] :      # 만약에 앞에 있는 인덱스보다 더 크면
                # tmp 없이 두 변수 교체방식
                ary[cur-1] , ary[cur]  = ary[cur] , ary[cur-1]
    return ary

dataary = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]

print("정렬 전 --> " , dataary )
dataary = insertionsort( dataary )
print("정렬 후 --> " , dataary )

"""
    [ 55 , 77 , 66 ] 
    1. n = 3
        2. end = 1 일때
            3. cur = 1 
                4.  55 > 77 false -> 교체x 
        2. end = 2 일때 
            3. cur = 2
                4.  77 > 66 true  -> 교체o
            3. cur = 1
                4.  55 > 66 false -> 교체x 
                
"""






