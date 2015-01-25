def letter_freq(text):

    freq_d = {}
    for c in text:
        c = c.lower()
        if c in freq_d:
            freq_d[c] += 1
        else:
            freq_d[c] = 1

    return freq_d

def make_pretty(dic):

    # make copy
    d = dict(dic)
    
    total = 0
    for c in d:
        total += d[c]

    for c in d:
        d[c]=float(d[c])/total

    vals = d.items()
    vals.sort()

    return vals
    

f = open("les_mis.txt", "r")
text = f.read()
d = letter_freq(text)
print make_pretty(d)
