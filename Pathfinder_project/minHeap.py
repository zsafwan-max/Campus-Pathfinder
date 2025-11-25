class MinHeap:
    def __init__(self):
        self.heap = []  # store (priority, value)

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        """Insert a new (priority, node) tuple into the heap."""
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        """Extract and return the smallest item (based on priority)."""
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self._bubble_down(0)
        return item

    def _bubble_up(self, index):
        """Move the element at 'index' up to maintain heap property."""
        while index > 0:
            parent = self._parent(index)
            if self.heap[index][0] < self.heap[parent][0]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _bubble_down(self, index):
        """Move the element at 'index' down to maintain heap property."""
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._bubble_down(smallest)

    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)