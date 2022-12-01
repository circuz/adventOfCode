# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:46:15 2021

@author: August
"""

def diccopy(dictionary):
    copy = {}
    for x in dictionary:
        copy[x] = dictionary[x]
    return(copy)

def dicnew(dictionary):
    copy = {}
    for x in dictionary:
        copy[x] = 0
    return(copy)

insertions = {"FO" : "K",
                "FF" : "H",
                "SN" : "C",
                "CC" : "S",
                "BB" : "V",
                "FK" : "H",
                "PC" : "P",
                "PH" : "N",
                "OB" : "O",
                "PV" : "C",
                "BH" : "B",
                "HO" : "C",
                "VF" : "H",
                "HB" : "O",
                "VO" : "N",
                "HK" : "N",
                "OF" : "V",
                "PF" : "C",
                "KS" : "H",
                "KV" : "F",
                "PO" : "B",
                "BF" : "P",
                "OO" : "B",
                "PS" : "S",
                "KC" : "P",
                "BV" : "K",
                "OC" : "B",
                "SH" : "C",
                "SF" : "P",
                "NH" : "C",
                "BS" : "C",
                "VH" : "F",
                "CH" : "S",
                "BC" : "B",
                "ON" : "K",
                "FH" : "O",
                "HN" : "O",
                "HS" : "C",
                "KK" : "V",
                "OK" : "K",
                "VC" : "H",
                "HV" : "F",
                "FS" : "H",
                "OV" : "P",
                "HF" : "F",
                "FB" : "O",
                "CK" : "O",
                "HP" : "C",
                "NN" : "V",
                "PP" : "F",
                "FC" : "O",
                "SK" : "N",
                "FN" : "K",
                "HH" : "F",
                "BP" : "O",
                "CP" : "K",
                "VV" : "S",
                "BO" : "N",
                "KN" : "S",
                "SB" : "B",
                "SC" : "H",
                "OS" : "S",
                "CF" : "K",
                "OP" : "P",
                "CO" : "C",
                "VK" : "C",
                "NB" : "K",
                "PB" : "S",
                "FV" : "B",
                "CS" : "C",
                "HC" : "P",
                "PK" : "V",
                "BK" : "P",
                "KF" : "V",
                "NS" : "P",
                "SO" : "C",
                "CV" : "P",
                "NP" : "V",
                "VB" : "F",
                "KO" : "C",
                "KP" : "F",
                "KH" : "N",
                "VN" : "S",
                "NO" : "P",
                "NF" : "K",
                "CB" : "H",
                "VS" : "V",
                "NK" : "N",
                "KB" : "C",
                "SV" : "F",
                "NC" : "H",
                "VP" : "K",
                "PN" : "H",
                "OH" : "K",
                "CN" : "N",
                "BN" : "F",
                "NV" : "K",
                "SP" : "S",
                "SS" : "K",
                "FP" : "S"}

template = "FSHBKOOPCFSFKONFNFBB"

"""
insertions = {
                "CH" : "B",
                "HH" : "N",
                "CB" : "H",
                "NH" : "C",
                "HB" : "C",
                "HC" : "B",
                "HN" : "C",
                "NN" : "C",
                "BH" : "H",
                "NC" : "B",
                "NB" : "B",
                "BN" : "B",
                "BB" : "N",
                "BC" : "B",
                "CC" : "N",
                "CN" : "C",}

template = "NNCB"
"NCNBCHB"
"""

"""
for n in range(40):
    newtemplate = []
    for i in range(len(template)-1):
        newtemplate.append(template[i])
        newtemplate.append(insertions[template[i:i+2]])
    newtemplate.append(template[i+1])
    template = "".join(newtemplate)
    print(n)

for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(c + ":" + str(template.count(c)))
"""
pairs = {}
newpairs = {}
adder = {}
created = ["",""]
for pair in insertions:
    pairs[pair] = 0
    created[0] = pair[0] + insertions[pair]
    created[1] = insertions[pair] + pair[1]
    adder[pair] = [created[0],created[1]]
 
    
for i in range(len(template)-1):
    pairs[template[i:i+2]] += 1

for __ in range(40):
    newpairs = dicnew(pairs)
    for pair in pairs:
        to_add = pairs[pair]
        add_to = adder[pair]
        newpairs[add_to[0]] += to_add
        newpairs[add_to[1]] += to_add
    pairs = diccopy(newpairs)

each = {"0":0}
for pair in pairs:
    for c in pair:
        if c in each:
            each[c] += int(pairs[pair]/2)
        else:
            each[c] = int(pairs[pair]/2)

print(each)
"""
Här kommer den coola delen:
    copy-pastea in det från each i en lista och ta max(listan)-min(listan).
    Det hade gått lätt att programmera men det gick snababre med copy-paste B-)
    tyvärr var den vi hade minst av "B", som vi slutar på. Det är ett problem
    för vi räknar allt annat två gånger och därför delar på två. Men B delar vi
    lite för mycket på två eller nåt... jag fick "41...56.5" som svar så jag
    gissade först på "41...57" men det var för högt, "41...56" var rätt!
"""