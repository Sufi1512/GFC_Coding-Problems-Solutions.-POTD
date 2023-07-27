class Solution:
    def heapify(self, arr, n, i):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        # Find the index of the largest element among the root, left child, and right child
        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        # If the largest element is not the root, swap it with the root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    def buildHeap(self, arr, n):
        # Start from the last non-leaf node and heapify all nodes in reverse order
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def HeapSort(self, arr, n):
        # Build the initial binary heap
        self.buildHeap(arr, n)

        # Extract elements one by one from the heap and place them at the end of the array
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            # Reduce the size of the heap and heapify the root node
            self.heapify(arr, i, 0)
