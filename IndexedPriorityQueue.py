# Code created by Dr. Haynes Heaton
# COMP 5970
# Code used by Wesley Lowman - Fall 2022 Final Project

class IndexedPriorityQueue:
    def __init__(self):
        self.min_heap = []
        self.index = {}

    def push(self, key, value):
        self.index[key] = len(self.min_heap)
        self.min_heap.append([key, value])
        self.__heapify_up(key)

    def popmin(self):
        to_return = self.min_heap[0]
        del self.index[to_return[0]]
        end = self.min_heap.pop()
        if self.min_heap:
            self.min_heap[0] = end
            self.index[end[0]] = 0
            self.__heapify_down(end[0])
        return to_return

    def peek(self):
        return self.min_heap[0]

    def decrease_key(self, key, new_value):
        self.min_heap[self.index[key]][1] = new_value
        self.__heapify_up(key)

    def __heapify_up(self, key):
        #Passing a key to internal functions instead of the
        #index requires a completely redundant dict lookup :(
        index = self.index[key]

        if index != 0:
            parent_index = (index - 1) // 2 #truncated division
            if self.min_heap[index][1] < self.min_heap[parent_index][1]:
                self.__swap(index, parent_index)
                self.__heapify_up(key)

    def __heapify_down(self, key):
        index = self.index[key]

        #Can the base interpreter even possibly do tail-recursion optimization?
        child_index = 2 * index + 1
        if child_index < len(self.min_heap):
            if child_index + 1 < len(self.min_heap) \
                    and self.min_heap[child_index][1] > self.min_heap[child_index + 1][1]:
                child_index = child_index + 1

            if self.min_heap[index][1] > self.min_heap[child_index][1]:
                self.__swap(index, child_index)
                self.__heapify_down(key)

    #-------------------------
    #----- New functions -----
    #-------------------------
    def __swap(self, index1, index2):
        #I absolutely do not trust python reference semantics, just swap manually
        tmp = self.min_heap[index1]
        self.min_heap[index1] = self.min_heap[index2]
        self.min_heap[index2] = tmp
        self.index[self.min_heap[index1][0]] = index1
        self.index[self.min_heap[index2][0]] = index2

    def __getitem__(self, key):
        #Obtain the value from an input key
        return self.min_heap[self.index[key]][1]

    def __contains__(self, key):
        return key in self.index

    def __len__(self):
        return len(self.min_heap)
