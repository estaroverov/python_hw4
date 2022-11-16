import math

print(math.pi)
def AccuracyCalc(number, accuracy, accuracyList=[10**(-1*i) for i in range(1,11)]):
    counter = 0
    if accuracy in accuracyList:
        while accuracy<1:
            accuracy*=10
            counter+=1
    return round(number,counter)

print(AccuracyCalc(math.pi,0.001))
