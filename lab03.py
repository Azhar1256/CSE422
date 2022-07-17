import random
high, low = 1000, -1000


def alpha_beta(height, index, max_player,list, a, b):
    if height == 3:
        return list[index]

    if max_player:
        top = low
        for i in range(0, 2):
            val = alpha_beta(height + 1, index * 2 + i, False, list, a, b)
            top = max(top, val)
            a = max(a, top)
            if b <= a:
                break
        return top

    else:
        top = high
        for i in range(0, 2):
            val = alpha_beta(height + 1, index * 2 + i, True, list, a, b)
            top = min(top, val)
            b = min(b, top)
            if b <= a:
                break
        return top



bottoms = 0
w = 0
main = input('Enter your id: ')
main = main.replace('0','8')


for i, j in enumerate(main):
    if i == 4:
        bottoms = int(j)
    if i == 3:
        w = int(j)


select = main[-1] + main[-2]
select = int(select)
topmost = int(select * 1.5)
point_list = []


for i in range(0, 8):
    point_list.append(random.randint(bottoms, topmost))
point = alpha_beta(0, 0, True, point_list, low, high)
print("Generated 8 random points between the minimum and maximum point")
print('Limits:', point_list)
print('Total points to win:', select)
print('Achieved point by applying alpha-beta pruning =', point)
if point >= select:
    print("The Winner is Optimus Prime")
else:
    print("The Winner is Megatron")


victory = 0
points = []


for i in range(w):
    point_list = []
    for j in range(0, 8):
        point_list.append(random.randint(bottoms, topmost))
    new_point = alpha_beta(0, 0, True, point_list, low, high)
    points.append(new_point)
    if new_point >= select:
        victory += 1
max_points_shuffle = points[0]
for i in points[1:]:
    if i > max_points_shuffle:
        max_points_shuffle = i


print()
print("After the shuffle")
print('List of all points list from each shuffle:', points)
print('The maximum value of all shuffles:', max_points_shuffle)
print('Won', victory, 'times out of', w, 'number of shuffles')
