# task 3
str1 = "spam"
str2 = "ni ! "
print("Task 3: ")
print("a)", " The Knights who say , " + str2)
print("b)", 3 * str1 + 2 * str2)
print("c)", str1[1])
print("d)", str1[1:3])
print("e)", str1[2]+ str2[:2])
print("f)", str1+ str2[-1])
print("g)", str1.upper())
print("h)", str2.upper()*3)

# task 4
print("Task 4: ")
print("a)", end = " ")
for ch in " aardvark":
    print (ch)

print("b)", end = " ")
for w in " Now is the winter of our discontent . . . ".split():
    print (w)

print("c)", end = " ")
for w in "Mississippi".split("i") :
    print (w , end= " ")

print("\nd)", end = " ")
msg = " "
for s in "secret".split("e") :
    msg = msg + s
print (msg)

print("e)", end = " ")
msg = " "
for ch in "secret":
    msg = msg + chr(ord(ch) + 1)
print(msg)

