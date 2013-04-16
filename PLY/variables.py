import collections

Variable = collections.namedtuple('Variable', 'name type')
v = Variable('i', 'int')
v2 = Variable('j', 'float')

#Directorio de Procedimientos. Se agregarán los módulos aquí.
DirProc = collections.namedtuple('DirProc', 'name retType tabVar')
d = DirProc('uno', 'none', [v,v2])
#print(d)

d.tabVar.append(Variable('var','string'))
print(d)

d.tabVar.append(Variable('dos','string'))
print("\n")
print(d)

print("\n%s" % d.tabVar)

tabVar = []

tabVar.append(v)
tabVar.append(v2)

#print(tabVar[0], tabVar[1])

v2 = Variable('k', 'int')
tabVar.append(v2)

for a in d.tabVar:
    print(a)

#print(tabVar)