a=20
b=20

print('Part 1:','\na=',a,':',id(a),'\nb=',b,':',id(b))

if (a is b):
    print("Part 2: \na and b have same identity")
else:
    print("Part 2: \na and b not have same identity\n")


if(id(a)==id(b)):
    print("Part 3: \na and b have same identity")
else:
    print("Part 3: \na and b not have same identity\n")


b=30
print('Part 4:','a=',a,':',id(a),'\nb=',b,':',id(b))

if (a is not b):
    print("Part 4: \na and b have different identity")
else:
    print("Part 4: \na and b have same identity\n")