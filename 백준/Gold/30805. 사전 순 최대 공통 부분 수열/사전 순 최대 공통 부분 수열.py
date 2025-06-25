def sol(arr1, arr2, res = []):
    
    # 두 배열 중 하나라도 비어 있으면 결과 반환
    if (not arr1) or (not arr2):
        return res
    
    # arr1과 arr2에서 각각 가장 큰 값과 그 인덱스를 찾음
    tmp1, tmp2 = max(arr1), max(arr2)
    idx1, idx2 = arr1.index(tmp1), arr2.index(tmp2)

    # 두 값이 같으면 결과에 추가하고 그 이후 부분으로 재귀 호출
    if tmp1 == tmp2:
        res.append(tmp1)
        return sol(arr1[idx1 + 1:], arr2[idx2 + 1:], res)
    # tmp1이 더 크면 arr1에서 제거하고 재귀 호출
    elif tmp1 > tmp2:
        arr1.pop(idx1)
        return sol(arr1, arr2, res)
    # tmp2가 더 크면 arr2에서 제거하고 재귀 호출
    else:
        arr2.pop(idx2)
        return sol(arr1, arr2, res)


n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

# 함수 호출
ans = sol(arr1, arr2)

# 결과 출력
print(len(ans))
if ans:
    print(*ans)