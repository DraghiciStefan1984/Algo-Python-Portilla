def sequential_search(arr, elem):
    pos=0
    found=False
    while pos<len(arr) and not found:
        if arr[pos]==elem:
            found=True
        else:
            pos+=1
    return found


def ordered_sequential_search(arr, elem):
    pos=0
    found=False
    stopped=False
    while pos<len(arr) and not found and not stopped:
        if arr[pos]==elem:
            found=True
        else:
            if arr[pos]>elem:
                stopped=True
            else:
                pos+=1
    return found


def binary_search(arr, elem):
    first=0
    last=len(arr)-1
    found=False
    while first<=last and not found:
        mid=(first+last)//2
        if arr[mid]==elem:
            found=True
        else:
            if elem<arr[mid]:
                last=mid-1
            else:
                first=mid+1
    return found


def binary_search_rec(arr, elem):
    if len(arr)==0:
        return False
    else:
        mid=len(arr)//2
        if elem==arr[mid]:
            return True
        else:
            if elem<arr[mid]:
                return binary_search_rec(arr[:mid], elem)
            else:
                return binary_search_rec(arr[mid+1:], elem)