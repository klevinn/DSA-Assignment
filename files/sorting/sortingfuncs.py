from sorting.sortingfuncsplus import *
from general.shortenfuncs import *

"""
All Sorting Functions 

All functions require the arguments : arr, mode, rev

arr = the array of objects to be sorted
mode = the type of sorting to be done (Customer Name, Package Name, Number of Pax , Cost Per Pax)
rev = 1 if ascending, 2 if descending

method() function basically gets the value from the object see in shortenfunc.py in the general folder
"""
"""
Bubble Sort Function
    Best time complexity: O(n)
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)

Greater Element Bubbles up to the top

First we check through all the elements using the for _ in range(n) loop
Then we check through all the elements using the for i in range(n-1) loop
For rev == 1: Meaning we sort in ascending order, if the element is greater than the next element swap the 2
For rev == 2: Descending order, we just swap the sign

Demonstration

Initial : [5,1,2]
First Loop : [1,5,2]
Second Loop : [1,2,5]
"""
def bubbleSort(arr, mode, rev):
    method = determine_type(mode)
    n = len(arr)

    for _ in range(n):
        for i in range(n-1):
            if (rev == 1):
                if (method(arr[i]) > method(arr[i+1])):
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if (method(arr[i]) < method(arr[i+1])):
                    arr[i], arr[i+1] = arr[i+1], arr[i]

"""
Selection Sort Function
    Best time complexity: O(n^2)
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)

Compare element with all elements till lowest is found and swaps with the first index

First to ensure we check through all the elements, we use the for i in range(n) loop:
Then we check through the rest of the elements using the for j in range(i+1,n) loop
For rev == 1: Meaning we sort in ascending order, if the element is greater than the next element we assign the next index as lowest, we keep doing till we are through all the elements of the list. After that we swap the first element and the lowest element (based of lowest index)
For rev == 2: Descending order, we just swap the sign to make it so that the index of the highest value is stored in the lowest

Demonstration

Initial = [5,1,2]
First Loop : 
    lowest variable is assigned to index 1 or the value 5
    Since 1 is lesserr than 5, the index 2 is assigned to the lowest variable
Second Loop : 
    lowest variable stays assigned to index 2 as 1 is lesser than 2
After all comparisons with rest of the elements:
The element at index 1 (lowest variable) swaps with the first index:
[1,5,2]

This goes on for all elements
"""
def selectionSort(arr, mode, rev):
    method = determine_type(mode)
    n = len(arr)
    for i in range(n):
        lowest = i
        for j in range(i+1,n):
            if (rev == 1):
                if (method(arr[j]) < method(arr[lowest])):
                    lowest = j
            else:
                if (method(arr[j]) > method(arr[lowest])):
                    lowest = j
        
        arr[i], arr[lowest] = arr[lowest], arr[i]

"""
Insertion Sort Function
    Best time complexity: O(n)
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)

Similar to Selection, in terms of comparing through all elements in the list. However, Insertion works backwards and instead of storing the index, swaps the element with the previous element if the previous element is greater

The for i in range (1,n) starts from 1 due to us minusing the index by 1 if swap, hence if start from 0 will return index error / redundent code as the while loop will never be entered
The while loop basically checks the current element with the previous element, if the previous element is greater than the current element, we replace the current element with the previous element. The -= 1 is to continuously move down the list
arr[current] = value places the replaced value in the current index

Demonstration

Initial = [5,1,2]
First loop : 
    current = 1
    1 is greater than 5, so the current element gets replaced
    [5,5,2]
    The current value minuses one so = 0, exitting the loop
    Replacing the current with the replaced element
    [1,5,2]

Keeps going through all elements of the list
""" 
def insertionSort(arr, mode, rev):
    method = determine_type(mode)
    n = len(arr)
    for i in range(1,n):
        value = arr[i]
        current = i
        if (rev == 1):
            while (current > 0) and (method(arr[current-1]) > method(value)):
                arr[current] = arr[current-1]
                current -= 1
        else:
            while (current > 0) and (method(arr[current-1]) < method(value)):
                arr[current] = arr[current-1]
                current -= 1
        
        arr[current] = value

