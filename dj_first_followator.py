f = open('grammar.txt', 'r')
lines = f.readlines()
f.close()



class NonTerminal:
    def __init__(self, symbol):
        self.symbol = symbol
        self.rules = []
        self.first = []
        self.firstdepen = []
        self.followdepen = []
        self.follow = []
        self.followupd = False

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
nonterminals[0].follow.append('$')
def first(nt):
    for rule in nt.rules:
        if rule.s[0].islower():
            nt.first.append(rule.s[0])
        elif rule.s[0].isupper():
            for c in rule.s:
                if c.isupper():
                    nt2 = next((n for n in nonterminals if n.symbol == c), None)
                    if nt2 not in nt.firstdepen:
                        nt.firstdepen.append(nt2)
                        nt.firstdepen.extend(nt2.firstdepen)
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


def follow():
    for nt in nonterminals:
        for rule in nt.rules:
            for j in range(len(rule.s)):
                if rule.s[j].isupper():
                    nt2 = next(n for n in nonterminals if n.symbol == rule.s[j])
                    if j == len(rule.s) - 1:
                        nt2.followdepen.append(nt)
                        if 'ε' in nt2.first:
                            for k in range(j - 1, 0):
                                if rule.s[k].isupper():
                                    nt4 = next(n for n in nonterminals if n.symbol == rule.s[k])
                                    nt4.followdepen.append(nt)
                                else: break
                        continue
                    else:
                        for c in range(j + 1, len(rule.s)):
                            if rule.s[c].isupper():
                                nt3 = next(n for n in nonterminals if n.symbol == rule.s[c])
                                nt2.follow.extend([bigh for bigh in nt3.first if bigh != 'ε'])
                                if 'ε' in nt3.first:
                                    continue
                                else:
                                    break
                            else:
                                nt2.follow.append(rule.s[c])
                                break
    for i in range(2):
        for nt in nonterminals:
            for depen in nt.followdepen:
                nt.follow.extend(depen.follow)
    for nt in nonterminals:
        nt.follow = list(set(nt.follow))

follow()

for nt in nonterminals:
    print(f'First({nt.symbol}): ', '{', end='')
    for i in range(len(nt.first)):
        print(f' {nt.first[i]}', end='')
        if i != len(nt.first) - 1:
            print(',', end='')
        else:
            print(' }')

print('\n\n')
for nt in nonterminals:
    print(f'Follow({nt.symbol}): ', '{', end='')
    for i in range(len(nt.follow)):
        print(f' {nt.follow[i]}', end='')
        if i != len(nt.follow) - 1:
            print(',', end='')
        else:
            print(' }')