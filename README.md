Функции и их сложность

Линейный поиск (in\_mass)

```python

def in\_mass(mass: list, search: int) -> bool:

&#x20;   if len(mass) == 0:

&#x20;       return False

&#x20;   for i in mass:

&#x20;       if i == search:

&#x20;           return True

&#x20;   return False```

Время: O(n) – линейный проход по массиву.

Память: O(1) – не использует дополнительную память (кроме входных данных).



Поиск второго максимума (second\_max)

```python

def second\_max(mass: list) -> int:

&#x20;   if len(mass) < 2 or len(set(mass)) == 1:

&#x20;       return False

&#x20;   max1 = mass\[0]

&#x20;   for i in range(1, len(mass)):

&#x20;       if mass\[i] > max1:

&#x20;           max1 = mass\[i]

&#x20;   i = 0

&#x20;   while mass\[i] == max1:

&#x20;       i += 1

&#x20;   max2 = mass\[i]

&#x20;   for i in range(0, len(mass)):

&#x20;       if mass\[i] > max2 and mass\[i] < max1:

&#x20;           max2 = mass\[i]

&#x20;   return max2```

Время: O(n) – два прохода по массиву.

Память: O(1) – используются только счётчики.



Бинарный поиск (bin\_search)

```python

def bin\_search(mass: list, search: int) -> bool:

&#x20;   if len(mass) == 0:

&#x20;       return False

&#x20;   r = len(mass) - 1

&#x20;   l = 0

&#x20;   if mass\[(r + l) // 2] == search:

&#x20;       return True

&#x20;   elif mass\[(r + l) // 2] > search:

&#x20;       return bin\_search(mass\[l:(r + l) // 2], search)

&#x20;   elif mass\[(r + l) // 2] < search:

&#x20;       return bin\_search(mass\[(l + r) // 2 + 1:r + 1], search)

&#x20;   return False```

Время: O(logn) 

Память: O(n log n) в худшем случае (пиковая память из-за хранения срезов в рекурсии).



Построение таблицы умножения (create\_table)

python

```def create\_table(n: int) -> list:

&#x20;   mass = \[]

&#x20;   for i in range(1, n + 1):

&#x20;       temp = \[]

&#x20;       for j in range(1, n + 1):

&#x20;           temp.append(i \* j)

&#x20;       mass.append(temp)

&#x20;   return mass```

Время: O(n²) – вложенные циклы.

Память: O(n²) – создаётся матрица размером n×n.



Пузырьковая сортировка (babl\_sort)

python

```

def babl\_sort(mass: list) -> list:

&#x20;   for i in range(0, len(mass) - 1):

&#x20;       for j in range(len(mass) - 1 - i):

&#x20;           if mass\[j] > mass\[j + 1]:

&#x20;               temp = mass\[j]

&#x20;               mass\[j] = mass\[j + 1]

&#x20;               mass\[j + 1] = temp

&#x20;   return mass```

Время: O(n²) – классическая пузырьковая сортировка.

Память: O(1) – сортировка на месте.



Быстрая сортировка (Quick\_sort)

```python

def Quick\_sort(mass: list) -> list:

&#x20;   if len(mass) <= 1:

&#x20;       return mass

&#x20;   piv = mass\[len(mass) // 2]

&#x20;   left = \[i for i in mass if i < piv]

&#x20;   pivot = \[i for i in mass if i == piv]

&#x20;   right = \[i for i in mass if i > piv]

&#x20;   return Quick\_sort(left) + pivot + Quick\_sort(right)```

Время: O(n log n) в среднем, O(n²) в худшем случае 

Память: O(n log n)



\## Результаты замеров



\### Линейный поиск (`in\_mass`)



| n      | Время (с) | Память (КБ) |

|--------|-----------|-------------|

| 100    | 0.00004   | 0.05        |

| 1000   | 0.00003   | 0.05        |

| 5000   | 0.00012   | 0.05        |

| 10000  | 0.00006   | 0.05        |



\### Поиск второго максимума (`second\_max`)



| n      | Время (с) | Память (КБ) |

|--------|-----------|-------------|

| 100    | 0.00004   | 10.26       |

| 1000   | 0.00103   | 40.26       |

| 5000   | 0.00673   | 160.26      |

| 10000  | 0.01771   | 640.26      |



\### Бинарный поиск (`bin\_search`) – массив предварительно сортируется



| n      | Время (с) | Память (КБ) |

|--------|-----------|-------------|

| 100    | 0.00005   | 0.72        |

| 1000   | 0.00005   | 7.85        |

| 5000   | 0.00008   | 39.10       |

| 10000  | 0.00035   | 78.45       |



\### Построение таблицы умножения (`create\_table`)



| n      | Время (с) | Память (КБ)   |

|--------|-----------|---------------|

| 100    | 0.00634   | 368.23        |

| 1000   | 1.18221   | 39857.02      |

| 5000   | 26.21039  | 985733.02     |

| 10000  | 129.57169 | 3956829.99    |



\### Сравнение сортировок



| n     | Алгоритм       | Время (с) | Память (КБ) |

|-------|----------------|-----------|-------------|

| 100   | Пузырьковая    | 0.01379   | 0.11        |

| 100   | Быстрая        | 0.00156   | 4.66        |

| 1000  | Пузырьковая    | 0.50996   | 0.25        |

| 1000  | Быстрая        | 0.00812   | 30.76       |

| 5000  | Пузырьковая    | 16.01938  | 0.25        |

| 5000  | Быстрая        | 0.04010   | 205.34      |

| 10000 | Пузырьковая    | 76.88650  | 0.25        |

| 10000 | Быстрая        | 0.08236   | 339.19      |

