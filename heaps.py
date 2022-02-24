def default_comparator(lhs, rhs):
    return lhs < rhs

def custom_comparator(lhs, rhs):
    if lhs[0] == rhs[0]:
        return lhs[1] < rhs[1]
    return lhs[0] < rhs[0]

class minHeap:
# Используем представление в виде листа
    def __init__(self, comparator=default_comparator):
        self.items = []
        self.comparator = comparator
# self.items = [[curr_time, thread_number]]

    def get_parent(self, i):
        return (i - 1) // 2
    
    def get_left_child(self, i):
        if 2 * i + 1 >= len(self.items):
            return None
        return 2 * i + 1
    
    def get_right_child(self, i):
        if 2 * i + 2 >= len(self.items):
            return None
        return 2 * i + 2
    
    def swap(self, lhs, rhs):
        self.items[lhs], self.items[rhs] = self.items[rhs], self.items[lhs]

    def sift_down(self, parent):
        left_child, right_child = self.get_left_child(parent), self.get_right_child(parent)
        if left_child is not None and right_child is not None:
            if self.comparator(self.items[parent], self.items[left_child]) and self.comparator(self.items[parent], self.items[right_child]):
                return
            if self.comparator(self.items[right_child], self.items[left_child]):
                self.swap(right_child, parent)
                self.sift_down(right_child)
            else:
                
                self.swap(left_child, parent)
                self.sift_down(left_child)
        
        elif left_child is not None:
            if self.comparator(self.items[left_child], self.items[parent]):
                self.swap(left_child, parent)

    def sift_up(self):
        child = len(self.items) - 1
        while self.get_parent(child) >= 0 and self.comparator(self.items[child], self.items[self.get_parent(child)]):
            self.swap(child, self.get_parent(child))
            child = self.get_parent(child)
    
    def push(self, item):
        self.items.append(item)
        self.sift_up()

    def pop(self):
        if len(self.items) == 0:
            pass
        elif len(self.items) == 1:
            return self.items.pop()
        else:
            self.swap(0, len(self.items) - 1)
            root = self.items.pop()
            self.sift_down(0)
            return root

