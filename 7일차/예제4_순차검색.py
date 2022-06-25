#1. 정렬이 있는 순차 검색 [중복 허용 ]
# 정렬이 되어있는 배열의 순차검색 정의
def seqSearch( ary , fdata ) :
    poslist = []
    size = len(ary)
    for i in range( size ) :
        if ary[i] == fdata :
            # pos = i
            poslist.append( i )
        elif ary[i] > fdata :
            break
    return poslist

# 전역변수
dataAry = [ 188 , 50 , 168 , 50 , 105 , 120 , 177 , 50 ]
# 정렬하기
dataAry.sort()  #오름차순

# 입력받기
finddata = int( input(" 검색할 데이터 : ") )
position = seqSearch( dataAry , finddata )
if position == [] :
    print( finddata , "가 없습니다.")
else:
    print( finddata ,"는 " , position,'위치에 있음')