# 중복을 고려한 퀵정렬 ##
def quickSort( ary ) :
    n = len( ary )
    if n <= 1 :
        return ary
    pivot = ary[ n//2 ]
    left , mid , right = [],[],[]       # 왼쪽 가운데 오른쪽
    for num in ary :
        if num < pivot :            #기준보다 더 작으면
            left.append(num)
        elif num > pivot :          #기준보다 더 크면
            right.append(num)
        else:                       #기준과 동일하면
            mid.append(num)
    return quickSort( left ) + mid +quickSort( right )

dataAry = [ 120 , 120 , 188 , 150 , 140 , 50 , 162 , 105 , 120 , 177 ,50 ]

print("정렬 전 --> " , dataAry )
dataAry = quickSort( dataAry )
print("정렬 후 --> " , dataAry )



