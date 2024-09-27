import re

import_string = input()	

output = re.sub(pattern=r"(A)", repl="aa", string = import_string , count=0, flags=re.MULTILINE)
p_word_count = len(re.findall(pattern=r"\bp\w+", string = import_string, flags=re.MULTILINE))

print("Результат:\n",output)
print("Количество слов начинающихся на 'p':\n",p_word_count)