"""
Merge Sort Function
    Best time complexity: O(n log n)
    Worst time complexity: O(n log n)
    Average time complexity: O(n log n)

Merge Sort breaks the list into 2 halves, then recursively calls itself on the 2 halves until the list is 1 element
Then we merge the 2 halves together all the way till the list is sorted

Demonstration

Initial = [5,1,2,4]
First Split = [5,1] & [2,4]
Second Split = [5], [1], [2], [4]

Merge together = [1,5] , [2,4]
Merge Together = [1,2,4,5]

Keeps going through all elements of the list
""" 
def mergeSort(arr, mode, rev):
    if (len(arr) <= 1):
        return arr
    else:
        mid = len(arr) // 2

        lefthalf = mergeSort(arr[:mid], mode, rev)
        righthalf = mergeSort(arr[mid:], mode, rev)

        newList = mergeSortedList(lefthalf, righthalf, mode, rev)

        return newList

"""
Quick Sort Function
    Best time complexity: O(n log n)
    Worst time complexity: O(n log n)
    Average time complexity: O(n^2)

Quick sort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
Finds pivot where left side is smaller and right side is greater

Demonstration
Initial = [7,2,1,6]
Pointer set at 6 (last element)
Then compares with the first element if greater, set as second pointer, in the above example, 7 will be set as the second pointer

Now initial pointer compares with the element after the first element, since the element is greater than the pointer (6>2), swap the 6 and the 2, if not check with the next element
Next List = [2,7,1,6].

The second pointer will then switch to the second element(still 7)
6 compares with 1, its greater (6>1), swap occurs again
Next List = [2,1,7,6]

So now we reach the second last element we swap the first pointer with the last pointer
Next list = [2,1,6,7]
Now look at the list into 2 where the pointer is the middle:
Pretend the list is like this = [2,1,6] & [7]

Run quicksort on both to sort them
""" 
def quickSort(array, low, high, mode, rev):
    if (low < high):
        pi = partition(array, low, high, mode, rev)

        quickSort(array, low, pi - 1, mode, rev)
        quickSort(array, pi + 1, high, mode, rev) 

"""
Counting Sort Function
    Best time complexity: O(n + k)
    Worst time complexity: O(n + k)
    Average time complexity: O(n + k)

Why use Counting Sort:
    better time complexity 
    though space complexity may be sacrificed when dealing with larger numbers
        Worst Space Complexity : O(MAX)

Counting Sort counts the number of occurences of each number
Length of count list will be the greatest number in the list
store cumulative count in the count list
Index = value. Then the number in that index will be where its placed in the new list
Minus one after using


What lines are for:
Initialize count array
count = [0] * (greatest + 1)

for i in range(0, size) helps Store the count of each elements in count array

Stores the cummulative count
for i in range(1, len(count)):
    count[i] += count[i - 1]

Find the index of each element of the original array in count array
place the elements in output array
i = size - 1

demonstration

arr = [2,5,4,1]
count = [0,0,0,0,0]
after counting:
[0,1,1,0,1,1]

Cumulative:
[0,1,2,2,3,4]

For element 2, we look at index 2
The value is 2. The index of where 2 is placed is 2-1 = 1
[x,2,x,x]

For element 5, we look at index 5
the value is 4. the index of where 5 is placed is 4-1 =3
[x,2,x,5]

Done till sorted: 
[1,2,4,5]
"""
def countingSort(array, mode, rev):
    size = len(array)
    output = [0] * size
    newarr = []
    for i in range(len(array)):
        if (mode == 1):
            newarr.append(array[i].get_paxnum())
        else:
            newarr.append(round(array[i].get_packcost()))
    greatest = max(newarr)

    count = [0] * (greatest + 1)

    for i in range(0, size):
        if (mode == 1):
            count[array[i].get_paxnum()] += 1
        else:
            count[round(array[i].get_packcost())] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = size - 1
    if (rev == 1):
        while (i >= 0):
            if (mode == 1):
                output[count[array[i].get_paxnum()] - 1] = array[i]
                count[array[i].get_paxnum()] -= 1
            else:
                output[count[round(array[i].get_packcost())] - 1] = array[i]
                count[round(array[i].get_packcost())] -= 1

            i -= 1

    else:
        while (i >= 0):
            if (mode == 1):
                output[-(count[array[i].get_paxnum()])] = array[i]
                count[array[i].get_paxnum()] -= 1
            else:
                output[-(count[round(array[i].get_packcost())])] = array[i]
                count[round(array[i].get_packcost())] -= 1
            
            i -= 1

    return output

