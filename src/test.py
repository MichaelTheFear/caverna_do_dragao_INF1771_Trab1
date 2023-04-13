class Test:
    def __init__(self,x):
        self.x = x

    def __repr__(self):
        return f"Test({self.x})"


lista = []
for i in range(10):
    lista.append(Test(i))

y = lista[0]

y.x = 10

print(lista[0].x)
print(lista)

