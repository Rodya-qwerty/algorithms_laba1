# Музыкальный плейлист на связных списках (Python и C++)

Данный проект реализует музыкальный плейлист с использованием:
- **Python** – односвязный список, сохранение/загрузка CSV, режимы повтора, статистика, поиск.
- **C++** – двусвязный список, перемешивание через массив указателей, сохранение в текстовый файл.

---

## 1. Python версия (`Laba2.py`)

### Класс `Node` – узел односвязного списка

```python
class Node:
    def __init__(self, name=None, time=None, genre=None, rating=None):
        self.name = name      # название трека
        self.time = time      # длительность в секундах
        self.genre = genre    # жанр
        self.rating = rating  # рейтинг (1-5)
        self.next = None      # указатель на следующий узел
```
Назначение: хранит данные одного трека и ссылку на следующий элемент.

Класс Music – управление плейлистом

__init__ – конструктор
```python
def __init__(self, name=None, time=None, genre=None, rating=None):
    self.size = 0
    self.head = None
    self.repeat_mode = "none"
    self.current_track = None
```
Что делает: инициализирует пустой плейлист.
Атрибуты: size (0), head (None), repeat_mode ("none"/"one"/"all"), current_track (текущий трек).

append_to_end – добавление в конец
python
def append_to_end(self, name=None, time=None, genre=None, rating=None):
    new_node = Node(name, time, genre, rating)
    if self.head is None:
        self.head = new_node
    else:
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    self.size += 1
Что делает: добавляет трек в конец (O(n)).

prepend – добавление в начало
python
def prepend(self, name=None, time=None, genre=None, rating=None):
    new_node = Node(name, time, genre, rating)
    new_node.next = self.head
    self.head = new_node
    self.size += 1
Что делает: добавляет трек в начало (O(1)).

dell – удаление трека
python
def dell(self, del_name):
    dell = self.head
    next_del = (self.head).next
    for i in range(self.size):
        if self.head.name == del_name:
            self.head = next_del
            self.size -= 1
            break
        elif next_del.name == del_name:
            dell.next = next_del.next
            self.size -= 1
            break
        else:
            dell = next_del
            next_del = next_del.next
Что делает: удаляет первый узел с заданным именем (O(n)).

get_set – вывод списка
python
def get_set(self):
    if self.head is None:
        print("Список пуст")
        return
    print("--------------")
    p = self.head
    index = 0
    while p is not None:  
        print(f"Узел №{index+1}:", p.name, p.time, p.genre, p.rating)
        p = p.next
        index += 1
    print("--------------")
Что делает: выводит все треки в консоль (O(n)).

shak – перемешивание
python
def shak(self):
    if self.size <= 1:
        return
    for _ in range(randint(self.size, self.size * 2)):
        pos = randint(0, self.size - 1)
        if pos == 0:
            node_to_move = self.head
            self.head = self.head.next
            current = self.head
            while current.next:
                current = current.next
            current.next = node_to_move
            node_to_move.next = None
        else:
            prev = self.head
            for i in range(pos - 1):
                prev = prev.next
            node_to_move = prev.next
            prev.next = node_to_move.next
            current = self.head
            while current.next:
                current = current.next
            current.next = node_to_move
            node_to_move.next = None
Что делает: случайно перемешивает плейлист (O(n²)).

play_all – воспроизведение
python
def play_all(self):
    if self.head is None:
        print("Плейлист пуст")
        return
    self.current_track = self.head
    while self.current_track is not None:
        print(f"Сейчас играет: {self.current_track.name}")
        time.sleep(0.5)  
        if self.repeat_mode == "one":
            continue
        else:
            self.current_track = self.current_track.next
        if self.current_track is None and self.repeat_mode == "all":
            self.current_track = self.head
            print("--- Плейлист повторяется ---")
Что делает: имитирует проигрывание с учётом режима повтора.

