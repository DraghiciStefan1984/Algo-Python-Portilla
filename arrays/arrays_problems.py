import collections


def anagram_check_1(s1, s2):
    s1=s1.replace(' ', '').lower()
    s2=s2.replace(' ', '').lower()
    return sorted(s1)==sorted(s2)


def anagram_check_2(s1, s2):
    s1=s1.replace(' ', '').lower()
    s2=s2.replace(' ', '').lower()
    if len(s1)!=len(s2):
        return False
    count={}
    for letter in s1:
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1
    for letter in s2:
        if letter in count:
            count[letter]-=1
        else:
            count[letter]=1
    for k in count:
        if count[k]!=0:
            return False
    return True


def array_pair_sum(arr, k):
    if len(arr)<2:
        return
    seen=set()
    output=set()
    for num in arr:
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    return '\n'.join(map(str, list(output)))


def find_missing_element_1(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1, arr2):
        if num1!=num2:
            return num1
    return arr1[-1]


def find_missing_element_2(arr1, arr2):
    d=collections.defaultdict(int)
    for num in arr1:
        d[num]+=1
    for num in arr2:
        if d[num]==0:
            return num
        else:
            d[num]-=1


def largest_continuous_sum(arr):
    if len(arr)==0:
        return 0
    max_sum=curent_sum=arr[0]
    for num in arr[1:]:
        curent_sum=max(curent_sum+num, num)
        max_sum=max(curent_sum, max_sum)
    return max_sum