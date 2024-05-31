"""
This module contains sorting algorithms learnt in the A-Level CS course
"""

class Sort:
    """
    This class currently contains bubble sort, insersion sort and merge sort
    """

    def bubble_sort(self, arr):
        """
        This function sorts an array using bubble sort
        """

        n = len(arr)
        for i in range(n):
            noSwaps = True
            for j in range(n - i - 1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    noSwaps = False

            if noSwaps:
                break

        return arr

    def insertion_sort(self, arr):
        """
        This function sorts an array using insertion sort
        """

        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

        return arr

    def merge_sort(self, arr):
        """
        This function sorts an array using merge sort
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr
