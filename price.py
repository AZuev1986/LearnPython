# -*- coding: utf-8 -*-
def format_price(price):
    int_price = int(price)
    return print('Цена: {} руб.'.format(int_price))

display_price = format_price(56.24)
