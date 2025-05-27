import string

f = open('grammar.txt', 'r')
class NonTerminal:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.rules = [str]
        self.first_dependencies = [str]
        self.follow_dependencies = [str]

nont = [NonTerminal]
while 1:
    line = f.readline()
    if not(line is None or line == '' or line == string.whitespace):
        symb, rules = line.strip().split('=>')
        bigh = NonTerminal(symb)
        r = list(rules.strip().split('|'))
        bigh.rules = r
        nont.append(bigh)
    else:
        break
symbols = []
for non in nont:
    print(non.symbol)

