class BacktrackingAlgorithm(): pass
class BruteForceAlgorithm(): pass
class DynamicProgrammingAlgorithm():pass
class GreedyAlgorithm(): pass
class HashingAlgorithm(): pass

class MiscAlgorithms():
    def LuhnAlgorithm(): pass

class RandomizedAlgorithms(): pass
class RecursiveAlgorithms(): pass
class SearchAlgorithms():

    def LinearSearch(self): pass
    def BinarySearch(self): pass
class SortAlgorithms():

    def BubbleSort(self, arg): pass

    def MergeSort(self, array, start, end):
        #   Adapted from geeksforgeeks.org
        
        if start >= end:
            return

        def merge(array, left, mid, right):
            subArrayOne = mid - left + 1
            subArrayTwo = right - mid

            # Create temp arrays
            leftArray = [0] * subArrayOne
            rightArray = [0] * subArrayTwo

            # Copy data to temp arrays leftArray[] and rightArray[]
            for i in range(subArrayOne):
                leftArray[i] = array[left + i]
            for j in range(subArrayTwo):
                rightArray[j] = array[mid + 1 + j]

            indexOfSubArrayOne = 0  # Initial index of first sub-array
            indexOfSubArrayTwo = 0  # Initial index of second sub-array
            indexOfMergedArray = left  # Initial index of merged array

            # Merge the temp arrays back into array[left..right]
            while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
                if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
                    array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
                    indexOfSubArrayOne += 1
                else:
                    array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
                    indexOfSubArrayTwo += 1
                indexOfMergedArray += 1

            # Copy the remaining elements of left[], if any
            while indexOfSubArrayOne < subArrayOne:
                array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
                indexOfSubArrayOne += 1
                indexOfMergedArray += 1

            # Copy the remaining elements of right[], if any
            while indexOfSubArrayTwo < subArrayTwo:
                array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
                indexOfSubArrayTwo += 1
                indexOfMergedArray += 1
            return

        mid = start + (end - start) // 2

        self.MergeSort(array, start, mid)
        self.MergeSort(array, mid + 1, end)
        merge(array, start, mid, end)

        return array

    def SelectionSort(self, arg): pass
    
