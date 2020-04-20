def recursive_sum(n):
    if n==0:
        return
    else:
        return n+recursive_sum(n-1)


def sum_func(n):
    if len(str(n))==1:
        return n
    else:
        return n%10+sum_func(n//10)


def word_split(phrase, list_of_words, output=None):
    if output is None:
        output=[]
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
    return output


def reverse_string(s):
    if len(s)<=1:
        return s
    return reverse_string(s[1:])+s[0]


def permute_string(s):
    out=[]
    if len(s)==1:
        out=[s]
    else:
        for i, let in enumerate(s):
            for perm in permute_string(s[:1]+s[i+1:]):
                out+=[let+perm]
    return out