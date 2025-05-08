def vowels(n):
    value=0

    for ch in n:
        if ch in "aeiouAEIOU":
            value+=1
    return value
n="DHARISH JAYAPRIYAN J"
print(vowels(n))


### TO COUNT NUMBER OF VOWELS

def vowels_count(a):
    vowel="aeiou"
    count={v:0 for v in vowel}
    for ch in n.lower():
        if ch in vowel:
            count[ch]+=1
        return count
a="aeiou"
print(vowels_count(a))
