import random

teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
rooms = [[], [], []]

for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)
for i, room in enumerate(rooms):
    print('房间%d里有%d个老师' % (i, len(room)), end='')
    for teacher in room:
        print(teacher, end='\t')
    print()
