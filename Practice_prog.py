import random as rd

head_or_tail = rd.choice(['head', 'tail'])
if head_or_tail == 'head':
    print('Head')
else:
    print('Tail')