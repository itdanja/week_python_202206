
# 최단 거리 찾기 [ 그래프 구현 ]
    # 조건 : 춘천 , 서울 , 속초 , 대전 , 광주 , 부산
    # 조건 : 지역 이동간 걸리는 시간 [ 임의 ]

# 1. 그래프 클래스 선언 [2차원 리스트를 이용한 그래프 구현 ]
class Graph() :
    def __init__(self , size):
        self.SIZE = size
        self.Graph = [ [0 for _ in range(size)] for _ in range(size) ]
# 2. 전역변수
G1 = None
Locationlist = [ "춘천" , "서울" , "속초" , "대전" , "광주" , "부산" ]
춘천 , 서울 , 속초 , 대전 , 광주 , 부산 = 0 ,1 ,2 ,3 ,4 ,5

# 3. 실행
Locationsize = len( Locationlist )
G1 = Graph( Locationsize )
# 지역 이동간 걸리는 시간 [ 임의 설정 ]
G1.Graph[춘천][서울] = 10;  G1.Graph[춘천][속초] = 15
G1.Graph[서울][춘천] = 10;  G1.Graph[서울][속초] = 40; G1.Graph[서울][대전] = 11; G1.Graph[서울][광주] = 50
G1.Graph[속초][춘천] = 15;  G1.Graph[속초][서울] = 40; G1.Graph[속초][대전] = 12
G1.Graph[대전][서울] = 11;  G1.Graph[대전][속초] = 12; G1.Graph[대전][광주] = 20; G1.Graph[대전][부산] = 30
G1.Graph[광주][서울] = 50;  G1.Graph[광주][대전] = 20; G1.Graph[대전][광주] = 25
G1.Graph[부산][대전] = 30;  G1.Graph[부산][광주] = 25









