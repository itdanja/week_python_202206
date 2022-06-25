
from operator import itemgetter # 외부라이브러리 가져오기 : itemgetter 메소드

# 책이름 과 저자별 정렬 함수
def makeIndex( ary , pos ) :    # 인수 : 배열 , 정렬기준
    beforeAry = []      #
    index = 0
    for data in ary :
        beforeAry.append( (data[pos] , index) )
        index +=1
    sortedAry = sorted( beforeAry , key=itemgetter(0) ) # sorted( 배열명 , key=itemgetter(인덱스번호) ) : 해당 인덱스 기준으로 정렬
    return sortedAry
# 이진검색
def bookSearch( ary , fdata ) :
    pos = -1
    start = 0
    end = len( ary )-1
    while (start <= end ) :
        mid = (start + end) //2
        if fdata == ary[mid][0] :
            return ary[mid][1]
        elif fdata > ary[mid][0] :
            start = mid + 1
        else:
            end = mid - 1
    return pos
#전역변수
# 책이름 , 저자
bookAry = [
        ['어린왕자' ,'쌩덱쥐베리'] , ['이방인','까뮈'] , ['부활' , '톨스토이'] ,
        ['신곡' , '단테'] ,  ['돈키호테' , '세르반테스'] , ['동물농장','조ㅈ오웰'] ,
        ['데미안' , '헤르만헤세'] , [ '파우스트','괴테'] , ['대지','펄벅']
    ]
nameIndex = [ ] # 책이름
nameIndex = makeIndex( bookAry , 0 )
print( " 정렬후 : " , nameIndex )

authIndex = [ ] # 저자이름
authIndex = makeIndex( bookAry , 1 )
print( " 정렬후 : " , authIndex )

btn = int(input("검색 카테고리 (1:책이름 2:저자이름 입력 : )" ) )

findname = ''
if btn == 1 :
    findname = input("책이름 : ")
    findpos =  bookSearch( nameIndex , findname )
    if findpos == -1 :
        print( findname +' 의 도서는 없습니다.')
    else :
        print( findname,'의 도서는 ' , findpos,' 위치에 있습니다.')
elif btn == 2 :
    findname = input("저자이름 : ")
    findpos = bookSearch( authIndex , findname )
    if findpos == -1 :
        print( findname +' 의 저자는 없습니다.')
    else :
        print( findname,'의 저자의 도서는 ' , findpos,' 위치에 있습니다.')
else:
    print("알수 없는 번호 입니다. ")















