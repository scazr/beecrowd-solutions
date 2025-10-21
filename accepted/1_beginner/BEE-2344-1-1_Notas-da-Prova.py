N = int(input())

grade = None
if         N ==  0: grade = "E"
elif 1  <= N <= 35: grade = "D"
elif 36 <= N <= 60: grade = "C"
elif 61 <= N <= 85: grade = "B"
else: grade = "A"

print(grade)
