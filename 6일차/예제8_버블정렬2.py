#개선된 버블정렬#
def bubbleSort( ary ) :
    n = len( ary )
    for end in range( n-1 , 0 , -1 ) :
        changeYN = False                # 자리 변경 여부 저장 변수
        print(" 싸이클 --> " , ary )
        ######################### 버블 정렬 #############################
        for cur in range( 0, end ) :
            if ary[cur] > ary[cur+1] :
                ary[cur] , ary[cur+1] = ary[cur+1] , ary[cur]   # 자리 변경
                changeYN = True # true
        ############################################################
        # 자리 변경이 한번도 존재 하지 않았으면 정렬 끝난 상태
        # 버블정렬의 특이점 : 특정 싸이클에서 자리 변경이 한번도 없을경우 정렬 완료~~~~
        if not changeYN :   # 만약에 False         # 만약에 자리 변경이 있을경우 다시 비교
            break           # 반복문 종료
    return ary

dataAry = [ 188 , 162 , 168 , 120 , 50 , 150 , 177 , 105]

print("정렬 전 : " , dataAry )
dataAry = bubbleSort( dataAry )
print("정렬 후 : " , dataAry )