"""
Shell Sort 
    Best Time Complexity: O(n log n)
    Average Time Complexity: O(n log n)
    Worst Time Complexity: O(n^2)

Why Shell Sort:
    Better Time Complexity, Not as many comparisons.

Similar logic to Insertion but uses intervals to deal with element further apart, and the intervals get smaller & smaller

Rearrange elements at each n/2, n/4, n/8, ... intervals
Compare using intervals , divide the intervals by 2 after completion of for loop with first interval

Compares backwards and swaps when necessary

What lines are for:
for i in range(interval, n): loop through the elements in the array in intervals of the gap

temp = array[i] Storing of variable for swapping later

while (j >= interval) and (method(array[j-interval]) > method(temp)):
    OR
while (j >= interval) and (method(array[j-interval]) < method(temp)):

While loop goes on as long as the index being used (j) greater than the interval
Basically checks if greater than or lesser than, then swaps the elements

interval //= 2 = halving the interval

Demonstration:
Initial List = [10,2,7,9,1,4,7]

interval will be 3 cause len is 7
temp stores the 3rd element : 9
and j stores the index : 3

first while loop:
will compare array[0] > array[3]
since its true, the 2 elements will swap 

next pass = [9,2,7,10,1,4,7]

the j value will then minus 3 and become 0
since its no longer greater than/equal to the interval

it will swap array[j] and temp which is still 9 so no chanegs to list

the while loop ends and goes to the next for loop

where i = 4
so it will now compare array[1] > array[4]
since its true, the 2 elements will swap 

next pass = [9,1,7,10,2,4,7]
the j value then minuses the interval and becomes 1
breaking the while loop since lesser than the interval and swaps arr[1] with the previous arr[4], 1
meaning no changes

this goes on untill the for loop ends where i = 6.

from there the interval will be halved again becoming 1 (floor division)
the whole process goes again 
untill the interval becomes 0: 

where the array SHOULD look like [1,2,4,7,7,9,10]
"""
def shellSort(array, mode, rev):
    method = determine_type(mode)
    n = len(array)
    interval = n // 2

    while (interval > 0):
        for i in range(interval, n):
            temp = array[i]
            j = i
            if (rev == 1):
                while (j >= interval) and (method(array[j-interval]) > method(temp)):
                    array[j] = array[j-interval]
                    j-= interval
            else:
                while (j >= interval) and (method(array[j-interval]) < method(temp)):
                    array[j] = array[j-interval]
                    j -= interval   
            
            array[j] = temp    

        interval //= 2

"""
Pancake Sort 
    Best time complexity: O(n) only when array is already sorted
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)

Finds the index of the greatest element, flips the list [beginning:index of max element]
bringing the greatest number to the front and flips the whole list to the end.
then locks the last element

Using Findmax, find index of the greatest value

make the highest number the first index
the flips second argument being the maxind meaning the list flipped would be [element, element, element with maxind]

Then places the highest number at the end, by flipping the whole list

Size -= 1 : minus 1 to not touch the last element of the list

Demonstration
Initial : [2,5,10,9,3]
use find max on the list and its index : 10, index=2

flips the list up to index 2
first flip: [10,5,2,9,3]
then flips the whole list, putting the greatest element at the end
second flip = [3,9,2,5,10]

then the size they deal with will then minus 1 to no longer touch the last element
It keeps doing this untill fully sorted 

Final list : [2,3,5,9,10]
"""
def pancakeSort(arr, mode, rev):
    size = len(arr)
    while (size > 1):
        maxind = findMax(arr,size, mode , rev)
        
        if (maxind != size-1):
            flip(arr,maxind)

            flip(arr,size-1)

        size -= 1


