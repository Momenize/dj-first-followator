f = open('grammar.txt', 'r')
lines = f.readlines()
f.close()



class NonTerminal:
    def __init__(self, symbol):
        self.symbol = symbol
        self.rules = []
        self.first = []
        self.depen = []

class Rule:
    def __init__(self, s: str, nont: NonTerminal):
        self.s = s
        self.nont = nont
        self.nont.rules.append(self)

nonterminals = []


for line in lines:
    line = line.replace('\n', '')
    rules = []
    symbol, rule = line.split(' => ')
    nonterminal = NonTerminal(symbol)
    nonterminals.append(nonterminal)
    rules.extend(rule.split(' | '))
    for rule in rules:
        r = Rule(rule, nonterminal)

def first(nt):
    for rule in nt.rules:
        if rule.s[0].islower():
            nt.first.append(rule.s[0])
        elif rule.s[0].isupper():
            for c in rule.s:
                if c.isupper():
                    nt2 = next((n for n in nonterminals if n.symbol == c), None)
                    if nt2 not in nt.depen:
                        nt.depen.append(nt2)
                        nt.depen.extend(nt2.depen)
                        d = first(nt2)
                        nt.first.extend([x for x in d if x != 'ε'])
                        if 'ε' in d:
                            if c == rule.s[-1]:
                                nt.first.append('ε')
                            continue
                        else:
                            break
                    else:
                        if 'ε' in nt2.first:
                            continue
                        else:
                            break
                else:
                    nt.first.append(c)
                    break
        else:
            nt.first.append('ε')
    nt.first = list(set(nt.first))
    return nt.first

for nt in nonterminals:
    if len(nt.first) == 0:
        first(nt)