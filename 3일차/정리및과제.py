
# 과제1 : (역순 프로그램)입력받은 문자열 꺼꾸로 출력 하는 프로그램[ stack 구현 ]
def push( char ) :  # 입력받은 데이터를 하나씩 저장
    # 문제 코드 작성 !!!!!!
    return

def pop( ) :        # 데이터 추출
    # 문제 코드 작성  !!!!!!
    return

String  = [ ]       # 입력받은 문자를 저장하는 리스트
while True :
    char = input(" 1개 문자입력( *입력시 종료 ) : ")
    if char == "*" :
        # 지금 입력받은 문자들을 꺼꾸로 출력
        for i in String :
            pop( )
        print("프로그램 종료 ")
        break
    else:
        push( push )