"""
Comb Sort (Similar to Shell Sort, Deals with gaps)
    Best time complexity: O(n log n)
    Worst time complexity: O(n^2/2^p) (p is a number of increment)
    Average time complexity: O(n^2)

Comb sort does a single "bubbling" pass (ala bubble sort) over each set for each gap or increment, whereas Shell sort completely sorts each set

Comb sort is less effective than shell sort. 
Comb sort also deals with gap however its very similar to bubble sort where it compares upwards and swaps when necessary (Bubbling Up but with caps this time)

Creates the gap
while (gap > 1) or (swaps):
    gap = max(1, int(gap / 1.25))  # minimum gap is 1
    swaps = False
    
Ensures no index error.
    for i in range(len(arr) - gap):
        j = i+gap

Demonstration
Initial List = [10,2,3,5,8]

Gap will be 4 (Len of 5 / 1.25)

So compares 10 and 8, since 10 > 8, swaps the 2
Firs pass = [8,2,3,5,10]

Then runs the next while loop since the range is 1 (5-4), each comparison is one iteration of the for loop
The next gap will be 3 (4/1.25)

Compares 8 and 5, since 8 > 5 , swaps the 2
Second pass = [5,2,3,8,10]

Then compares 2 and 10, since 2 < 10, no swapping

Then runs the next while loop since the range is 2 (5-3)
The next gap will be 2 (3/1.25)

Compares 5 and 3, 5 > 3, swaps the 2
Fourth pass = [3,2,5,8,10]

The rest of the comparisons will not lead to swaps since 2 and 5 is not greater than 8 and 10

Runs the next while loop. However the gap is 1 so we look at the other condition of the while loop and since there was a swap in the previous while loop interation, its currently set to True, so it will still run the loop with a gap of 1

It will compare the first 2 elements, and since 3 > 2, it will swap the 2.

Seventh pass = [2,3,5,8,10]

As u can see its already sorted, so it will compare through it all again but no swaps will occur.

However, 1 more while loop will run because a swap did occur in the beginning of the while loop. So the variable sill set to True. However since its already sorted, it will go through the whole list without swapping anything so the swaps variable will now stay False.

Thus breaking the while loop and ending the sorting algorithm with the list

[2,3,5,8,10]
"""
def combsort(arr, mode, rev):
    method = determine_type(mode)
    gap = len(arr)
    swaps = True
    while (gap > 1) or (swaps):
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(arr) - gap):
            j = i+gap
            if (rev == 1):
                if (method(arr[i]) > method(arr[j])):
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps = True
            else:
                if (method(arr[i]) < method(arr[j])):
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps = True

"""
Cocktail Shaker Sort 
    Best time complexity: O(n) already sorteed
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)

Goes from one end of the list to the other, then starts from the end and goes back to another end , swapping any elements that are not sorted, however its one by one.

Demonstration
Initial list = [2,1,5,4]
Starts from end to beginning, comparing if greater than swaps
for example, 5 is greater than 4 so they swap them
First pass =  [2,1,4,5]
Since 1 is not greater than 4 , no swapping
Second pass = list stays the same

then comparing next 2 is greater than 1, so they swap:
third pass = [1,2,4,5]

In this case, its sorted so since now its going from beginning to end with no changes to the list. 
Then since is_swapped stays True it goes to the next pass of the original for loop

It will compare through the list the same way again, however, its already sorted, so the is_swapped variable will stay False, and it will break the for loop and  return the sorted list
"""
def cocktail_shaker_sort(nums, mode, rev):
    method = determine_type(mode)
    for i in range(len(nums)-1, 0, -1):
        is_swapped = False
        if (rev == 1):
            for j in range(i, 0, -1):
                if (method(nums[j]) < method(nums[j-1])):
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    is_swapped = True

            for j in range(i):
                if (method(nums[j]) > method(nums[j+1])):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    is_swapped = True
        else:
            for j in range(i, 0, -1):
                if (method(nums[j]) > method(nums[j-1])):
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    is_swapped = True

            for j in range(i):
                if (method(nums[j]) < method(nums[j+1])):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    is_swapped = True

        if (not is_swapped):
            return nums

