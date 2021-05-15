from zope.interface import Interface, Attribute, implementer

class ISorted(Interface):
    def SortAscending(self, data):
        """ """

    def SortDescending(self, data):
        """ """


@implementer(ISorted)
class BubbleSort(object):
    _selector = None
    _comparer = None

    def __init__(self, selector, comparer):
        self._selector = selector
        self._comparer = comparer

    def SortAscending(self, arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1):
                if self._comparer(self._selector(arr[j + 1]), self._selector(arr[j])) < 0:
                    self.temp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = self.temp

    def SortDescending(self, arr):
        self.SortAscending(arr)
        arr.reverse()


@implementer(ISorted)
class HeapSort(object):
    _selector = None
    _comparer = None
    _array = []
    _heapsize = None

    def __init__(self, selector, comparer):
        self._selector = selector
        self._comparer = comparer

    def SortAscending(self, arr):
        self._array = arr
        self._heapsize = len(arr)
        self.HeapSort()

    def SortDescending(self, arr):
        self.SortAscending(arr)
        reversed = arr.reverse()

    def HeapSort(self):
        self.BuildMaxHeap()
        for i in range(len(self._array) -1 ,0,-1):
            temp = self._array[0]
            self._array[0] = self._array[i]
            self._array[i] = temp

            self._heapsize -= 1
            self.MaxHeapify(0)

    def Left(self, i):
        return 2*i+1

    def Right(self, i):
        return 2*i+2

    def MaxHeapify(self, i):
        l = int(self.Left(i))
        r = int(self.Right(i))
        lagest = i

        if l < self._heapsize and self._comparer(self._selector(self._array[l]), self._selector(self._array[i])) > 0:
            lagest = l

        if r < self._heapsize and self._comparer(self._selector(self._array[r]), self._selector(self._array[lagest])) > 0:
            lagest = r

        if lagest is not i:
            temp = self._array[i]
            self._array[i] = self._array[lagest]
            self._array[lagest] = temp

            self.MaxHeapify(lagest)

    def BuildMaxHeap(self):
        i = int(len(self._array)/2)

        while i >= 0:
            self.MaxHeapify(i)
            i-=1


@implementer(ISorted)
class InsertionSort(object):
    _selector = None
    _comparer = None

    def __init__(self, selector, comparer):
        self._selector = selector
        self._comparer = comparer

    def SortAscending(self, arr):
        for i in range(len(arr)):
            cur = arr[i]
            j = i
            while j > 0 and self._comparer(self._selector(cur), self._selector(arr[j - 1])) < 0:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = cur


    def SortDescending(self, arr):
        self.SortAscending(arr)
        arr.reverse()


@implementer(ISorted)
class MergeSort(object):
    _selector = None
    _compare = None

    def __init__(self, selector, comparer):
        self._selector = selector
        self._comparer = comparer

    def SortAscending(self, arr):
        if len(arr) <= 1:
            return

        midPoint = int(len(arr)/2)
        takeArray = arr[:midPoint]
        self.SortAscending(takeArray)
        skipArray = arr[-midPoint:]
        self.SortAscending(skipArray)
        self.Merge(arr, takeArray, skipArray)

    def Merge(self, arr, left, right):
        leftIndex = 0
        rightIndex = 0
        sortedIndex = 0

        while(leftIndex < len(left) and rightIndex < len(right)):
            comparison = self._comparer(self._selector(left[leftIndex]), self._selector(right[rightIndex]))
            if comparison <= 0:
                arr[sortedIndex] = left[leftIndex]
                leftIndex+=1
            else:
                arr[sortedIndex] = right[rightIndex]
                rightIndex+=1
            sortedIndex += 1

        while leftIndex < len(left):
            arr[sortedIndex] = left[leftIndex]
            leftIndex+=1
            sortedIndex+=1

        while rightIndex < len(right):
            arr[sortedIndex] = right[rightIndex]
            rightIndex+=1
            sortedIndex+=1

    def SortDescending(self, arr):
        self.SortAscending(arr)
        arr.reverse()


