#
# 합계 찾기
# 정수의 List L에서 정수 A가 될 수 있는 두 인덱스 찾기
# 효율성 A 보다 큰값 제거, 중복 제거
#

import itertools

L = [1,2,3,5]
A = 5
for a in itertools.combinations(L,2):
    if a[0] + a[1] == A:
        print(a)

