name = []
score = []
i = 0
sum = 0
avg = 0
n = int(input("input number student is "))
while i < n:
    name.append(str(input("Input name[%d] =  "%i)))
    score.append(float(input("Input scoer[%d] =  "%i)))
    while score[i] < 0 or score[i] > 100:
        name.append(str(input("Input name[%d] =  "%i)))
        score[i] = (float(input("Input scoer[%d] =  "%i)))
    i = i + 1
min = score[0]
max = score[0]
namemax = name[0]
namemin = name[0]
i = 0
while i < n :
    if score[i] > max :
        max = score[i]
        namemax = name[i]
    if score[i] < min :
        min = score[i]
        namemin = name[i]
    sum = sum + score[i]
    i = i + 1
avg = sum / n
print("max is : %.2f at name is %s "%(max,namemax))
print("min is : %.2f at name is %s  "%(min,namemin))
print("avg is %.2f "%avg)
