#확대 / 축소 : ctrl + 마우스 휠
# : 주석처리
"""여러줄 주석처리"""
# 주석 단축키 [ ctrl+ / ]
"""
    자료 구조 : 자료[데이터]구조[저장방법]
        사용이유 : 많은 양의 데이터를 효율적으로 저장 [ 빅데이터 ]
        예 ) 도서관 , 폴더 등등
        자료구조 종류 이용한 활용 연습
        
    알고 리즘 : 순서도[ 순서 대로 하는 행동 ]
        사용이유 : 컴퓨터 일처리 하는 순서 정리 
        예 ) 엘레베이터 , 지하철 등등 
        습관 : 한글로 알고리즘  ---->>  코드화 
        과제 :    
            1. 엘레베이터 알고리즘  --> 코드화 
            2. 신호등 알고리즘     --> 코드화
"""
# 파이썬 기본 문법
# 실행 단축키 : ctrl+shitf+f10
# tab 주의 !!!!

# 1. 출력함수 = print( )
print("내용 출력하는 함수")
# 2. 입력함수 = input( )
input("입력 : ")
# 3. 변수 : 변하는 수     vs      상수 : 고정된 수
# 변수[ 데이터 1개 저장 할 수 있는 메모리 / 저장된 데이터 는 바뀔수 있다. ]
# 상수[ 데이터 1개 저장 할 수 있는 메모리 / 한번 저장된 데이터 는 바뀔수 없다]
정수 = 10
print( " 정수변수에 저장된 데이터 " , 정수 )

입력변수 = input( "변수에 값넣기 : ")
print( " 입력한 데이터는 " , 입력변수 )

# 4.연산자 : 연산시 사용 되는 특수문자 [ 결과 얻어낼수 있는 특수문자 ]
변수1 = 10
변수2 = 3
# 산술연산자 : +더하기 -빼기 *곱하기 **거듭제곱 /나누기(실수) //나누기(정수) %나머지
print( 변수1 + 변수2 )
print( 변수1 - 변수2 )
print( 변수1 * 변수2 )
print( 변수1 ** 변수2 )
print( 변수1 / 변수2 )
print( 변수1 // 변수2 )
print( 변수1 % 변수2)
# 대입연산자 :
#   1. =  : 대입(오른쪽데이터 -> 왼쪽변수 )
#   2. += : 오른쪽 데이터를 왼쪽 데이터에 더한 후에 왼쪽 변수에 저장
#   3. -= : 오른쪽 데이터를 왼쪽 데이터에 뺀 후에 왼쪽 변수에 저장
#   4. *=    **=  /= //= %=
변수1 = 변수2
print( 변수1 )

변수1 += 변수2
print( 변수1 )

변수1 -= 변수2
print( 변수1 )

변수1 *= 변수2
print( 변수1 )

변수1 **= 변수2
print( 변수1 )

변수1 /= 변수2
print( 변수1 )

변수1 //= 변수2
print( 변수1 )

변수1 %= 변수2
print( 변수1 )

# 비교연산자 [ 결과는 true 아니면 false 반환 ]
    # == 같다   != 같지않다  >초과 <미만 >=이상 <=이하
print( "변수1 : " , 변수1  , " 변수2 : " , 변수2 )
print( 변수1 == 변수2 )
print( 변수1 != 변수2 )
print( 변수1 > 변수2 )
print( 변수1 < 변수2 )
print( 변수1 >= 변수2 )
print( 변수1 <= 변수2 )
# 논리연산자 [ 비교연산자가 두개 이상일때 and or / 결과반대 : not  ]
    # and 이면서 이고 모두 그리고 [ 앞뒤 비교연산자가 모두 참이면 참 ]
    # or 이거나 거나 하나라도 [ 앞뒤 비교연산자가 하나라도 참이면 참 ]
    # not 반전 [ 참->거짓 / 거짓 -> 참 ]
변수3 = 5
print( 변수1 < 변수2 and 변수1 < 변수3 )
    # 0 < 3 and 3 < 5  ==>    true and true  ==> true
print( 변수1 < 변수2 or 변수1 > 변수3 )
    # 0 < 3 or 0 > 5   ==>    true or false ==> true
print( not( 변수1 < 변수2 or 변수1 > 변수3 )  )
    # true ==> false    not true/false




















