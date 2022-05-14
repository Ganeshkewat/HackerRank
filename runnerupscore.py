n = int(input())
arr = map(int, input().split())
list = sorted(list(set(arr)))[-2]

print(list)

