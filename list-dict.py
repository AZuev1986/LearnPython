# -*- coding: utf-8 -*-
'''list = [2, 3, 4, 5, 6, 7]
print(list)
list.append('Python')
print(len(list))'''
dict_city = {"city": "Москва", "temperature": "20"}
print(dict_city['city'])
dict_city['temperature'] = int(dict_city['temperature']) - 5
print(dict_city)
print(dict_city.get('country'))
print(dict_city.get('country', 'Россия'))
dict_city['date'] = '27.05.2017'
print(len(dict_city))
