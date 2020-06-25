import random as r

role =[]
taste = ['嘗起來','味道']
adverb = ['蠻','有夠','稍微']
adj = ['好ㄘ','難ㄘ','普通','噁爛']


role.append(input("請輸入食物 : "))

def S():
    return  ROLE() + '這東西' + TASTE() + ADVERB() + ADJ()

def ROLE():
    return r.choice(role)

def TASTE():
    return r.choice(look)

def ADVERB():
    return r.choice(adverb)

def ADJ():
    return r.choice(adj)


print(S())
