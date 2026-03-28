n = int(input())
nums = map(int , input().split())
if all( x >= 0 for x in nums):
    print("Yes")
else:
    print("No")