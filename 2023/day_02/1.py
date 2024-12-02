

f = open("input_real.txt", "r")
a = f.read()

a_split = a.split('\n')



still_valid = False

sum_ids = 0

for line in a_split:
    game_id = line.split(':')[0].split(' ')[1]
    conf = line.split(': ')[1]
    sets = conf.split('; ')

    for i, subset in enumerate(sets):
        count_red = 0
        count_green = 0
        count_blue = 0
        for item in subset.split(','):
            item = item.strip()
            if item.find('red') != -1:
                count_red += int(item.split(' ')[0])
            if item.find('green') != -1:
                count_green += int(item.split(' ')[0])
            if item.find('blue') != -1:
                count_blue += int(item.split(' ')[0])

        if count_red <= 12 and count_green <= 13 and count_blue <= 14:
            still_valid = True

        else:
            still_valid = False
            break

        if i == len(sets)-1 and still_valid:
            sum_ids += int(game_id)

print(sum_ids)






