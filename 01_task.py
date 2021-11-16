import re

text = input('Ведите почту: ')
if '@'not in text or '.'not in text:
    raise Exception('Такой почты не существует')

pattern = re.compile(r'(?P<username>\w+)[@](?P<domain>\w+[.,a-z]+)')

result_iter = pattern.finditer(text)
for i in result_iter:
    print(i.groupdict())
