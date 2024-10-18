import spacy

n=spacy.load('en_core_web_sm')

def extract(sentence):
    doc=n(sentence)
    predicates=[]

    for token in doc:
        if token.dep_ in ['attr',['acomp']]:
            predicates.append(token.text)

    
        if token.pos_=='VERB' and token.dep_!='aux':
            predicates.append(token.lemma_)


    return sorted(set(predicates))

sentences=[
    "kinjal is a dancer."
]

for sen in sentences:
    predicates=extract(sen)
    print(f"sentences '{sen}':'{predicates}'")


