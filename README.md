## Описание класса

### Node
Узел связного списка, хранящий информацию о треке.

**Атрибуты:**
- `name` - название трека
- `time` - длительность в секундах
- `genre` - жанр
- `rating` - рейтинг
- `next` - ссылка на следующий узел

---

### Music
Основной класс для управления плейлистом.

**Атрибуты:**
- `size` - количество треков
- `head` - первый элемент списка
- `repeat_mode` - режим повтора (`"none"`, `"one"`, `"all"`)
- `current_track` - текущий воспроизводимый трек

**Методы:**

#### `append_to_end(name, time, genre, rating)`
Добавляет трек в конец плейлиста.
- Сложность: O(n)
- Пример: `my_playlist.append_to_end("Imagine", 183, "Pop", 5)`

#### `prepend(name, time, genre, rating)`
Добавляет трек в начало плейлиста.
- Сложность: O(1)
- Пример: `my_playlist.prepend("Yesterday", 125, "Rock", 4)`

#### `dell(del_name)`
Удаляет первый трек с указанным названием.
- Пример: `my_playlist.dell("Imagine")`

#### `get_set()`
Выводит все треки плейлиста в консоль с нумерацией.

#### `shak()`
Перемешивает плейлист случайным образом.

#### `play_all()`
Воспроизводит весь плейлист с учётом режима повтора:
- `"none"` - однократное воспроизведение
- `"one"` - бесконечный повтор текущего трека
- `"all"` - зацикленное воспроизведение всего плейлиста

#### `set_repeat_mode(mode)`
Устанавливает режим повтора.
- Параметры: `"none"`, `"one"`, `"all"`

#### `safe_in_file()`
Сохраняет плейлист в CSV файл (`Laba2/music_save.csv`).

#### `see_table()`
Читает сохранённый CSV файл и выводит таблицу в консоль.

---

## Пример использования

```python
my_playlist = Music()

# Добавление треков
my_playlist.append_to_end("Bohemian Rhapsody", 354, "Rock", 5)
my_playlist.append_to_end("Imagine", 183, "Pop", 5)
my_playlist.prepend("Billie Jean", 294, "Pop", 4)

# Воспроизведение
my_playlist.set_repeat_mode("all")
my_playlist.play_all()

# Сохранение и просмотр
my_playlist.safe_in_file()
my_playlist.see_table()
```

# Вывод в консоль
```
Сейчас играет: Bohemian Rhapsody
Сейчас играет: Imagine
Сейчас играет: Stairway to Heaven
Плейлист записан
                   name  time genre  rating
0    Bohemian Rhapsody   354  Rock       5
1              Imagine   183   Pop       5
2  Stairway to Heaven   482  Rock       5
```