def main():
    # multiplication_table()
    # table_miles_km()
    # power2table()
    # acronym()


def acronym(str='Random Access Memory'):
    # returns an acronym
    lst_str = str.split()
    result = ''
    for i in lst_str:
        result = result + i[0]

    return result


def multiplication_table(number=7):
    print(f'Multiplication Table for number: {number}')
    print('-' * 35)
    for i in range(1, 11):
        print('%d   x %3.d   = %3.d' % (number, i, i * number))


def table_miles_km(start=10, finish=20):
    print('Miles\tKilometers')
    print('-' * 19)
    for i in range(start, finish + 1):
        print('%d\t\t%.2f' % (i, i * 1.609))


def power2table(nr_entries=5):
    print('Number | Square')
    for i in range(1, nr_entries + 1):
        print(format(i, "6.0f"), "|", format(pow(i, 2), "6.0f"))


def print_alpha_beta_gamma():
    # https://en.wikipedia.org/wiki/List_of_Unicode_characters#Greek_and_Coptic
    print(chr(945), chr(946), chr(947))


if __name__ == '__main__':
    main()

'''
Which names can be used to name objects? Justify does which can't.
True, if it can
False, if it can't

abc = True
5peso = False           Starts with a number
_valor = True
Ernesto Costa           Contains a blank space ' '
ABC = True
with = False            'with' is a reserved word
peso$ = False           Contains a symbol other than '_'
minha_altura = True
class = False           'class' is a reserved word
nome_ALUNO = True
___1 = True
__x__ = True
import_from = True
area-rect = False       Contains a symbol other than '_'
'''
