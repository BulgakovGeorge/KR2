import re

input_string = input()

sample = r"^#[ABCDEFabcdef|0-9]{6}$"
reg_form = re.findall(pattern = sample, string = input_string)

if reg_form:
    print("Была найдена строка с шестнадцатиричным идентификатором цвета в HTML -",''.join(reg_form))
else:
    print("Данная строка не является шестнадцатиричным идентификатором цвета в HTML")