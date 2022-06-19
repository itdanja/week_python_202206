# 버블 정렬 구현
def BubbleSort( ary ) :
    n = len( ary )                      # 1. 배열의 길이 변수
    for end in range( n-1 , 0 , -1 ) :  # 2. end : 비교 끝지점 : 마지막인덱스부터 0인덱스전까지 -1씩 감소 반복
        for cur in range( 0 , end ) :   # 3. cur : 현재 비교대산 : 0번인덱스부터 end 까지 1씩 증가
            if ary[cur] > ary[cur+1] :  # 4. 현재값이 다음값보다 더 크면
                ary[cur] , ary[cur+1] = ary[cur+1] , ary[cur] # 교체
    return ary

dataAry = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105]

print("정렬 전 : " , dataAry )
dataAry = BubbleSort( dataAry )
print("정렬 후 : " , dataAry )

"""
    알고리즘[ = 순서도  ]
    [ 44 , 33 , 77 , 55 ]
    1. n = 4
        2. end = 3 
            3. cur = 0  
                4. 44 > 33  : true : 교체          [ 33 , 44 , 77 , 55 ]
            3. cur = 1
                4. 44 > 77 :  false 
            3. cur = 2
                4. 77 > 55 : true 교체             [ 33 , 44 , 55 , 77 ]
        2. end = 2 
            3. cur = 0
                4. 33 > 44 : false 
            3. cur = 1
                4. 44 > 55 : false 
        2. end = 1 
            3. cur = 0
                4. 33 > 44 : false
    --------------------------------------------------------------------------
 
"""
