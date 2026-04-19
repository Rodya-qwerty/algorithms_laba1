import random
import time


def in_mass(mass:list, search:int)->bool:
    """ Проверка, есть ли элемент в масиве 
        выполлянется за O(n) """
    if len(mass) == 0:
        return False
    
    for i in mass:
        if i == search:
            return True
    return False


def second_max(mass:list)->int:
    """Нахождение воторого максимального эл. в масиве
        выполняется за O(n) (Два форика => O(2n) => O(n))"""
    if len(mass)<2 or len(set(mass)) == 1: 
        return False
    
    max1 = mass[0]
    for i in range(1,len(mass)):
        if mass[i] > max1:
            max1 = mass[i]

    i = 0
    while (mass[i] == max1):
        i+=1
    max2 = mass[i]
    
    for i in range(0,len(mass)):
        if mass[i] > max2 and mass[i] < max1:
            max2 = mass[i]
    return max2


def bin_search(mass:list, search:int)->bool:
    """Бинарный поиск в масиве, реализовал рекурсивно, что наверно не лучшая стратегия, 
    но хотелось потренироваться. Выполняется за O(logn)"""
    r = len(mass)-1
    l = 0
    if(len(mass) == 0): return False
    elif (mass[(r+l)//2] == search): return True
    elif (mass[(r+l)//2] > search): return bin_search (mass[l:(r+l)//2], search)
    elif (mass[(r+l)//2] < search): return bin_search (mass[(l+r)//2+1:r+1], search)

def create_table(n:int)->list:
    """Создание 'матрицы' квадратов. Выполняется за O(n^2)"""
    mass = []
    for i in range (1,n+1):
        temp = []
        for j in range(1,n+1):
            temp.append(i*j)
        mass.append(temp)
    return mass

def babl_sort(mass:list)->list:
    """ Бабл сорт, сложность O(n^2) """
    for i in range(0,len(mass)-1):
        for j in range(len(mass) -1 - i):
            if mass[j] >  mass[j+1]:
                temp = mass[j]
                mass[j] = mass[j+1]
                mass[j+1] = temp 
    return mass

def Quick_sort(mass:list)->list:
    """ Быстрая сортировка, сложность O(nlogn) """
    if len(mass) <= 1: 
        return mass
    piv = mass[len(mass)//2]
    left =  [i for i in mass if i < piv ]
    pivot = [i for i in mass if i == piv]
    right = [i for i in mass if i > piv ]
    return Quick_sort(left) + pivot + Quick_sort(right)


def generate_array(n):
    """Генерация случайных чисел в масиве"""
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr


def measure_time(func, data):
    """Функция для замера времени"""
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start



size = [10**2, 10**3, 5*10**3, 10**4, 5*10**4]
for n in size:
    print(f"Кол-во элементов в массиве {n}:")
    mass = generate_array(n)
    print(f"Бабал сорт: {measure_time(babl_sort, mass):.5f}")
    print(f"Быстрая сортировка: { measure_time(Quick_sort, mass):.5f}")
    print("-"*20)
