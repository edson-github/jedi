def marks(code):
    if '.' in code:
        another(code[:code.index(',') - 1] + '!')
    else:
        another(f'{code}.')


def another(code2):
    call(numbers(f'{code2}haha'))

marks('start1 ')
marks('start2 ')


def alphabet(code4):
    return f'{code4}a'


def numbers(code5):
    return alphabet(f'{code5}1')


def call(code3):
    code3 = numbers(numbers('end')) + numbers(code3)
    code3.partition
