num_nonterminals = int(input('Enter the number of non-terminals: '))
class NonTerminal:
    def __init__(self, char):
        self.char = char
        self.rules = [[]]
        self.first = []
        self.follow = []
class Terminal:
    def __init__(self, char):
        self.char = char
def clown():
    print ('Wanna play games, little funny clown?')
nonterminals = []
bare_rules = [[]]
for i in range(num_nonterminals):
    nont = input('Enter your non-terminal: ')
    if nont == '' or nont.islower():
        clown()
        i -= 1
        continue
    else:
        nonterminals.append(NonTerminal(nont))
        r = int(input('Enter number of rules this non-terminal has: '))
        for j in range(r):
            rule = input(f'Enter rule {j + 1} (White space as Epsilon): ')
            if rule == '':
               clown()
               j -= 1
               continue
            else:
                bare_rules[i].append(rule)
terminals = []
for i in range(nonterminals.__len__()):
    for j in range(len(bare_rules[i])):
        for s in bare_rules[i][j]:
            if not s.isupper():
                term = Terminal(s)
                terminals.append(term)
            else:
                nonterminals[i].rules[j].append(s)

def dupremove(terminal_list):
    return list(dict.fromkeys(terminal_list))

terminals = dupremove(terminals)


class Grammar:
    def __init__(self, nonterminals: [NonTerminal], terminals: [Terminal]):
        self.nonterminals = nonterminals
        self.terminals = terminals

grammar = Grammar(nonterminals, terminals)
res = []
def first(sign):
    if sign is Terminal:
        if sign == ' ':
            res.append('epsilon')
            return res
        res.append(sign.char)
        return res
    else:
        res.append(first(lambda x: x.char == sign.char for x in nonterminals))
        return res




for nont in grammar.nonterminals:
    for rule in nont.rules:
        res.clear()
        fi = first(rule[0])
        bigh = fi.remove('epsilon')
        nont.first.append(bigh)
        if 'epsilon' in fi:
            for i in range(1, len(rule) - 1):
                if rule[i] is NonTerminal and 'epsilon' in first(rule[i]):
                    nont.first.append(first(rule[i + 1]).remove('epsilon'))
                    if i == len(rule) - 2:
                        if 'epsilon' in first(rule[i + 1]):
                            nont.first.append('epsilon')
                            continue
                else:
                    break


for nont in grammar.nonterminals:
    print(f'first({nont.char}) = {nont.first}\n')

