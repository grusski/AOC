
numbers_as_string = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,'nine':9}


def find_first_number(input):
    position_int = 0
    number = 0

    array_results = []
    position_string = 0
    number_string = ''

    for character in input:
        if character.isnumeric():
            number = int(character)
            break
        position_int += 1

    for item in numbers_as_string:
        position_string = input.find(item)
        if position_string == -1:
            continue
        else:
            array_results.append([position_string, numbers_as_string[item]])

        # print(array_results.sort(key=lambda x:x[1],reverse=True))

    array_results = sorted(array_results, key=lambda x: x[0], reverse=False)

    if len(array_results) == 0:
        return number
    elif position_int < array_results[0][0]:
        return number
    else:
        return array_results[0][1]





def find_last_number(input):
    position_int = 0
    number = -1

    array_results = []
    position_string = 0
    number_string = ''

    for character in reversed(input):
        if character.isnumeric():
            number = int(character)
            break
        position_int += 1
    if number == -1:
        position_int = -1


    for item in numbers_as_string:
        position_string = input.rfind(item)
        if position_string == -1:
            continue
        else:
            array_results.append([position_string, numbers_as_string[item]])

        # print(array_results.sort(key=lambda x:x[1],reverse=True))

    array_results = sorted(array_results, key=lambda x: x[0], reverse=True)



    if len(array_results) == 0:
        return number
    elif position_int == -1 or len(input) - position_int <= array_results[0][0]:
        return array_results[0][1]
    else:
        return number


f = open("input_real.txt", "r")
a = f.read()

a_split = a.split('\n')

number_temp = 0

for line in a_split:

    print(int(str(find_first_number(line)) + str(find_last_number(line))))


    number_temp += int(str(find_first_number(line)) + str(find_last_number(line)))

print()
print(number_temp)