set_repeat_mode – режим повтора
python
def set_repeat_mode(self, mode):
    if mode in ["none", "one", "all"]:
        self.repeat_mode = mode
        print(f"Режим повтора: {mode}")
    else:
        print("Неверный режим. Используйте: 'none', 'one', 'all'")
Что делает: устанавливает режим повтора.

safe_in_file – сохранение в CSV
python
def safe_in_file(self):
    if self.head is None:
        print("Нечего сохранять в файл")
        return 
    with open("music_save.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "time", "genre", "rating"])
        wr = self.head
        while wr is not None:
            writer.writerow([wr.name, wr.time, wr.genre, wr.rating])
            wr = wr.next
        print("Плейлист записан")
Что делает: сохраняет плейлист в music_save.csv.

see_table – просмотр CSV
python
def see_table(self):
    table = pandas.read_csv('music_save.csv')
    print(table)
Что делает: выводит содержимое CSV в виде таблицы.

read_csv – загрузка из CSV
python
def read_csv(self):
    file = pandas.read_csv("music_save.csv")
    print("Прочитанные данные с файла и добавленные в список:")
    print("-------------------------")
    for i in range(file.shape[0]):
        print('name = ', file.loc[i, file.columns]['name'])
        print('time = ', file.loc[i, file.columns]['time'])
        print('genre = ', file.loc[i, file.columns]['genre'])
        print('rating = ', file.loc[i, file.columns]['rating'])
        self.append_to_end(
            file.loc[i, file.columns]['name'],
            file.loc[i, file.columns]['time'],
            file.loc[i, file.columns]['genre'],
            file.loc[i, file.columns]['rating']
        )
        print("-------------------------")
Что делает: загружает треки из CSV и добавляет в список.

report – статистика
python
def report(self):
    all_time = 0 
    sum_rating = 0
    temp = self.head
    for i in range(self.size):
        all_time += temp.time
        sum_rating += temp.rating
        temp = temp.next
    print("Кол-во треков: ", self.size)
    print("Общее время: ", all_time)
    print("Медианный рейтинг: ", sum_rating // self.size)
Что делает: выводит статистику (количество, общее время, средний рейтинг).

search_genre – поиск по жанру
python
def search_genre(self):
    search = input("Введите жанр, который вы хотите найти: ")
    table = pandas.read_csv('music_save.csv')
    print(table.loc[ table.loc[:,'genre'] == search ])
Что делает: ищет треки по жанру в CSV.

search_reating – поиск по рейтингу
python
def search_reating(self):
    search = input("Введите рейтинг, не ниже которого должен быть поиск: ")
    table = pandas.read_csv('music_save.csv')
    print(table.loc[ table.loc[:,'rating'] >= search ])
Что делает: ищет треки с рейтингом ≥ заданного.

2. C++ версия (Laba.cpp)
Класс Node – узел двусвязного списка
cpp
class Node {
public:
    string name {"None"};
    int time {0};
    string genre {"None"};
    int rating {0};
    Node* next {nullptr};
    Node* previous {nullptr};

    Node(string n = "None", int t = 0, string g = "None", int r = 0) 
        : name(n), time(t), genre(g), rating(r), next(nullptr) {}
};
Назначение: хранит данные трека, указатели на следующий и предыдущий узлы.

Класс Music – управление плейлистом
Music и ~Music – конструктор и деструктор
cpp
Music() : head(nullptr), size(0), end{nullptr} {}
~Music(){ 
    Node* current = head;
    while (current != nullptr){
        Node* next = current->next;
        delete current;
        current = next;
    }
}
Что делает: конструктор инициализирует пустой список; деструктор очищает память.

append_to_end – добавление в конец
cpp
void append_to_end(string name, int time, string genre, int rating){
    Node* new_node = new Node(name, time, genre, rating);
    if (this->head == nullptr){
        this->head = new_node;
    }
    else{
        Node* current = this->head;
        while (current->next != nullptr){
            current = current->next;
        }
        new_node->previous = current; 
        current->next = new_node;
    }
    this->end = new_node;
    this->size++;
}
Что делает: добавляет трек в конец двусвязного списка (O(n)).

append_to_head – добавление в начало
cpp
void append_to_head(string name, int time, string genre, int rating){
    Node* new_node = new Node(name, time, genre, rating);
    if (size == 0){
        this->head = new_node;
        this->end = new_node;
    }
    else{
        new_node->next = this->head;
        (this->head)->previous = new_node;
        this->head = new_node;
    }
    this->size++;
}
Что делает: добавляет трек в начало (O(1)).

del – удаление трека
cpp
void del(string name){
    if (head == nullptr){
        cout << "list is empty" << endl;
        return;
    }
    if (head->name == name){
        Node* temp = head;
        head = head->next;
        if (head != nullptr){
            head->previous = nullptr;
        } else {
            end = nullptr;
        }
        delete temp;
        size--;
        return;
    }
    Node* current = head->next;
    while (current != nullptr){
        if (current->name == name){
            current->previous->next = current->next;
            if (current->next != nullptr){
                current->next->previous = current->previous;
            } else {
                end = current->previous;
            }
            delete current;
            size--;
            return;
        }
        current = current->next;
    }
    cout << "Элемент не найден" << endl;
}
Что делает: удаляет первый узел с заданным именем (O(n)).

shuffle – перемешивание
cpp
void shuffle(){
    if (size <= 1) return;
    Node** mass = new Node*[size];
    Node* temp = this->head;
    for (int i = 0; i < size; i++){
        mass[i] = temp;
        temp = temp->next;
    }
    for (int i = size - 1; i > 0; i--){
        int j = rand() % (i + 1);
        Node* swap = mass[i];
        mass[i] = mass[j];
        mass[j] = swap;
    }
    for (int i = 0; i < size; i++){
        mass[i]->next = (i < size - 1) ? mass[i + 1] : nullptr;
        mass[i]->previous = (i > 0) ? mass[i - 1] : nullptr;
    }
    this->head = mass[0];
    this->end = mass[size - 1];
    delete[] mass;
}
Что делает: перемешивает список (O(n) времени, O(n) памяти).

save_to_file – сохранение в файл
cpp
void save_to_file(){
    FILE* file = fopen("table.txt", "w");
    if (file == NULL){
        cout << "Can`t open file" << endl;
        return;
    }
    Node* temp = this->head;
    while (temp != nullptr){
        fprintf(file, "%s %d %s %d\n", temp->name.c_str(), temp->time, temp->genre.c_str(), temp->rating);
        temp = temp->next;
    }
    fclose(file);
}
Что делает: сохраняет плейлист в текстовый файл.

print – вывод списка
cpp
void print(){
    Node* ob = this->head;
    for (int i = 0; i < this->size; i++){
        if (i == 0)
            cout << "Track " << i+1 << ": " << ob->name << " (no previous)" << endl;
        else
            cout << "Track " << i+1 << ": " << ob->name << ", previous: " << ob->previous->name << endl;
        ob = ob->next;
    }
}
Что делает: выводит треки с информацией о предыдущем элементе.

Пример работы
Python
text
Исходный плейлист:
--------------
Узел №1: Shape of You 233 Pop 5
Узел №2: Bohemian Rhapsody 354 Rock 5
--------------

--- Воспроизведение ---
Сейчас играет: Shape of You
Сейчас играет: Bohemian Rhapsody

--- Статистика ---
Кол-во треков: 2
Общее время: 587
Медианный рейтинг: 5
C++
text
Track 1: Bohemian Rhapsody (no previous)
Track 2: Imagine, previous: Bohemian Rhapsody
Track 3: Stairway to Heaven, previous: Imagine

Playlist is shuffled!
Track 1: Stairway to Heaven (no previous)
Track 2: Bohemian Rhapsody, previous: Stairway to Heaven

Delete: Imagine
Track 1: Stairway to Heaven (no previous)
Track 2: Bohemian Rhapsody, previous: Stairway to Heaven
