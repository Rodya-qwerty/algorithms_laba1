#include <iostream> 
#include <locale.h>
#include <string>
#include <cstdlib> 
#include <ctime>
#include <stdio.h>

using namespace std;

class Node{
    
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

class Music {
    private:
        Node* head;
        Node* end;
        int size;

    public:
        Music() : head(nullptr), size(0), end{nullptr} {}

        ~Music(){ 
            Node* current = head;
            while (current != nullptr){
                Node* next = current->next;
                delete current;
                current = next;
            }
        }

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
                cout << "Delete: " << name << endl;
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
                    cout << "Delete: " << name << endl;
                    return;
                }
                current = current->next;
            }
            
            cout << "Элемент '" << name << "' не найден" << endl;
        }

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
            
            cout << "Playlist is shaffle!" << endl;
        }

        void save_to_file(){
            FILE* file = fopen("C:\\Users\\Mi\\Desktop\\code\\data_structures_and_algorithms\\Laba2\\table.txt", "w");
            if (file == NULL){
                cout << "Can`t open file" << endl;
                return ;
            }
            Node* temp = this->head;
            while (temp!=nullptr){
                fprintf(file, "%s %d %s %d\n", temp->name.c_str(), temp->time, temp->genre.c_str(), temp->rating);
                temp = temp->next;
            }
            fclose(file);
        }

        void print(){
            Node* ob = this->head;
            for (int i = 0; i < this->size; ){
                if (i!=0){
                cout << "Object "<<++i << ": " << ob->name << ", previous: "<< (ob->previous)->name << endl; 
                ob = ob->next;
            }
            else{
                cout << "Object "<<++i << ": " << ob->name << ", previous is haven`t" << endl; 
                ob = ob->next;
            }
            }
        }
};

int main(){
    srand(time(nullptr));
    setlocale(LC_ALL, "");
    Music playlist;
    
    playlist.append_to_end("Bohemian Rhapsody", 354, "Rock", 5);
    playlist.append_to_end("Imagine", 183, "Pop", 5);
    playlist.append_to_end("Stairway to Heaven", 482, "Rock", 5);
    
    playlist.print();

    // playlist.save_to_file();
    return 0;
}