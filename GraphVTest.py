from DSViz.GraphV import GraphV

# test = GraphV(Directed=True)
test = GraphV()
test.add('run', 'intr')
test.add('intr', 'runbl')
test.add('runbl', 'run')
test.add('run', 'kernel')
test.add('kernel', 'zombie')
test.add('kernel', 'sleep')
test.add('kernel', 'runmem')
test.add('sleep', 'swap')
test.add('swap', 'runswap')
test.add('runswap', 'new')
test.add('runswap', 'runmem')
test.add('new', 'runmem')
test.add('sleep', 'runmem')


test.show

test2 = GraphV()
test2.add('new', ['runswap', 'runmem'])
test2.add('runswap', ['runmem', 'new', 'swap'])
# test2.show