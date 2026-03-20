# Integer
a = 16
print("Before:", id(a))

a = a + 4
print("After:", id(a))


# String
s = "hello"
print("Before:", id(s))

s = s + " world"
print("After:", id(s))


# List
l = [1, 2, 3]
print("Before:", id(l))

l.append(4)
print("After:", id(l))