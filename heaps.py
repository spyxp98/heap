import heapq
import math 
import random

# Пишем max heap
class Heap:
    
    def __init__(self, data):
        # data - просто список элементов без упорядочивания 
        self.data = data
        # tree_data - breadth-first упорядоченная data
        self.tree_data = []
        # Высота полностью заполненных слоев
        # self.height = math.floor(math.log(len(data), 2))
    
    # По data построить tree_data (плохой алгоритм за n log n)
    def heapify(self):
        self.tree_data.append(self.data[0])
        for i in range(1, len(self.data)):
            self.tree_data.append(self.data[i])
            self.newsift_up()

    # Добавить элемент в конец и устроить просеивание наверх
    def sift_up(self, element):
        self.tree_data.append(element)
        k = len(self.tree_data) - 1
        while self.tree_data[k] > self.tree_data[k//2]:
            self.tree_data[k], self.tree_data[k//2] = self.tree_data[k//2], self.tree_data[k]
            k = k//2 

    # Забрать элемент из вершины и восстановить кучу
    def sift_down(self):
        if len(self.tree_data) == 1:
            return self.tree_data.pop()
        else:
            root = self.tree_data[0]
            self.tree_data[0] = self.tree_data[-1]
            del self.tree_data[-1]
            i = 0
            while 2 * i + 1 < len(self.tree_data):
                left = 2 * i + 1
                right = 2 * i + 2
                temp = left 
                if right < len(self.tree_data) and self.tree_data[left] <= self.tree_data[right]:
                    temp = right
                if self.tree_data[i] > self.tree_data[temp]:
                    break
                self.tree_data[i], self.tree_data[temp] = self.tree_data[temp], self.tree_data[i]
                i = temp
            return root
    
    def get_parent(self, child):
        # child - индекс детеныша
        if child == 0:
            # Возвращаем root
            return child

        return (child - 1) // 2
    
    def get_children(self, parent):
        left_child, right_child = 2 * parent + 1, 2 * parent + 2
        if left_child >= len(self.tree_data):
            left_child = None
        if right_child >= len(self.tree_data):
            right_child = None

        return left_child, right_child

    def newsift_up(self):
        child = len(self.tree_data) - 1
        while self.tree_data[child] > self.tree_data[self.get_parent(child)]:
            self.tree_data[child], self.tree_data[self.get_parent(child)] = self.tree_data[self.get_parent(child)], self.tree_data[child]
            child = self.get_parent(child)

    # Стартовать с корня и проверить вниз правильность дерева 
    def newsift_down(self, parent):
        left_child, right_child = self.get_children(parent)
        if left_child is not None and right_child is not None:
            if self.tree_data[parent] >= self.tree_data[left_child] and self.tree_data[parent] >= self.tree_data[right_child]:
                return
    
            if self.tree_data[left_child] <= self.tree_data[right_child]:
                self.swap(right_child, parent)
                self.newsift_down(right_child)
            else:
                self.swap(left_child, parent)
                self.newsift_down(left_child)
        
        elif left_child is not None:
            if self.tree_data[left_child] > self.tree_data[parent]:
                self.swap(left_child, parent)
                
        



    
    def push(self, item):
        self.tree_data.append(item)
        self.newsift_up()

    def pop(self):
        if len(self.tree_data) == 0:
            pass
        elif len(self.tree_data) == 1:
            return self.tree_data.pop()
        else:
            self.swap(0, len(self.tree_data) - 1)
            root = self.tree_data.pop()
            self.newsift_down(0)
            return root

    def swap(self, lhs, rhs):
        self.tree_data[lhs], self.tree_data[rhs] = self.tree_data[rhs], self.tree_data[lhs]



def main_heap():
    heap = Heap([])
    n = int(input())
    for _ in range(n):
        str = input().split()
        if str[0] == "Insert":
            heap.push(int(str[1]))
        elif str[0] == "ExtractMax":
            print(heap.pop())

def make_random_input(inp_len, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(inp_len)]

def main_test():
    random.seed(42)
    for i in range(100):
        print('###############\n')
        print(f'{i}...')
        print('###############\n')
        inp_len = random.randint(5, 100)
        lower_bound = random.randint(0, 20)
        upper_bound = lower_bound + random.randint(20, 100)
        test_input = make_random_input(inp_len, lower_bound, upper_bound)
        
        reference_heap = [-inp for inp in test_input]
        heapq.heapify(reference_heap)
        pahan_heap = Heap(test_input)
        pahan_heap.heapify()

        print(f'pahan_heap: {pahan_heap.tree_data}')
        print(f'reference: {reference_heap}')

        for _ in range(100):
            item_for_push = random.randint(lower_bound, upper_bound)
            print('-----------------')
            print(f'Item for push: {item_for_push}')

            pahan_heap.push(item_for_push)
            pahan_heap.newsift_up()
            heapq.heappush(reference_heap, -item_for_push)
            
            print('AFTER PUSH:')
            print(f'pahan_heap: {pahan_heap.tree_data}')
            print(f'reference: {reference_heap}')
            

            pahan_item = pahan_heap.pop()
            reference_item = -heapq.heappop(reference_heap)
            print('\nAFTER POP:')
            print(f'pahan_heap: {pahan_heap.tree_data}')
            print(f'reference: {reference_heap}')

            print('-----------------')
            assert pahan_item == reference_item, f"{pahan_item} != {reference_item}, \npahan_heap: {pahan_heap.tree_data}\nreference: {reference_heap}"
        print('OK')


    # test_data = [random.randint(1, 100) for _ in range(20)]
    # test_heap = Heap(test_data)
    # test_heap.heapify()

    # print(test_heap.tree_data)

if __name__ == "__main__":
    # heap = Heap([1, 2, 4, 10, 2000])
    # heap.heapify()
    # print(f"{heap.data}, {heap.tree_data}")
    # heap.sift_up(10)
    # print(heap.tree_data)
    # print(heap.sift_down())
    # print(heap.tree_data)
    
    # main_test()
    main_heap()