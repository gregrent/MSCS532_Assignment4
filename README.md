# MSCS532_Assignment4

# 🧮 HeapSort & Priority Queue Scheduler

## 📦 Overview

This Python project implements two core components:

1. **HeapSort**  
   - A sorting algorithm based on the binary heap data structure.

2. **Priority Queue Scheduler**  
   - A task manager that uses a max-heap to schedule tasks by priority

---

## 🚀 How to Run

### Requirements
- Python 3.6 or higher (no external libraries needed)

### Command to run the code
python assignment_4.py

---

## 📊 Summary of Findings

HeapSort
- Time complexity is O(n log n) in all cases (best, average, and worst).
- This comes from building the heap in O(n) and performing n extractions in O(log n) each.
- Space complexity is O(1) since it's an in-place sorting algorithm.
- While HeapSort offers stable performance and memory efficiency, it is often slower in practice than Quicksort due to poor cache performance and higher constant factors.

Priority Queue (Max-Heap)
- Implemented using a binary heap stored in an array for simplicity and efficiency.
- Core operations:
    - insert: O(log n)
    - extract_max: O(log n)
    - increase_key: O(log n)
    - is_empty: O(1)
- A max-heap is used to model scheduling where higher priority values mean more urgent tasks.
- The binary heap provides an optimal balance between performance (logarithmic operations) and ease of implementation.


## 🔍 Observations

- Empirical tests showed that:
    - Quicksort is generally faster on random inputs but can degrade without a good pivot strategy.
    - Merge Sort is consistent and stable, performing well across all distributions.
    - HeapSort performs steadily across input types but is slightly slower in practice.

- The priority queue implementation handled dynamic scheduling effectively and demonstrated how task priorities can be managed efficiently in real-time systems.