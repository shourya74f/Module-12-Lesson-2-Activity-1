n=int(input("How many characters to preview? "))
file=open("Code.txt", "r")
print(file.read(n))
file.close()
print()

file=open("Code.txt", "r")
l=file.readlines()
file.close()
print("Total number of lines in the file: ", len(l))
for i in range(len(l)):
    print(i+1, "-", l[i].strip())
print()

w=input("Skip lines starting with: ")
file=open("Code.txt", "r")
for line in file:
    if line.startswith(w):
        print("Skipping line: ", line.strip())
    else:
        print("Keeping line: ", line.strip())
file.close()
print()

file=open("Code.txt", "r")
l=file.readlines()
file.close()
o=open("Odd.txt", "w")
for i in range(0, len(l), 2):
    o.write(l[i])
o.close()
print("Odd lines written to Odd.txt")