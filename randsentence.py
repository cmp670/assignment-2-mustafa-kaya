import random
from collections import OrderedDict
def yaz(g_sentence, inputfile):
    with open(inputfile, "w") as file:
        for s in g_sentence:
            file.write(s + "\n")
            
def c_sentence(r, begin):
    results = []

    def depth_first_search(root):
        
        random_rule = random.choice(r[root].split('|')).split()
        for i in random_rule:

            if i in r:
                depth_first_search(i)
                
                    
            else:
                 results.append(i)

    depth_first_search(begin)
    return " ".join( results)            

def cfg():
    
    kural = OrderedDict()
    with open("cfg.gr", "r") as file:
        lines = file.readlines()
        for l in lines:
            if l != "\n" and l[0] != "#":
                content = l.split("#")[0]
                content = content.replace("\n", "").split("\t")
                if kural.get(content[0]) == None:
                    kural[content[0]] = content[1]
                else:
                    kural[content[0]] = kural[content[0]] + "|" + content[1]
    return kural

gen_sentence = []
while(1<2):
    cumle = c_sentence(cfg(), "ROOT")
    
    if len(cumle.split()) <= 30:
        gen_sentence.append(cumle)
        
    if len(gen_sentence) >= 5:
        break
        
yaz(gen_sentence, "random-sentence.txt")
print("random-sentence.txt oluşturuldu.")