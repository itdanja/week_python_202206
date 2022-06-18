'''
    * 함수 : method=메소드=function
        함수 : 함(=상자) 수(=숫자) : 상자 안에 들어있는 수 -> 미리 상자안에 넣어둔 수
            -> 미리 정의된 수(코드)
        자원 : 메모리[기억장치]는 많이 사용하면 속도 느림
        1.함수 사용 하는 이유
            1. 함수 호출시 메모리 할당 -> 메모리 효율성 증가
            2. 코드의 재 활용성
            3. 인수와 반환
                -함수 안에 들어 가는 값에 따라 서로 다른 값를 반환!!!!!!!!

    * 재귀(recursion) : 어떤한 것을 정의할때 자기 자신을 참조[사용]하는 뜻
        = 자기 자신을 불러내기
        1. 최대 재귀 횟수 : 996회ㅣ
        2. 재귀함수는 호출횟수만큼 종료 해야한다!!!!
            ** 재귀 함수 3번 호출 했으면 종료도 3번 ~~~~
'''
# 재귀함수 구현1
# def openBox() : # 함수 정의
#     global i
#     i +=1
#     print(" 상자를 열기 실행횟수 :  " , i ) # 실행코드
#     openBox() # 함수내 함수호출
#     # 자기 자신을 계속 부르다보면 끝이 없다.
# i = 0
# openBox()   # 함수 호출

# 재귀함수 구현2 : 상자1->상자2->상자3 --------- 상자10 ->
def openBox2() :
    global count
    print(" 상자를 열기 ")
    count -= 1
    if count == 0 :
        print(" 선물 넣기 ")
        return
    openBox2()
    print(" 상자를 닫기 ")
count = 3
openBox2()
"""
    알고리즘[=순서도] 
        1. 함수호출->상자열기->count-1->조건=false->재귀함수
              2. 함수호출->상자열기->count-1->조건=flase->재귀함수
                    3.함수호출 ->상자열기->count-1->조건=true->선물넣기->return
              2. 상자닫기 -> return
        1. 상자닫기 -> return
"""
#재귀함수 구현3
def plusmethod( num ) :
    if num <= 1 : #만약에 1보다 작으면 함수 종료
        return 1
    return num + plusmethod( num- 1 )
print( plusmethod(3) )
"""
    1.함수호출(3) ->조건=false-> return 3 + 재귀함수(2)
        2. 함수호출(2) ->조건=false -> return 2 + 재귀함수(1)
            3. 함수호출(1) -> 조건=true -> return 1 
        2.  2 + 1
    1. 3 + 3 
    =6
"""