"""
Heap Sort 
    Best time complexity: O(nlog n)
    Worst time complexity: O(nlog n)
    Average time complexity: O(nlog n)

Complete binary tree, visualise the List as a binary tree.
Where the array can be derived after level order traversal of the binary tree
[1,2,3,4,5]

1 root node, 2 is left subtree, 3 is right subtree, 4 is left subtree of left subtree and 5 is right subtree of the left subtree

Heap sort follows, swap, remove & heapify

Max heap is swapped to the last element of level order traversal, then removed from tree (placed into array at the last index), then heapify (make it max heap again). Then it will repeat the process until the array is sorted. / Tree is empty

Build max heap, (root node being the highest)
its // 2 because any more would result in useless loops 
Taking the //2 element as root node
Is a loop to ensure the elements deemed as root node is always max heap

Swap last element with first element (should be greatest due to maxheap)
arr[i], arr[0] = arr[0], arr[i]

Heapify new root element then redo the whole process
heapify(arr, i, 0, mode, rev)

Demonstration
***
"""
def heapSort(arr, mode, rev):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i, mode, rev)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, mode, rev)

"""
Bucket Sort
    Best time complexity: O(n+k)
    Worst time complexity: O(n^2)
    Average time complexity: O(n)

size = largest/length : size variable determines the groups per buket (for example if size = 4, numbers stored in a bucket = 1-4)
Stores the numbers in buckets, sorts the bucket and concatenate the list into one

index = int(value/size) (determines the index based of the size of each bucket)

For descending, we just flip which bucket its placed in
And for the counting sort used, i have already coded in the reverse function so it can just be used

Demonstration:
Initial list = [2,1,5,4,10]
Using largest / length, we can determine the size of each bucket, in this case its 2
Hence the values for the first bucket will be 0-1, second bucket will be 2-3 and et cetera

Initialise the bucket list same length as the initial list 

Bucket list = [[],[],[],[],[]]

Then goes through each element of the list, using the index, derived by dividing value and size to determine which bucket to add it to

For example, the first value is 2 and the size is 2. So the index derived will be 1.
Placing the value 2 into the bucket at index 1:

Bucket List = [[],[2],[],[],[]]

It goes through the list but when it reaches the greatest number , the index derived it will always be the length of the list, so the index will be the last one, cause we use its value to derive the size.
In this example it will be 10, and 10/2 = 5 and thats the length of the list 
so minus 1 from the supposed index and put it in the last bucket.

Bucket List (when it reaches 10) : [[1],[2],[5,4],[],[10]]

Then just sort each bucket, in actual code it uses the built in sort function
However, since counting sort is already implemented, we can just use it (One of the better sorts involving integers)

Sorted Bucket List = [[1],[2],[4,5],[],[10]]

Then afterwards just concatenate the list together to form the final list

Final List = [1,2,4,5,10]
"""
def bucketSort(array, mode, rev):
    length = len(array)
    largestInd = findMax(array, length, mode+2, 1)

    largest = array[largestInd].get_packcost()
    if (mode == 1):
        largest = array[largestInd].get_paxnum()

    size = largest/length
    buckets = []

    # Create Buckets
    for i in range(length):
        buckets.append([])
    # buckets = [[] for i in range(length)]

    # Bucket Sorting   
    for i in range(length):
        value = array[i].get_packcost()
        if (mode == 1):
            value = array[i].get_paxnum()


        index = int(value/size)
        if (rev == 1):
            if (index != length):
                buckets[index].append(array[i])
            else:
                buckets[length - 1].append(array[i])
        
        else:
            if (index != length):
                buckets[-(index+1)].append(array[i])
            else:
                buckets[0].append(array[i])


    # Sorting Individual Buckets  
    for i in range(len(array)):
        if (len(buckets[i]) != 0):
            buckets[i] = countingSort(buckets[i],mode, rev)


    # Flattening the Array
    result = []
    for i in range(length):
        result += buckets[i]

    return result

"""
RaditzSort (Only paxnum is implemented, and reverse uses .reverse())
    Best time complexity: O(n+k)
    Worst time complexity: O(n+k)
    Average time complexity: O(n+k)

Counting Sort using Places, such as ones, tens, hundreds

Demonstration:
Same as Counting Sort , but this time occurs multiple time for each place present
So we look at ones place first, create a count list based on that, then sort the array, then we look at the tens place, create a count list and sort the array, and so on.
"""
def radixSort(array, mode, rev):
    # Get maximum element
    maxElemInd = findMax(array, len(array), mode+2, 1)
    maxElement = array[maxElemInd].get_paxnum()

    # Apply counting sort to sort elements based on place value.
    place = 1
    while (maxElement // place > 0):
        countingSort_raditz(array, place)
        place *= 10
    
    if (rev != 1):
        array.reverse()