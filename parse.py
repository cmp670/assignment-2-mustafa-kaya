


def wordsCount(s, terms):
   
    if ' ' in s:
        splits = s.split(' ')
        return len(splits)
    else:
        return len(s)

def cyk_parser(terms, var, string, pR):
    N = wordsCount(string, terms)
 
    result = False


    table = [[[] for i in range(N)] for j in range(N)]


    cons(N, pR, string, table, var)


    constructSubs(N, pR, table, terms, var)

    lastLength = len(table[N - 1][0])
    lastVector = []



    for i in range(lastLength):
        lastVector.append((table[N - 1][0][i].token))

    if var[0] in lastVector:
        print(string+' The given sentence is not correct according to given grammar rules.')
        
        print(' ')

    else:
        print(string+' The given sentence is correct according to given grammar rules.')
      
        print(' ')


    return result

def update1(token, tokenPos, rules, variables, table):
  

    for rule in rules:
        if token == rule[1]:
            table[0][tokenPos].append(Part(token=rule[0], words=rule[1]))


def update2(rules, variables, words, table, l, s, p):
    
    for rule in rules:
        left = rule[0]  
      

        right = rule[1]

        isRight(l, left, p, right, s, table, words)


def loopOver(firstchild, firstparentLength, l, left, p, right1, right2, s, secondchild, table):
    for i in range(firstparentLength):
        if right1 ==(table[p][s][i].token):
            firstchild = table[p][s][i]
    secondparentLength = len(table[l - p - 1][s + p + 1])

    for i in range(secondparentLength):
        if right2 == (table[l - p - 1][s + p + 1][i].token):
            secondchild = table[l - p - 1][s + p + 1][i]
    if firstchild != None and secondchild != None:
        table[l][s].append(Part(token=left, firstchild=firstchild, secondchild=secondchild))

def isRight(l, left, p, right, s, table, words):
    if right not in words:
        firstchild = None
        secondchild = None
        right1 = right.split(' ')[0]
        right2 = right.split(' ')[1]

        firstparentLength = len(table[p][s])
      
        loopOver(firstchild, firstparentLength, l, left, p, right1, right2, s, secondchild, table)



class Part:
    def __init__(self, token, firstchild=None, secondchild=None, words=None):
       
        self.token = token
        self.firstchild = firstchild
        self.secondchild = secondchild
        self.words = words






def cons(N, pR, string, table, var):
    if ' ' in string:
        splits = string.split(' ')
        for s in range(1, N + 1):
            update1(splits[s - 1], s - 1, pR, var, table)
    else:
        for s in range(1, N + 1):
            update1(string[s - 1], s - 1, pR, var, table)


def constructSubs(N, pR, table, terms, var):
    for l in range(2, N + 1):  
        for s in range(1,
                       N - l + 2): 
            for p in range(1,
                           l):  
                update2(pR, var, terms, table, l - 1, s - 1, p - 1)


def main():
    global abbreviation, words, rules, checked_sentence
    if __name__ == '__main__':
        abbreviation = ["S", "NP", "VP", "Verb", "Noun", "PP", "Det", "Prep", "Adj"]
        words = ["ate", "wanted", "kissed", "washed", "pickled", "the", "a", "every", "president", "sandwich", "pickle",
                 "mouse", "floor",
                 "fine", "delicious", "beautiful", "old", "with", "on", "under", "in"]

        rules = [("S", "NP VP"), ("VP", "Verb NP"), ("NP", "Det Noun"), ("NP", "NP PP"), ("PP", "Prep NP"),
                 ("Noun", "Adj Noun"), ("Verb", "ate"), ("Verb", "wanted"),
                 ("Verb", "kissed"), ("Verb", "washed"), ("Verb", "pickled"), ("Det", "the"), ("Det", "a"),
                 ("Det", "every"), ("Noun", "president"), ("Noun", "sandwich"),
                 ("Noun", "pickle"), ("Noun", "mouse"), ("Noun", "floor"), ("Adj", "fine"), ("Adj", "delicious"),
                 ("Adj", "beautiful"), ("Adj", "old"), ("Prep", "with"),
                 ("Prep", "on"), ("Prep", "under"), ("Prep", "in")]

        f = open("sentence.txt", "r")
        f1 = f.readline()
        checked_sentence = f1



if __name__ == "__main__":
    main()
    cyk_parser(words, abbreviation, checked_sentence, rules)



