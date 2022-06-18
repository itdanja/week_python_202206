# 회문찾기
    # 회문 : 앞으로 읽었을때 와 뒤로 읽었을때 동일
# 3. 회문판단 함수
def palindrome( pstr ) : # 인수로 문자 받는다 .
    if len(pstr) <= 1 : # 해당 문자열 길이가 1보다 작으면
        return True     # True
    if pstr[0] != pstr[-1] :
        return False
    return palindrome( pstr[ 1:len(pstr)-1 ] )  # 첫 글자와 마지막 글자를 제외한 재귀함수

# 1. 배열 선언 [ 여러개 문자열 임의 저장 ]
strary = [ "reaver" , 'keyak' , 'borrow or rob' , "주유소의 소유주","살금 살금"]
# 2. 반복문
for str in strary : # 배열내 모든 문자열 하나씩 꺼내오기
    print( str , end = "---> ")
    str = str.lower().replace(' ' ,'') # 소문자로 변환과 공백제거
        # .lower() : 해당 문자열을 소문자로 변환
        # .replace('기존문자','새로운문자' ) : 기존문자가 새로운문자로 치환[교체]
    if palindrome( str ) : # 만약에 함수가 true 반환하면 회문이다
        print( 'O')
    else:                  # 만약에 함수가 false 반환하면 회문이 아니다 .
        print( 'x' )


'''                  
    1.함수호출(reaver) -> 조건1 = (6)false -> (r!=r)false -> retrun 재귀함수
        2.함수호출( eave ) -> 조건1 = (3)false -> (e!=e)false -> retrun 재귀함수 
            3. 함수호출( av ) -> 조건1 =(2)false -> (a!=v)true-> false
        2. false 
    1. false
    결과 : reaver ---> 회문이 아니다 . 
'''


























