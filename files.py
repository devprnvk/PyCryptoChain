f = open('demo.txt', mode='w')
f.write('Hello from python!')
f.close()

f = open('demo.txt', mode='r')
for line in f.readlines:
    print(line)
f.close()