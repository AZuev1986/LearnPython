'''list = [2, 3, 4, 5, 6, 7]
print(list)
list.append('Python')
print(len(list))'''

dict = {"city": "Москва", "temperature": "20"}
print(dict['city'])
dict['temperature'] = int(dict['temperature']) - 5
print(dict)
print(dict.get('country'))
print(dict.get('country', 'Россия'))
dict['date'] = '27.05.2017'
print(len(dict))
