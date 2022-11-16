import math


def AccuracyCalc(number, accuracy, accuracyList=[10**(-1*i) for i in range(1, 11)]):
    counter = 0
    if accuracy in accuracyList:
        while accuracy < 1:
            accuracy *= 10
            counter += 1
        return round(number, counter)
    else:
        return "No such accuracy"


print(AccuracyCalc(math.pi, 0.01))


def FactorDecompos(number):
    counter = 2
    i = 2
    simple = False
    factorList = []
    while counter <= number:
        if number % counter == 0:
            factorList.append(counter)
            number /= counter
        else:
            while i <= number:
                if number % i == 0 and i < number:
                    simple = False
                elif i == number:
                    simple = True
                i += 1
            if simple == True:
                factorList.append(int(number))
                break
            counter += 1

    return factorList


print(FactorDecompos(1978))

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))


def ListUnique(numbers):
    copy = False
    i = 0
    j = 0
    totalList = []
    while i < len(numbers):
        copy = False
        j = 0
        while j < len(numbers):
            if numbers[i] == numbers[j] and i != j:
                copy = True
                break
            j += 1
        if copy == False:
            totalList.append(numbers[i])
        i += 1
    return totalList


print(ListUnique(numbers))
