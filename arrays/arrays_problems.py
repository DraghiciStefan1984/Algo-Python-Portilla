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