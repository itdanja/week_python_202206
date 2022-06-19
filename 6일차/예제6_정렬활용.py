# 성적별 조 만들기
# 조는 2명 [ 성적이 높은 순 , 낮은 순 ]
#   98  70    63  50
# 98-50  1조
# 70-63  2조

# 정렬 함수 구현
def scoresort( ary ) :
    for end in range( 1 , len(ary) ) :
        for cur in range( end , 0 , -1 ) :
            if ary[cur-1][1] > ary[cur][1] :            # 이름 기준[0]  , 성적 기준 [1]
                ary[cur-1] , ary[cur] = ary[cur] , ary[cur-1]
    return ary

scoreAry = [ ['유재석',88] , ['강호동' , 99] , ['신동엽',71] , ['하하' , 78] , ['김희철',67] , ['김영철' , 92 ] ]
# 정렬 실행
print('정렬 전 : ' , scoreAry )
scoreAry = scoresort( scoreAry )
print('정렬 후 : ' , scoreAry )

# 조 만들기
for i in range( len(scoreAry)//2 ) :            # 1. 배열의 길이 나누기 2 만큼 반복처리
    print( scoreAry[i][0], ':' , scoreAry[ len(scoreAry)-1-i][0] )
    # i = 0일때     scoreAry[i][0] : 이름 ,        마지막인덱스 [ 길이-1 ] - i












