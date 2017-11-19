import pymorphy2

input_text = 'input.txt'
output_file = 'out.txt'
possw = {
    'NOUN' :  1,    # имя существительное
    'ADJF' :  2,    # имя прилагательное (полное)
    'ADJS' :  3,    # имя прилагательное (краткое)
    'COMP' :  4,    # компаратив
    'VERB' :  5,    # глагол (личная форма)
    'INFN' :  6,    # глагол (инфинитив)
    'PRTF' :  7,    # причастие (полное)
    'PRTS' :  8,    # причастие (краткое)
    'GRND' :  9,    # деепричастие
    'NUMR' :  10,   # числительное
    'ADVB' :  11,   # наречие
    'NPRO' :  12,   # местоимение-существительное
    'PRED' :  13,   # предикатив
    'PREP' :  14,   # предлог
    'CONJ' :  15,   # союз
    'PRCL' :  16,   # частица
    'INTJ' :  17,    # междометие
     None  :  18
}
symbol = {
    '!'  : '.',
    '.'  : '.',
    ','  : '',
    '?'  : '',
    ';'  : '.',
    ':'  : '',
    '('  : '',
    ')'  : '',
    '['  : '',
    ']'  : '',
    '{'  : '',
    '}'  : '',
    '"'  : '',
    '<'  : '',
    '>'  : '',
    '-'  : '',
    '@'  : '',
    '#'  : '',
    '$'  : '',
    '^'  : '',
    '&'  : '',
    '*'  : '',
    '+'  : '',
    '='  : '',
    '~'  : '',
    '/'  : '',
    '\\' : '',
    '|'  : '',
    '\n' : '',
    '«'  : '',
    '»'  : '',
    '—' : '',
    '–'  : '',
    None : '',
    '…'  : '',
    '“'  : '',
    '”'  : ''
}
morph = pymorphy2.MorphAnalyzer()


def createposfile():
    temp = ''
    infile = open(input_text, 'r')
    outfile = open(output_file, 'w')
    for char in infile.read():
        if char.isalpha():
            temp += char
        else:
            if temp != '':
                outfile.write(' ')
                outfile.write(str(possw.get(morph.parse(temp)[0].tag.POS)))
                temp = ''
            if ord(char) > 57 & ord(char) < 48:
                outfile.write(symbol.get(char, ''))

