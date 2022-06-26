"""
    배낭문제
        1. 조건
            1. 배낭 최대 담을수 있는 7KG
            2. 보석 4가지
                금고 , 수정 , 루비 , 진주
                6kg    4kg   3kg    5kg
                13억    8억   6억    12억
        2. 배낭에 최대 가격 으로 보석 담기
"""

def backpack() :
    # 2차원 로 빈배열 생성[ 메모이제이션 배열 = 기록 방식 ]
    array = [ [0 for _ in range(maxWeight+1) ]  for _ in range(rowCount+1) ]
    print("보석\kg 1k 2k 3k 4k 5k 6k 7k")
    for row in range( 1 , rowCount+1 ) :        # 인덱스 1부터 보석의 개수 까지
        print( row , '개-->' , end=" ")
        for col in range( 1 , maxWeight+1 ) :   # 인덱스 1부터 최대 무게 까지
            #### 배낭에 최대 가격을 담기위한 코드
            # 보석의 무게가 열보다 크면 = 물건이 가방에 안들어가면
            if weight[row] > col :  #  금괴무게 > 현재배낭무게
                # 배열[행][열] = 배열[ 행-1 ][열]
                array[row][col] = array[row-1][col]
            else:
                value1 = money[row] + array[row-1][col-weight[row] ] # 현재 보석의 가격
                value2 = array[row-1][col]      # 위에 있는 인덱스
                array[row][col] = max( value1 , value2 )

            print("%2d" % array[row][col], end=" ")
        print()
    return array[rowCount][maxWeight]
# 전역변수
maxWeight = 7   # 배낭 최대 무게
rowCount = 4    # 보석 숫자
weight = [ 0 , 6 , 4 , 3 , 5  ] # 보석 무게 [ 0 , 금괴 , 수정 , 루비 , 진주  ]
money = [ 0 , 13 , 8 , 6 , 12  ] # 보석 금액[ 0 , 금괴 , 수정 , 루비 , 진주  ]

maxValue = backpack()
print("배낭에 담을수 있는 보석의 최대 가격 --> " , maxValue , '억원')

"""
    순서도 
        1. 2차원
            col = 무게  row = 보석 개수
                  0 1 2 3 4 5 6 7  = 현재 배낭의 무게 
            0개 : 0 0 0 0 0 0 0 0
            1개 : 0 0 0 0 0 0 13 13      [ 금괴 추가 ] 
            2개 : 0 0 0 0 8 8 13 13      [ 수정 추가 ] 
            3개 : 0 0 0 6 8 8 13 14      [ 루비 추가 -> 수정1개+루비1개 ] 
            4개 : 0 0 0 6 8 12 13 14     [ 진주 추가 ] 
        2. 반복수 
            row = 1 
                col = 1     array[1][1] = 0
                col = 2     array[1][2] = 0
                col = 3     array[1][3] = 0
                col = 4     array[1][4] = 0
                col = 5     array[1][5] = 0
                col = 6     array[1][6] = 13
                    13
                col = 7     array[1][7] = 13
                    13
            row = 2 
            
            row = 3 
            
            row = 4 
            
        
"""

