@implementer(ISorted)
class Sort(object):
    _selector = None
    _comparer = None

    def __init__(self, selector, comparer):
        self._selector = selector
        self._comparer = comparer


    def SortAscending(self, arr):
        self.Sort(arr, 0, len(arr) - 1)

    def Partition(self, m, a, b):
        i = a
        j = a
        while j <= b:
            if self._comparer(self._selector(m[j]), self._selector(m[b])) <= 0:
                t = m[i]
                m[i] = m[j]
                m[j] = t
                i += 1
            j+=1
        return i - 1

    def Sort(self, m, a, b):
        if a >= b:
            return

        c = self.Partition(m, a, b)
        self.Sort(m, a, c - 1)
        self.Sort(m, c + 1, b)


    def SortDescending(self, arr):
        self.SortAscending(arr)
        reversed = arr.reverse()


@implementer(ISorted)
class SelectionSort(object):
    _selector = None
    _comparer = None

    def __init__(self, selector, comparer):
        self._selector = selector
        self._comparer = comparer


    def SortAscending(self, arr):
        length = len(arr)

        for i in range(length):
            min = i
            j = i + 1
            while j != length:
                if self._comparer(self._selector(arr[j]), self._selector(arr[min])) < 0:
                    min = j
                j+=1

            if min is not i:
                temp = arr[i]
                arr[i] = arr[min]
                arr[min] = temp

    def SortDescending(self, arr):
        self.SortAscending(arr)
        reversed = arr.reverse()


class IPrototype(Interface):
    def Copy(self):
        """"""


@implementer(IPrototype)
class ArrayPrototype(object):
    Data = None
    def __init__(self, data):
        self.Data = data

    def Copy(self):
        dataCopy = self.Data.copy()
        return ArrayPrototype(dataCopy)

class Food():
    HighestCalories = None

    def __init__(self, highestCalories):
        self.HighestCalories = highestCalories


def ShowSortResults(titile, strategy, array):
    data1 = array.Copy().Data
    strategy.SortAscending(data1)

    data2 = array.Copy().Data
    strategy.SortDescending(data2)

    print(titile)
    print("Ascending")
    for x in range(len(data1)):
        print(data1[x].HighestCalories)
    print("Descending")
    for x in range(len(data2)):
        print(data2[x].HighestCalories)


def PrintAbout():
    print("Пашковская Екатерина Анатольевна")
    print("8-Т3О-402Б-16")
    print("Лабораторная работа 3")


def FoodToHighestCalories(Food):
    return Food.HighestCalories

def comporator(x, y):
    if x > y: return 1
    if x == y: return 0
    if x < y: return -1

if __name__ == '__main__':
    PrintAbout()

    Food1 = Food(1500)
    Food2 = Food(405)
    Food3 = Food(1234)
    Food4 = Food(5)
    data = [
        Food1,
        Food2,
        Food3,
        Food4
    ]

    array = ArrayPrototype(data)
    bubbleSort = BubbleSort(FoodToHighestCalories, comporator)
    ShowSortResults("Bubble sort", bubbleSort, array)

    insertionSort = InsertionSort(FoodToHighestCalories, comporator)
    ShowSortResults("Insertion sort", insertionSort, array)

    selectionSort = SelectionSort(FoodToHighestCalories, comporator)
    ShowSortResults("Selection sort", selectionSort, array)

    Sort = Sort(FoodToHighestCalories, comporator)
    ShowSortResults("Quick sort", Sort, array)

    mergeSort = MergeSort(FoodToHighestCalories, comporator)
    ShowSortResults("Merge sort", mergeSort, array)

    heapsort = HeapSort(FoodToHighestCalories, comporator)
    ShowSortResults("Heap sort", heapsort, array)











