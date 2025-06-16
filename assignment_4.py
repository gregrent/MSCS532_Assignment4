# MSCS 532 Assignment 4
# Heapsort and Priority Queue with
# Task Management Implementation

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)
    return arr


class Task:
    def __init__(self, task_id, priority, arrival_time=None, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return (f"Task(id={self.task_id}, priority={self.priority}, "
                f"arrival={self.arrival_time}, deadline={self.deadline})")


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.task_position = {}  # Maps task_id to index in heap for O(1) access

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.task_position[self.heap[i].task_id], self.task_position[self.heap[j].task_id] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i):
        while i > 0 and self.heap[self._parent(i)].priority < self.heap[i].priority:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            left = self._left(i)
            right = self._right(i)
            largest = i

            if left < n and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < n and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != i:
                self._swap(i, largest)
                i = largest
            else:
                break

    def insert(self, task):
        """Insert a new task into the heap."""
        self.heap.append(task)
        idx = len(self.heap) - 1
        self.task_position[task.task_id] = idx
        self._heapify_up(idx)
        # Time complexity: O(log n)

    def extract_max(self):
        """Remove and return the task with the highest priority."""
        if not self.heap:
            return None
        max_task = self.heap[0]
        last_task = self.heap.pop()
        del self.task_position[max_task.task_id]
        if self.heap:
            self.heap[0] = last_task
            self.task_position[last_task.task_id] = 0
            self._heapify_down(0)
        return max_task
        # Time complexity: O(log n)

    def increase_key(self, task_id, new_priority):
        """Increase the priority of a task and fix heap."""
        if task_id not in self.task_position:
            raise KeyError(f"Task ID {task_id} not found")
        i = self.task_position[task_id]
        if new_priority < self.heap[i].priority:
            raise ValueError("New priority is lower than current priority.")
        self.heap[i].priority = new_priority
        self._heapify_up(i)
        # Time complexity: O(log n)

    def is_empty(self):
        return len(self.heap) == 0
        # Time complexity: O(1)

    def __repr__(self):
        return f"PriorityQueue({self.heap})"


if __name__ == "__main__":
    print("Testing heapsort:")
    test_arrays = [
        [3, 6, 5, 7, 2, 9, 1],
        [10, 20, 15, 12, 40, 25, 18],
        [1],
        [],
        [5, 5, 5, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    for arr in test_arrays:
        sorted_arr = heapsort(arr.copy())
        print(f"Original: {arr}\nSorted: {sorted_arr}\n")
    
    
    print("\nTesting PriorityQueue with Tasks:")
    pq = PriorityQueue()
    
    tasks = [
        Task(task_id=1, priority=20, arrival_time=0, deadline=10),
        Task(task_id=2, priority=15, arrival_time=2, deadline=12),
        Task(task_id=3, priority=30, arrival_time=1, deadline=15),
        Task(task_id=4, priority=10, arrival_time=3, deadline=20),
    ]
    
    # Insert tasks
    for task in tasks:
        pq.insert(task)
        print(f"Inserted: {task}")
        print(f"Heap: {pq}")
    
    # Extract max (highest priority)
    max_task = pq.extract_max()
    print(f"\nExtracted max task: {max_task}")
    print(f"Heap after extraction: {pq}")
    
    # Increase key of task 2
    pq.increase_key(task_id=2, new_priority=35)
    print(f"\nIncreased priority of task 2 to 35")
    print(f"Heap after priority increase: {pq}")
    
    # Extract max again
    max_task = pq.extract_max()
    print(f"\nExtracted max task: {max_task}")
    print(f"Heap after extraction: {pq}")
    
    # Check empty
    print(f"\nIs priority queue empty? {pq.is_empty()}")
