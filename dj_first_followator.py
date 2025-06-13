f = open('grammar.txt', 'r')
lines = f.readlines()
f.close()



class NonTerminal:
    def __init__(self, symbol):
        self.symbol = symbol
        self.rules = []

class Rule:
    def __init__(self, s: str, nont: NonTerminal):
        self.s = s
        self.nont = nont
        self.nont.rules.append(self)

nonterminals = []


for line in lines:
    rules = []
    symbol, rule = line.split(' => ')
    nonterminal = NonTerminal(symbol)
    nonterminals.append(nonterminal)
    rules.extend(rule.split(' | '))
    for rule in rules:
        r = Rule(rule, nonterminal)