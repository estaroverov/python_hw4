import math
import random

# Вычислить число c заданной точностью d
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

# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
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

#Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
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


f = open('polynom.txt', 'w')
f2 = open('polynom2.txt', 'w')

#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
def SetPolynom(k):
    i = 0
    polynomStr = ""
    while k >= i:
        c = str(random.randint(0, 100))
        polynomStr += c+"\n"
        k -= 1
    return polynomStr


f.write(SetPolynom(2))
f2.write(SetPolynom(2))
f.close
f2.close


f = open("polynom.txt", "r")
f2 = open("polynom2.txt", "r")
polynom1 = f.read()
polynom2 = f2.read()
f.close
f2.close

#Даны два файла, 
# в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
def PolynomSum(polynom1, polynom2):
    i = 0
    totalPoly = []
    totalStr = ""
    sum = 0
    polynom1 = polynom1.split("\n")
    polynom2 = polynom2.split("\n")
    length = len(polynom1)
    while i < length:
        if polynom2[i] != '' and polynom1[i] != '':
            sum = int(polynom1[i]) + int(polynom2[i])
        else:
            i += 1
            continue
        totalPoly.append(sum)
        i += 1
    for i in totalPoly:
        totalStr += str(i) + "\n"
    return totalStr


f = open("total_polynom.txt", "w")
f.write(PolynomSum(polynom1, polynom2))
f.close
