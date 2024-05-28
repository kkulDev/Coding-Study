"""
개발자 kkulDev는 코딩공부에 열중한 나머지 어느 날 모든것이 알고리즘으로 보이기 시작했습니다.
본인이 하던 게임에도 알고리즘이 보이자 직접 구현해보기로 마음먹습니다.

해당 모바일 게임은 본인 진영에 있는 N개의 훈련소에서 여러 종류의 병사를 생산하여 병력을 조직하고 상대 진영을 약탈하는 게임입니다.
약탈 이후 소모된 병사들은 "재훈련" 버튼으로 N개의 훈련소에 최대한 빠르게 생산할 수 있도록 분배합니다.
병력은 어려 종류의 병사들 다수로 구성되어 있으며 병사 종류별로 생산시간은 서로 다릅니다.
N개의 훈련소는 분배된 병력을 동시에 생산하며 모든 병력이 생산 완료되면 "훈련완료"로 판단합니다.
주어진 병력을 "재훈련" 시켰을 때 "훈련완료"까지 걸리는 "최단시간"을 출력합니다.

훈련소 N개, 병사의 종류 M개, 각 병사의 생산시간 Time, 각 병사의 수 Unit 이 순서대로 주어집니다.

예를들어 훈련소 10개, 병사의 종류 5개, 각 병사의 생산시간 [10 15 20 25 30], 각 병사의 수 [3 2 1 0 1] 일 경우
각 훈련소의 병사 생산시간은 [10 10 10 15 15 20 30 0 0 0] 이며 "훈련완료" 까지 30초가 소모됩니다.
만약 훈련소가 3개 일 경우 [35 35 40] 또는 [30 40 40]이 제일 효율적이며 "훈련완료" 까지 40초가 소모됩니다.


<조건>
2 <= N <= 100
1 <= M = Time = Unit <= 10000
1 <= Time[n](초) <= 10000    # 오름차순 정렬, 각 요소에 중복값은 입력되지 않습니다.
0 <= Unit[n] <= 10000

ex)
10  # N
10  # M
10 20 30 40 50 60 70 80 90 100   # Time
10 9 8 7 6 5 4 3 2 1   # Unit

"최단시간"은 초 단위로 출력합니다.

"""

class Training_Zone:
    def __init__(self, N, Time):
        self.Zone = N
        self.unit_Time = Time

    def TrainingAgain(self, M, Units):
        Training_Zone_Time = []
        Training_Time_Sum = 0
        Unit_Sum = 0
        count = 0
        for i in range(M):
            Unit_Sum += Units[i]
            Training_Time_Sum += self.unit_Time[i] * Units[i]
        Training_Time_Ave = Training_Time_Sum//self.Zone
        end = M-1
        front = 0
        while Unit_Sum:
            if count == self.Zone:
                Training_Zone_Time.sort()
                index = 0
                while True:
                    if front > end:
                        break
                    if Units[end]:
                        Training_Zone_Time[index%self.Zone] += self.unit_Time[end]
                        Units[end] -= 1
                        index += 1
                    else:
                        end -= 1
                break

            time_Sum = 0
            unit_Sum = 0
            remain_Time = 0

            while True:
                if front > end:
                    break
                if Units[end]:
                    temp = self.unit_Time[end] * Units[end]
                    if time_Sum + temp >= Training_Time_Ave:
                        use_Unit = (Training_Time_Ave - time_Sum) // self.unit_Time[end]
                        time_Sum += use_Unit * self.unit_Time[end]
                        Units[end] -= use_Unit
                        Unit_Sum -= use_Unit
                        break
                    time_Sum += temp
                    Unit_Sum -= Units[end]
                    Units[end] = 0
                end -= 1
            while True:
                if front > end:
                    break
                if Units[front]:
                    temp = self.unit_Time[front] * Units[front]
                    if time_Sum + temp >= Training_Time_Ave:
                        use_Unit = (Training_Time_Ave - time_Sum) // self.unit_Time[front]
                        remain_Time = (Training_Time_Ave - time_Sum) % self.unit_Time[front]
                        if remain_Time > self.unit_Time[front]-remain_Time:
                            use_Unit += 1
                        time_Sum += use_Unit * self.unit_Time[front]
                        Units[front] -= use_Unit
                        Unit_Sum -= use_Unit
                        break
                    time_Sum += temp
                    unit_Sum += Units[front]
                    Unit_Sum -= Units[front]
                    Units[front] = 0
                front += 1

            Training_Zone_Time.append(time_Sum)
            count += 1
        Training_Zone_Time.sort(reverse=True)
        print(Training_Zone_Time)
        return Training_Zone_Time[0]
    
# N = int(input())
# M = int(input())
# Time = list(map(int, input().split()))
# Unit = list(map(int, input().split()))

# 예시
N = 3
M = 5
Time = [10, 15, 20, 25, 30]
Unit = [3, 2, 1, 0, 1]

Tz1 = Training_Zone(N, Time)
print(Tz1.TrainingAgain(M, Unit))