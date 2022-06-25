# 판매제품별 판매수량의 정렬과 검색

#전역변수
#판매제품 배열
import random
def binSearch( ary , fdata ) :
    stat = 0
    end = len( ary ) -1
    while( stat <= end ) :
        mid = ( stat + end ) // 2
        if fdata == ary[mid] :
            return mid
        elif fdata > ary[mid] :
            stat = mid+1
        else:
            end = mid-1
    return -1
# 제품 목록
dataAry = ['나이키' , '아디다스' ,'리복' , '휠라','뉴발란스','언더아머' ]
# 제품 목록 20개의 랜덤으로 판매
sellAry = [ random.choice( dataAry ) for _ in range(20) ]
print( "중복O 정렬X"  , sellAry )
sellAry.sort()
print( "중복O 정렬O" , sellAry )
sellproduct = list( set(sellAry) )      # set 에는 동일한 데이터를 넣을수 없다 [ 중복제거 ]
print( "중복X" , sellproduct )
# 만약에 나이키 3개 중복이면  ( 나이키 : 3 ) -> 이진 탐색 이용
countlist = [ ]     # 제품별 판매수량 배열[리스트]
for product in sellproduct :    # 판매목록 반복문 실행
    count = 0           # 제품별 판매수량 저장되는 변수
    pos = 0             # 검색된  결과의 인덱스 저장도는 변수
    while pos != -1 : # 찾을 데이터가 없을때 까지  [ 검색결과가 없을때 까지 반복 ]
        pos = binSearch( sellAry , product )    # 판매목록과 검색제품
        if pos != -1 :  # 검색을 성공했으면
            count +=1   # 판매수량 증가
            del( sellAry[pos] ) # 검색된 데이터는 판매목록에서 제거
    countlist.append( (product,count) ) # 해당 제품의 검색이 끝났을때 제품별 판매수량 배열에 추가
print(" 결산 결과 : " , countlist )





