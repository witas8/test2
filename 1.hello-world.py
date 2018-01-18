print('Hello, world')
a = 5
b = 10
c = a + b
print('wynik to %s' % c)

x = int(input('x:'))
op = input('operacja:')
y = int(input('y:'))
if op == '+':
    print('%s + %s = %s' % (x,y,(x+y)))
elif op == '-':
    print('%s - %s = %s' % (x,y,(x-y)))

x = 60 / 94
print('%s' % x)