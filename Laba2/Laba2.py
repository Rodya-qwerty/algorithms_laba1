from random import randint
import time 
import csv
import pandas 

class Node:
    def __init__(self, name = None, time = None, genre = None, rating = None):

        self.name = name 
        self.time = time
        self.genre = genre
        self.rating = rating 
        self.next = None    



class Music:
    def __init__(self, name = None, time = None, genre = None, rating = None):
        self.name = name 
        self.time = time
        self.genre = genre
        self.rating = rating 
        self.size = 0
        self.head = None
        self.repeat_mode = "none"  # "none", "one", "all"
        self.current_track = None  # текущий играющий трек

    def append_to_end(self, name = None, time = None, genre = None, rating = None):
        """Добавление элемента в конец - сложность O(n)"""
        new_node = Node(name, time, genre, rating)
        if  self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, name=None, time=None, genre=None, rating=None):
        """Добавление в начало"""
        new_node = Node(name, time, genre, rating)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def dell(self, del_name):
        """Удаление из списка первого элемента, совпадающего по имени"""
        dell = self.head
        next_del = (self.head).next
        for i in range(self.size):
            if self.head.name  == del_name:
                self.head = next_del
                self.size -=1
                break
            elif next_del.name == del_name:
                dell.next = next_del.next
                self.size -=1
                break
            else:
                dell = next_del
                next_del = next_del.next
        
    def get_set(self):
        """Вывод всех элементов списка"""
        if self.head is None:
            print("Список пуст")
            return
        
        print("--------------")
        p = self.head
        index = 0
        while p is not None:  
            print(f"Узел №{index+1}:", p.name, p.time, p.genre, p.rating)
            p = p.next
            index+=1
        print("--------------")

    def shak(self):
        """Перемешивание плейлиста"""
        if self.size <= 1:
            return
        
        for _ in range(randint(self.size, self.size * 2)):  #кол-во перемешиваний 

            pos = randint(0, self.size - 1) #Элемент для добавления в конец 
            
            if pos == 0: # Если это первый эл, то кидаем в конец
                node_to_move = self.head
                self.head = self.head.next
                current = self.head

                while current.next:
                    current = current.next
                current.next = node_to_move
                node_to_move.next = None

            else: #
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

    def play_all(self):
        """Воспроизведение всего плейлиста с учётом режима повтора"""
        if self.head is None:
            print("Плейлист пуст")
            return
        
        self.current_track = self.head
        
        while self.current_track is not None:
            print(f"Сейчас играет: {self.current_track.name}")
            time.sleep(0.5)  
            
            if self.repeat_mode == "one":
                # Repeat One - не переходим к следующему, повторяем текущий
                continue
            else:
                self.current_track = self.current_track.next
            
            # Если дошли до конца при Repeat All
            if self.current_track is None and self.repeat_mode == "all":
                self.current_track = self.head
                print("--- Плейлист повторяется ---")
    
    def set_repeat_mode(self, mode):
        """Установка режима повтора: 'none', 'one', 'all'"""
        if mode in ["none", "one", "all"]:
            self.repeat_mode = mode
            print(f"Режим повтора: {mode}")
        else:
            print("Неверный режим. Используйте: 'none', 'one', 'all'")

    def safe_in_file(self):
        if self.head is None:
            print("Нечего сохранять в файл")
            return 

        with open("Laba2\\music_save.csv", "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(["name", "time", "genre", "rating"])
            self.set_repeat_mode('none')
            wr = self.head
            while wr is not None:
                writer.writerow([wr.name, wr.time, wr.genre, wr.rating])
                wr = wr.next
            print("Плейлист записан")
    
    def see_table(self):
        table = pandas.read_csv('Laba2\\music_save.csv')
        print(table)


        


def main():      
    # создание объекта и его заполнение 
    my_playlist = Music()
    my_playlist.append_to_end("Bohemian Rhapsody", 354, "Rock", 5)
    my_playlist.append_to_end("Imagine", 183, "Pop", 5)
    my_playlist.append_to_end("Stairway to Heaven", 482, "Rock", 5)

    # "Проигрыш" ввёденных песен, сохранение в файл и просмотр в таблице 
    my_playlist.play_all()
    my_playlist.safe_in_file()
    my_playlist.see_table()


if __name__ == "__main__":
    main()