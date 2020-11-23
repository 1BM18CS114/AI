# Create knowledge Base

combinations=[(True,True, True),(True,True,False),
              (True,False,True),(True,False, False),
              (False,True, True),(False,True, False),
              (False, False,True),(False,False, False)] # expand this set for more variables


def tell(kb, rule):
    kb.append(rule)

def ask(kb, q):
    print('kb  ', 'q')
    for comb in combinations:
                
        s = all(rule(comb) for rule in kb)
        f = q(comb)

        print(s, f)

        if s != f and s != False:
            return 'Does not entail' 
        
    return 'Entails '

# r1 = lambda x: x[0] or x[1] and (x[0] and x[1])
r2 = lambda x: (x[0] or x[1]) and x[2]

#q = lambda x: x[0] and x[1] and (x[0] or x[1])
q = lambda x: x[0] or x[1] and (x[0] and x[1])



### Does not Entail
# (x ^ y) v z
r1 = lambda x: (x[0] and x[1]) or x[2]
# ~y v ~z
r2 = lambda x: not x[1] or not x[2]


# ~ z
q = lambda x: not x[2] 

# Knowledgebase Array
kb = []

# Tell Rules
tell(kb, r1)
tell(kb, r2)

# Ask Queries
#print(ask(kb, q))


### Entails
r1 = lambda x: x[0] or x[1] and (x[0] and x[1])
r2 = lambda x: (x[0] or x[1]) and x[2]


q = lambda x: x[0] or x[1] and (x[0] and x[1])

# Knowledgebase Array
kb = []

# Tell Rules
tell(kb, r1)
tell(kb, r2)

# Ask Queries
print(ask(kb, q))

