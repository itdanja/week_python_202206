""" 개선된 선택 정렬 """

#선택정렬 함수 [ 교환방식 ]
def selectionSort( ary ) :
    n = len( ary )                      # 1. 배열=리스트 의 길이
    for i in range( 0 , n-1 ) :         # 2. 배열의 모든 인덱스 반복 [ 0 ~ 마지막인덱스까지 ]
        minIdx = i                      # 3. i = 비교기준
        for k in range( i+1 , n ) :     # 4. k = 비교대상
            if ary[minIdx] > ary[k] :   # 5. 만약에 비교기준이 더 크면 [ > : 오름차순 , < : 내림차순 ]
                minIdx = k              # 6. 최솟값 인덱스 교체
        # 교체
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    return ary
# 정렬 실행
dataary = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105 ]
print(" 정렬 전 : " , dataary )
dataary = selectionSort( dataary )
print(" 정렬 후 : " , dataary )
"""
    ! : 변수는 변수끼리 대입 교체가 불가능 
    a = 3 , b = 5      교환 
    *. tmp 임시변수  
    1. tmp = a          임시변수 = 3      
    2. a = b            3 = 5 
    3. b = tmp          5 = 3 
    결과 : a = 5 , b = 3 , temp = 5
    
    알고리즘 
    [ 77 , 55 , 88 ] 
    1. i = 0 일때 minIdx=0  77        2. 77 > 55     minIdx=1
                                      2. 77 > 88     X 
        i = 0 , minIdx = 1   /  교환 [i] <--->  [minIdx]  / 77 <-->55 
    [ 55 , 77  , 88 ]
    
    2. i = 1 일때 minIdx = 1          2. 77 > 88      
        i = 1 , minIdx = 1   /  교환 [i] <--->  [minIdx]  / 77 <-->77 
        
    결과 : [ 55 , 77  , 88 ]
    
"""