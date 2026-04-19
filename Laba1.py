import random
import time
import tracemalloc
import sys

def in_mass(mass: list, search: int) -> bool:
    if len(mass) == 0:
        return False
    for i in mass:
        if i == search:
            return True
    return False

def second_max(mass: list) -> int:
    if len(mass) < 2 or len(set(mass)) == 1:
        return False
    max1 = mass[0]
    for i in range(1, len(mass)):
        if mass[i] > max1:
            max1 = mass[i]
    i = 0
    while mass[i] == max1:
        i += 1
    max2 = mass[i]
    for i in range(0, len(mass)):
        if mass[i] > max2 and mass[i] < max1:
            max2 = mass[i]
    return max2

def bin_search(mass: list, search: int) -> bool:
    if len(mass) == 0:
        return False
    r = len(mass) - 1
    l = 0
    if mass[(r + l) // 2] == search:
        return True
    elif mass[(r + l) // 2] > search:
        return bin_search(mass[l:(r + l) // 2], search)
    elif mass[(r + l) // 2] < search:
        return bin_search(mass[(l + r) // 2 + 1:r + 1], search)
    return False

def create_table(n: int) -> list:
    mass = []
    for i in range(1, n + 1):
        temp = []
        for j in range(1, n + 1):
            temp.append(i * j)
        mass.append(temp)
    return mass

def babl_sort(mass: list) -> list:
    for i in range(0, len(mass) - 1):
        for j in range(len(mass) - 1 - i):
            if mass[j] > mass[j + 1]:
                temp = mass[j]
                mass[j] = mass[j + 1]
                mass[j + 1] = temp
    return mass

def Quick_sort(mass: list) -> list:
    if len(mass) <= 1:
        return mass
    piv = mass[len(mass) // 2]
    left = [i for i in mass if i < piv]
    pivot = [i for i in mass if i == piv]
    right = [i for i in mass if i > piv]
    return Quick_sort(left) + pivot + Quick_sort(right)

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time_memory(func, *args):
    tracemalloc.start()
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end - start, peak / 1024

size = [10**2, 10**3, 5*10**3, 10**4, 5*10**4]

print("Поиск в массиве (in_mass):")
for n in size:
    mass = generate_array(n)
    search_val = random.randint(1, 1000)
    t, mem = measure_time_memory(in_mass, mass, search_val)
    print(f"  n={n:6d} | время: {t:.5f} с | память: {mem:.2f} КБ")

print("-" * 50)

print("Нахождение второго максимального (second_max):")
for n in size:
    mass = generate_array(n)
    t, mem = measure_time_memory(second_max, mass)
    print(f"  n={n:6d} | время: {t:.5f} с | память: {mem:.2f} КБ")

print("-" * 50)

print("Бинарный поиск (bin_search) — массив предварительно сортируется:")
for n in size:
    mass = sorted(generate_array(n))
    search_val = random.randint(1, 1000)
    t, mem = measure_time_memory(bin_search, mass, search_val)
    print(f"  n={n:6d} | время: {t:.5f} с | память: {mem:.2f} КБ")

print("-" * 50)

print("Построение таблицы умножения (create_table):")
for n in size:
    t, mem = measure_time_memory(create_table, n)
    print(f"  n={n:6d} | время: {t:.5f} с | память: {mem:.2f} КБ")

print("-" * 50)
print("Сравнение сортировок:")
for n in size:
    mass = generate_array(n)
    print(f"\n  n={n}:")
    
    mass_bubble = mass.copy()
    t_bubble, mem_bubble = measure_time_memory(babl_sort, mass_bubble)
    print(f"    Пузырьковая: время = {t_bubble:.5f} с, память = {mem_bubble:.2f} КБ")
    
    mass_quick = mass.copy()
    t_quick, mem_quick = measure_time_memory(Quick_sort, mass_quick)
    print(f"    Быстрая:     время = {t_quick:.5f} с, память = {mem_quick:.2f} КБ")
    print("  " + "-" * 35)