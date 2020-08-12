a = {"abrand": "aFord"}, {"bbrand": "bFord"}

b = {"bbrand": "zbFord"}
c = {"bbrand": "zbFord"}

b = (b,)
c = c,
d = a + b + c
print(d)
