import sys
input = lambda: sys.stdin.readline().rstrip()


n, s, r = map(int, input().split())
temp = []
kayac = [0 for _ in range(n+2)]	#대회에 참가한 팀의 갯수만큼 0으로 초기화. 인덱스처리 위해 앞뒤 0으로 패딩
temp = list(map(int, input().split()))
for i in range(s):	#카약 망가진 팀은 -1
    kayac[temp[i]] -= 1	
temp = list(map(int, input().split()))
for i in range(r):	#카약 여분 있는 팀은 +1
    kayac[temp[i]] += 1
for i in range(1, len(kayac)):	#인덱스1부터 시작, kayac 배열 맨뒤 0패딩 있으므로 마지막팀까지 처리 가능
    if kayac[i] == 1:	#여분이 있다면
        if kayac[i-1] == -1:	#이전 팀부터 빌려준다(빨리 빌려서 먼저 경기에 나가야 하므로)
            kayac[i-1] += 1
            kayac[i] -= 1
        #이전 팀에서 추가 카약이 필요없다면 다음 팀을 확인
        elif kayac[i+1] == -1:	#다음 팀의 카약이 없다면 우리 팀의 카약을 빌려준다.
            kayac[i+1] += 1
            kayac[i] -= 1	
print(kayac.count(-1))	#마지막까지 카약을 못 빌린 팀의 갯수를 출력