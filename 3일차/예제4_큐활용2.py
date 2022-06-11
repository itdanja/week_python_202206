# 지하철 관제 프로그램
# 차고지 ---> 강남역-----> 역삼역 -----> 선릉역 ---> 삼성역 -> 차고지
# 조건 : 차고지에 차량대기 : 전차A , 전차B , 전차C
def station_print() :
    print( " 현재 전차들의 위치 " , 호선2)
차고지 = [ "전차A" , "전차B" , "전차C" ]
강남역 = [ None , None , None ]
역삼역 = [ None , None , None ]
선릉역 = [ None , None , None ]
삼성역 = [ None , None , None ]
호선2 = [ 차고지 , 강남역 , 역삼역 , 선릉역 , 삼성역 ]   # 2차원 리스트
while True :
    station_print()
    select = int( input( " 출발신호 : 0.차고지 1.강남역 2.역삼역 3.선릉역 4.삼성역 :  ") )
    if select == 1 :
        print(" 차고지에 전차 출발!! ")
        station_print()
    elif select == 2 :
        print(" 강남역에 전차 출발 ")
        station_print()
    elif select == 3 :
        print(" 역삼역에 전차 출발 ")
        station_print()
    elif select == 4 :
        print(" 삼성역에 전차 출발 ")
        station_print()
    else:
        print(" 알수 없는 번호 입니다.")


