# 이진검색 구현
def binSearch( ary , fdata ) :
    pos = -1    # 검색된 결과의 인덱스 저장 하는 변수
    start = 0       # 시작인덱스 변수
    end = len( ary ) -1 # 끝인덱스 변수 [ -1 하는이유 ( 인덱스 0부터 ) ]

    while start <= end :    # start 부터 end 까지 반복처리
        mid = ( start+end ) // 2 # 가운데 인덱스 구하기
        if fdata == ary[mid] :  # 가운데 인덱스가 찾는 데이터와 같으면
            return mid          # 찾기 성공
        elif fdata > ary[mid] : # 만약에 찾는 데이터가 더 크면
            start = mid+1       # 가운데 인덱스 1 증가 -> start을 mid로 사용
        else:                   # 만약에 찾는 데이터가 더 작으면
            end = mid-1         # 가운데 인덱스 1 감소 -> start을 mid로 사용
    return pos  # 반환

#전역변수
# 정렬이 되어있는 배열
dataAry = [ 50 , 60 , 105 , 120 , 150 , 160 , 162 , 168 , 177 ,188 ]
finddata = int( input("검색할 데이터 : ") )
position = binSearch( dataAry , finddata )
if position == -1 :
    print( finddata , "가 없습니다. ")
else:
    print( finddata , "는 " , position , " 위치에 있음")



"""
    finddata = 168
    start = 0
    end = 9
                  mid = 4
            mid-3          mid=5
            만약에 더 크면     start = 5 end = 9  mid = 7
            만약에 더 작으면   start = 0 end = 3   mid = 1
"""
