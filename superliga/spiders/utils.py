# from 'sábado, 5 de novembro de 2022 - 21:30' to 2022-11-05

import locale
from datetime import datetime

def parse_ptbr_date(str):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    str_1 = str.replace(' de ', '-')
    str_2 = str_1.replace(' ', '')
    str_3 = str_2.split(',', 1)[1]
    str_4 = str_3.rsplit('-', 1)[0]

    parsed_date = datetime.strptime(str_4, '%d-%B-%Y').date()

    return parsed_date