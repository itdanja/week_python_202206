# 삽입할 데이터의 위치를 찾는 함수
def findinsertIdx( ary , data ) :
    findIdx = -1                        # 1. -1 [ 인덱스 없다.]
    for i in range( 0 , len(ary) ) :    # 2. 0부터 배열길이까지 반복문
        if ary[i] > data :              # 3. 만약에 data 가 i번째 인덱스 보다 작으면
            findIdx = i                 # 4. 위치 찾기변수 에 i 저장
            break                       # 5. 반복문 종료
    if findIdx == -1 :                  # 6. 만약에 못찾으면
        return len( ary )               # 7. 마지막 인덱스
    else:
        return findIdx                  # 8. 찾았으면 findIdx 반환

# 자신의 위치를 찾기 실행
testary = [ ]
inspos = findinsertIdx( testary , 55 )  # 배열에서 55 위치 찾기
print("삽입할 위치 : " , inspos )

testary = [ 33 , 77 , 88 ]
inspos = findinsertIdx( testary , 55 )  # 배열에서 55 위치 찾기
print("삽입할 위치 : " , inspos )

testary = [ 33 , 55 , 77 , 88 ]
inspos = findinsertIdx( testary , 100 ) # 배열에서 100 위치 찾기
print("삽입할 위치 : " , inspos )

# 삽입정렬 실행
before = [ 188 , 162 , 168 , 120 , 50 , 150 , 170 , 105]
after = [ ]

print("정렬 전--> " , before )

for i in range( len(before) ) :              # 1. 기존 배열의 길이만큼 반복문 실행
    data = before[i]                        # 2. i번째 데이터 호출
    inspos = findinsertIdx( after , data )  # 3. i번째 데이터의 위치 찾기
    after.insert( inspos , data )           # 4. 새로운 배열의 찾은 위치에 데이터 추가
print("정렬 후--> " , after )

"""
    알고리즘 [ 순서도 ] 
    befor = [ 33 , 55 , 44 ] 
    after = [  ] 
    1. i = 0일때   ->  33   2.함수실행( [] , 33 )   ->  0  -> after[o] = 33 
        결과 : after = [ 33 ]
    2. i = 1일때   ->  55   2.함수실행( [33] , 55 ) ->  1  -> after[1] = 55 
        결과 : after = [ 33 , 55 ] 
    3. i = 2일때   ->  44   2.함수실행( [33,55] , 44 ) -> 1 -> after[1] = 44 
        결과 : after = [ 33 , 44 , 55 ] 
"""





























