def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        print(n)
        for k in range(n):
            print(k)
            if arr[k]>arr[k+1]:
                arr[k], arr[k+1]=arr[k+1], arr[k]


def selection_sort(arr):
    for fill_slot in range(len(arr)-1, 0, -1):
        position_of_max=0
        for location in range(1, fill_slot+1):
            if arr[location]>arr[position_of_max]:
                position_of_max=location
        arr[fill_slot], arr[position_of_max]=arr[position_of_max], arr[fill_slot]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value=arr[i]
        position=i
        while position>0 and arr[position-1]>current_value:
            arr[position]=arr[position-1]
            position-=1
        arr[position]=current_value


def shell_sort(arr):
    sublist_count=len(arr)//2
    while sublist_count>0:
        for start in range(sublist_count):
            gap_insertion_sort(arr, start, sublist_count)
        sublist_count//=2

def gap_insertion_sort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        current_value=arr[i]
        position=i
        while position>=gap and arr[position-gap]>current_value:
            arr[position]=arr[position-gap]
            position-=gap
        arr[position]=current_value


def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=j=k=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                arr[k]=left_half[i]
                i+=1
            else:
                arr[k]=right_half[j]
                j+=1
            k+=1
        while i<len(left_half):
            arr[k]=left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            arr[k]=right_half[j]
            j+=1
            k+=1


def quick_sort(arr):
    quick_sort_help(arr, 0, len(arr)-1)

def quick_sort_help(arr, first, last):
    if first<last:
        split_point=partition(arr, first, last)
        quick_sort_help(arr, first, split_point-1)
        quick_sort_help(arr, split_point+1, last)

def partition(arr, first,last):
    pivot_value=arr[first]
    left_mark=first+1
    right_mark=last
    done=False
    while not done:
        while left_mark<=right_mark and arr[left_mark]<=pivot_value:
            left_mark+=1
        while arr[right_mark]>=pivot_value and right_mark>=left_mark:
            right_mark-=1
        if right_mark<left_mark:
            done=True
        else:
            arr[left_mark], arr[right_mark]=arr[right_mark], arr[left_mark]
    arr[first], arr[right_mark]=arr[right_mark], arr[first]
    return right_mark