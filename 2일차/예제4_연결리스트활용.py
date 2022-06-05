# 구현 프로그램 : 회원들의 전화번호부
    # 1. 연결리스트 구현

#1. 노드 클래스 선언
class Node() :
    def __init__(self):
        self.data = None
        self.link = None
#2. 노드 추가 함수 구현
def add_node( info ) :
    #전역변수 호출
    global head , current

    node = Node()       # 1. 노드 객체 선언
    node.data = info    # 2. 노드에 데이터[입력받은정보] 추가

    if head ==None  : # 만약에 헤드가 없으면 [ 첫 노드 생성 !!! ]
        head = node     # 방금 만들어진 노드를 헤드 노드 로 설정
        return
    if head.data[0] > info[0] : # 만약에 헤드노드의 이름이  새로 추가할 이름보다 크면
        node.link = head
        head = node
        return

    current = head
    current.link = node
# 3. 노드 출력 함수 구현
def node_print( ) :
    current = head
    print( current.data , end = ' ')
    while current.link !=None :
        current = current.link
        print( current.data , end = ' ')
    print()

# 전역변수
head = None     # 가장 앞에 있는 노드
current = None

# 메인 코드 실행
if __name__ == "__main__" :
    while True :
        name = input("회원명 : ")
        if name =="" or name == None : #만약에 입력받은 데이터 없으면
            print("정확한 회원명을 입력해주세요!")
            continue
        phone = input("연락처 : ")
        add_node( ( name , phone)  )
        node_print()
