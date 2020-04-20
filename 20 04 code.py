#Code 20 04
#This is a great code for the assignment for the assessment of "5", which we threw a teacher on computer science. The code was made by HeadNead.
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
if a > 0 and a // 10 < 10 and a // 10 > 0 and a % 10 == 5:
    q = 1
else: q = 0
if b > 0 and b // 10 < 10 and b // 10 > 0 and b %10 == 5:
    m = 1
else: m = 0
if c>0 and c//10<10 and c//10>0 and c % 10 == 5:
    l = 1
else: l = 0
if d > 0 and d // 10 < 10 and d // 10 > 0 and d % 10 == 5:
    o = 1
else:
    o = 0
if e > 0 and e // 10 < 10 and e // 10 > 0 and e % 10 == 5:
    i = 1
else:
    i = 0
n = i + o + l + m + q
print('Natural double-digit numbers ending in 5: ', n, '/n')
print('Other numbers (unnatural, unambiguous, and not ending in 5'): ', 5-n)
