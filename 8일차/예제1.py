"""
    동적 계획법 [ DP : 다이나믹 프로그래밍 ]
        1. 하나의 문제를 여러 개의 작은 단위로 나누어서 결과 찾기
            - 기억 하며 풀기
        2. 효율적으로 문제 해결 가능
"""
# 예 ) 피보나치 수열  VS 동적 계획법

def dp_fibo( n ) :
    global count_dp
    memo = [ 1 , 1 ]    # 계산된 수열 저장하는 공간
    if n < 2 :
        return memo[n]
    else:
        for i in range( 2 , n+1 ) :
            memo.append( memo[i-1] + memo[i-2] )
            count_dp += 1
        return memo[n]

def requ_fibo( n ) :
    global count_requ
    count_requ +=1
    if n < 2 :
        return 1
    else:
        return requ_fibo(n-1) + requ_fibo(n-2)      # 피보나치 수열 공식

#전역변수
count_requ = 0      # 재귀방식 피보나치 반복횟수
count_dp = 0       # DP방식 피보나치 반복횟수

print(" 30번째 피보나치 수열 ")
#
res = requ_fibo(30)
print(" 재귀를 이용한 피보나치 : ", res ,  "반복수 : " , count_requ )

#
res = dp_fibo(30)
print(" DP를 이용한 피보나치 : " , res ,"반복수 : ",count_dp)









