n = int(input()) 
words = input().split()
long = max(words , key=len)
print(long)