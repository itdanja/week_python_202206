# 재귀함수를 이용한 시에르핀스키 삼각형 구현
# 1. 터틀을 이용한 삼각형 그리기
# 2. 삼각형 안에 3개의 삼각형 그리기

# 삼각형( 120 *3 )
import turtle

def draw( length , n  ) :
        # length : 전체 삼각형의 길이
        # n : 함수당 재귀 횟수
    if n >= 1 :
        for i in range(3) :
            t.forward( length )
            t.left(120)
            draw( length/2 , n-1 )

t = turtle.Turtle()
t.speed( 100 )
draw( 200 , 3 )
