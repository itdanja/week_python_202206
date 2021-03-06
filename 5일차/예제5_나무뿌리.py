# 프랙탈 형태의 나무뿌리 그리기
import turtle       # 거북이 라이브러리 [ 그리기 라이브러리 ]

def tree( length ):         # length 이동 길이
    if length > 5 :             # 만약에 이동길이가 5보다 크면
        t.forward( length )     # 앞으로 이동
        t.right(20)             # 오른쪽 20도 회전
        tree( length-15 )       # 재귀
        t.left(40)              # 왼쪽 40도 회전
        tree( length-15 )
        t.right(20)             # 오른쪽 20도 회전
        t.backward(length)      # 이동한 만큼 되돌아오기

t = turtle.Turtle() # 거북이 객체 생성
t.left( 90 ) # 거북이 왼쪽으로 90도 회전

t.color("green")    # 거북이 선 색상
t.speed( 10 )        # 거북이 속도 [ 1 = 가장 느리게 ]
tree( 90 )          # 함수 호출 ( 이동길이=90 )


"""
    알고리즘=순서도 
    1.함수호출(30) -> 조건:true -> 30이동 -> 20오회전 -> 재귀함수
        2. 함수호출(15) -> 조건:true -> 20이동 ->  재귀함수
            3.함수호출(0) -> 조건:false
        2.                                          -> 40왼회전 -> 재귀함수 
            3.함수호출(0) -> 조건:false 
        2.                                                          -> 20오회전 -> 되돌아오기
    1. 함수호출(30) -> 조건:true -> 30이동 -> 40왼회전 -> 재귀함수                                                 40왼회전 -> 재귀함수
        2. 함수호출(15) -> 조건:true -> 20이동 ->  재귀함수
            3.함수호출(0) -> 조건:false
        2.                                          -> 40왼회전 -> 재귀함수 
            3.함수호출(0) -> 조건:false 
                                                                    -> 20오회전 -> 되돌아오기            

"""



















