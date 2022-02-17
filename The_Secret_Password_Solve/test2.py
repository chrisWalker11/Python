a = list('deA?%@JDQE%#AIJDE\x1e%#<E')
for i in range(0, len(a)):
     val = ord(a[i])
     val = val + 5
     a[i] = chr(val)




tespass = "".join(a[::-1])

print(f"masoncc{ {tespass} }")
