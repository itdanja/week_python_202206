# 1. 정렬이 없는 순차 검색 [ 중복검색 ]

# 중복 검색이 가능한 순차검색  정의
def seqSearch( ary , fdata ) :
    poslist = []    # 검색된 여러개를 저장하기 위한 배열 선언
    size = len( ary )
    for i in range( size ) :
        if ary[i] == fdata :
            poslist.append( i ) # 동일한 데이터의 인덱스를 배열 저장
    return poslist # 검색된 여러개를 반환

# 전역변수
dataAry = [ 188 , 50 , 168 , 50 , 105 , 120 , 177 , 50 ]
# 입력받기
finddata = int( input(" 검색할 데이터 : ") )
position = seqSearch( dataAry , finddata )
if position == [] : # 만약에 반환된 배열이 비어 있으면
    print( finddata , "가 없습니다." )
else: # 배열이 비어 있지 않으면
    print( finddata ,"는 " , position, '위치에 있음')