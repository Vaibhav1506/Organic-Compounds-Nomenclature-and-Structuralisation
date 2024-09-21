import re
import csv
def root_word(x):
    D1 = {"methh": 1, "ethh": 2, "propp": 3, "butt": 4, "pentt": 5, "hexa": 6, "heptt": 7, "octt": 8, "nonn": 9, "decc": 10}
    D2 = {"hen": 1, "do": 2, "tria": 3, "tetra": 4, "penta": 5, "hexa": 6, "hepta": 7, "octa": 8, "nona": 9}

    L1 = []

    num = x
    st = str(num)
    L = []

    for i in st:
        i = int(i)
        L.append(i)

    L.reverse()
    ln = len(L)
    C = 0

    for j in range(ln):
        a = pow(10, C)
        L[j] = L[j] * a
        C += 1

    if ln == 1:
        for i in D1:
            for k in L:
                if k == D1[i]:
                    L1.append(i)
    
    else:
        for i in L:
            if num == 11:
                L1.append("undeca")
                break
            elif 0 < i < 10:
                for j in D2:
                    if i == D2[j]:
                        L1.append(j)
            elif i == 10:
                L1.append("deca")
            elif 11 < i < 20:
                for j in D2:
                    if i == D2[j]:
                        L1.append(j + "deca")
            elif i == 20:
                L1.append("icosa")
            elif 30 <= i < 100:
                for j in D2:
                    if str(D2[j]) in str(i):
                        L1.append(j + "conta")
            elif i == 100:
                L1.append("hecta")
            elif i == 200:
                L1.append("dicta")
            elif i == 300:
                L1.append("tricta")
            elif 400 <= i < 1000:
                for j in D2:
                    if str(D2[j]) in str(i):
                        L1.append(j + "cta")
            elif i == 1000:
                L1.append("killia")
            elif i == 2000:
                L1.append("dillia")
            elif i == 3000:
                L1.append("trilia")
            elif 4000 <= i <= 9999:
                for j in D2:
                    if str(D2[j]) in str(i):
                        L1.append(j + "lia")
            elif i == 10000:
                L1.append("decalia")

    if L1[0] == "hen" and L1[1] == "deca":
        L1[0] = "undeca"
        L1.pop(1)

    st = ''.join(L1)
    return st


print("-" * len("NOTE: THE FOLLOWING FUNCTIONAL GROUPS ARE ONLY SUPPORTED: "))
print("NOTE: THE FOLLOWING FUNCTIONAL GROUPS ARE ONLY SUPPORTED: ")
print("1. Alkanes")
print("2. Alkenes")
print("3. Alkynes")
print("4. Alcohols")
print("5. Aldehydes")
print("6. Ketones")
print("7. Carboxylic Acids")
print("8. Cyanides")
print("9. Amides")
print("10. Haloalkanes")
print("-" * len("NOTE: THE FOLLOWING FUNCTIONAL GROUPS ARE ONLY SUPPORTED: "))


print("1. Get name of an organic compound from formula (only straight chains supported)")
print("2. Get formula of an organic compound from I.U.P.A.C name (only straight chains supported)")

choice = int(input("Enter your choice:"))

if choice == 1:
    print("Syntax for compound formula: No. of Carbon atoms + No. of Hydrogen atoms + Functional Grp(if any)")
    print("WHERE :-")
    print("No. of Carbon atoms ---> E.g: C5, C10, C456, etc.")
    print("No. of Hydrogen atoms ---> E.g: H5, H10, H456, etc. and has to be an indirect/direct multiple of No. of carbon atoms depending upon the Functional Group and in all cases.")

    com = input("Enter compound formula (Carbon range: 1 - 10999): ")

    l_num = re.findall(r'\d+', com)

    for i in range(0, len(l_num)):
        l_num[i] = int(l_num[i])

    if l_num[0] <= 10999:
        
        if "COOH" in com:
            if "HCOOH" == com:
                print("Compound Name: Methanoic acid.")
            com.replace("COOH", "")
            if l_num[1] == (2 * l_num[0]) + 1:
                RW = root_word(int(l_num[0]) + 1)
                LF = list(RW)
                LF[-1] = "anoic acid"
                RW = ''.join(LF)
                print("Compound Name:", RW.capitalize())
                print("Functional group: Carboxyl")
            else:
                print("Compound doesn't exist.")

        elif "COCH3" in com:
            com.replace("COCH3", "")
            if l_num[1] == (2 * l_num[0]) + 1:
                RW = root_word(int(l_num[0]) + 2)
                LF = list(RW)
                LF[-1] = "anone"
                RW = ''.join(LF)
                print("Compound Name:", RW.capitalize())
                print("Functional group: Keto")
            else:
                print("Compound doesn't exist.")

        elif "OH" in com:
            com.replace("OH", "")
            if l_num[1] == (2 * l_num[0]) + 1:
                RW = root_word(l_num[0])
                LF = list(RW)
                LF[-1] = "anol"
                RW = ''.join(LF)
                print("Compound Name:", RW.capitalize())
                print("Functional group: Hydroxyl")
            else:
                print("Compound doesn't exist.")

        elif "CHO" in com:
            com.replace("CHO", "")
            if l_num[1] == (2 * l_num[0]) + 1:
                RW = root_word(int(l_num[0]) + 1)
                LF = list(RW)
                LF[-1] = "anal"
                RW = ''.join(LF)
                print("Compound Name:", RW)
            else:
                print("Compound doesn't exist.")

        elif "CN" in com:
            if "HCN" == com:
                print("Compound Name: Methanenitrile.")
                print("Functional group: Cyano")

            else:
                com.replace("CHO", "")
                if l_num[1] == (2 * l_num[0]) + 1:
                    RW = root_word(int(l_num[0]) + 1)
                    LF = list(RW)
                    LF[-1] = "anenitrile"
                    RW = ''.join(LF)
                    print("Compound Name:", RW)
                    print("Functional group: Cyano")
                else:
                    print("Compound doesn't exist.")

        elif "CONH2" in com:
            if "HCONH2" == com:
                print("Compound Name: Methanamide.")
                print("Functional group: Amide")

            else:
                com.replace("CHO", "")
                if l_num[1] == (2 * l_num[0]) + 1:
                    RW = root_word(int(l_num[0]) + 1)
                    LF = list(RW)
                    LF[-1] = "anamide"
                    RW = ''.join(LF)
                    print("Compound Name:", RW)
                    print("Functional group: Amide")
                else:
                    print("Compound doesn't exist.")

        elif "Cl" or "I" or "F" or "Br" not in com:
            if l_num[1] == (2 * l_num[0]) + 2:
                RW = root_word(l_num[0])
                LF = list(RW)
                LF[-1] = "ane"
                RW = ''.join(LF)
                print("Compound Name:", RW)
                print("Functional group: Alkane")
            elif l_num[1] == 2 * l_num[0]:
                RW = root_word(l_num[0])
                LF = list(RW)
                LF[-1] = "ene"
                RW = ''.join(LF)
                print("Compound Name:", RW)
                print("Functional group: Alkene")
            elif l_num[1] == (2 * l_num[0]) - 2:
                RW = root_word(l_num[0])
                LF = list(RW)
                LF[-1] = "yne"
                RW = ''.join(LF)
                print("Compound Name:", RW)
                print("Functional group: Alkyne")
            else:
                print("Compound doesn't exist.")

    else:
        print("Out of range.")

elif choice == 2:
    print("Syntax for IUPAC name: Hexanone, Ethanal, Propanol,etc.")
    print("\n")
    com = input("Enter I.U.P.A.C. name of compound (Carbon Range : 1 - 100): ")
    com = com.lower()

    Nomenclature = {
        "meth": [1, 'C'],
        "eth": [2, 'C\u2082'],
        "prop": [3, 'C\u2083'],
        "but": [4, 'C\u2084'],
        "pent": [5, 'C\u2085'],
        "hex": [6, 'C\u2086'],
        "hept": [7, 'C\u2087'],
        "oct": [8, 'C\u2088'],
        "non": [9, 'C\u2089'],
        "dec": [10, 'C\u2081\u2080'],
        "undec": [11, 'C\u2081\u2081'],
        "dodec": [12, 'C\u2081\u2082'],
        "tridec": [13, 'C\u2081\u2083'],
        "tetradec": [14, 'C\u2081\u2084'],
        "pentadec": [15, 'C\u2081\u2085'],
        "hexadec": [16, 'C\u2081\u2086'],
        "heptadec": [17, 'C\u2081\u2087'],
        "octadec": [18, 'C\u2081\u2088'],
        "nonadec": [19, 'C\u2081\u2089'],
        "icos": [20, 'C\u2082\u2080'],
        "henicos": [21, 'C\u2082\u2081'],
        "docos": [22, 'C\u2082\u2082'],
        "tricos": [23, 'C\u2082\u2083'],
        "tetracos": [24, 'C\u2082\u2084'],
        "pentacos": [25, 'C\u2082\u2085'],
        "hexacos": [26, 'C\u2082\u2086'],
        "heptacos": [27, 'C\u2082\u2087'],
        "octacos": [28, 'C\u2082\u2088'],
        "nonacos": [29, 'C\u2082\u2089'],
        "triacont": [30, 'C\u2083\u2080'],
        "hentriacont": [31, 'C\u2083\u2081'],
        "dotriacont": [32, 'C\u2083\u2082'],
        "tritriacont": [33, 'C\u2083\u2083'],
        "tetratriacont": [34, 'C\u2083\u2084'],
        "pentatriacont": [35, 'C\u2083\u2085'],
        "hexatriacont": [36, 'C\u2083\u2086'],
        "heptatriacont": [37, 'C\u2083\u2087'],
        "octatriacont": [38, 'C\u2083\u2088'],
        "nonatriacont": [39, 'C\u2083\u2089'],
        "tetracont": [40, 'C\u2084\u2080'],
        "hentetracont": [41, 'C\u2084\u2081'],
        "dotetracont": [42, 'C\u2084\u2082'],
        "tritetracont": [43, 'C\u2084\u2083'],
        "tetratetracont": [44, 'C\u2084\u2084'],
        "pentatetracont": [45, 'C\u2084\u2085'],
        "hexatetracont": [46, 'C\u2084\u2086'],
        "heptatetracont": [47, 'C\u2084\u2087'],
        "octatetracont": [48, 'C\u2084\u2088'],
        "nonatetracont": [49, 'C\u2084\u2089'],
        "pentacont": [50, 'C\u2085\u2080'],
        "henpentacont": [51, 'C\u2085\u2081'],
        "dopentacont": [52, 'C\u2085\u2082'],
        "tripentacont": [53, 'C\u2085\u2083'],
        "tetrapentacont": [54, 'C\u2085\u2084'],
        "pentapentacont": [55, 'C\u2085\u2085'],
        "hexapentacont": [56, 'C\u2085\u2086'],
        "heptapentacont": [57, 'C\u2085\u2087'],
        "octapentacont": [58, 'C\u2085\u2088'],
        "nonapentacont": [59, 'C\u2085\u2089'],
        "hexacont": [60, 'C\u2086\u2080'],
        "henhexacont": [61, 'C\u2086\u2081'],
        "dohexacont": [62, 'C\u2086\u2082'],
        "trihexacont": [63, 'C\u2086\u2083'],
        "tetrahexacont": [64, 'C\u2086\u2084'],
        "pentahexacont": [65, 'C\u2086\u2085'],
        "hexahexacont": [66, 'C\u2086\u2086'],
        "heptahexacont": [67, 'C\u2086\u2087'],
        "octahexacont": [68, 'C\u2086\u2088'],
        "nonahexacont": [69, 'C\u2086\u2089'],
        "heptacont": [70, 'C\u2087\u2080'],
        "henheptacont": [71, 'C\u2087\u2081'],
        "doheptacont": [72, 'C\u2087\u2082'],
        "triheptacont": [73, 'C\u2087\u2083'],
        "tetraheptacont": [74, 'C\u2087\u2084'],
        "pentaheptacont": [75, 'C\u2087\u2085'],
        "hexaheptacont": [76, 'C\u2087\u2086'],
        "heptaheptacont": [77, 'C\u2087\u2087'],
        "octaheptacont": [78, 'C\u2087\u2088'],
        "nonaheptacont": [79, 'C\u2087\u2089'],
        "octacont": [80, 'C\u2088\u2080'],
        "henoctacont": [81, 'C\u2088\u2081'],
        "dooctacont": [82, 'C\u2088\u2082'],
        "trioctacont": [83, 'C\u2088\u2083'],
        "tetraoctacont": [84, 'C\u2088\u2084'],
        "pentaoctacont": [85, 'C\u2088\u2085'],
        "hexaoctacont": [86, 'C\u2088\u2086'],
        "heptaoctacont": [87, 'C\u2088\u2087'],
        "octaoctacont": [88, 'C\u2088\u2088'],
        "nonaoctacont": [89, 'C\u2088\u2089'],
        "nonacont": [90, 'C\u2089\u2080'],
        "hennonacont": [91, 'C\u2089\u2081'],
        "dononacont": [92, 'C\u2089\u2082'],
        "trinonacont": [93, 'C\u2089\u2083'],
        "tetranonacont": [94, 'C\u2089\u2084'],
        "pentanonacont": [95, 'C\u2089\u2085'],
        "hexanonacont": [96, 'C\u2089\u2086'],
        "heptanonacont": [97, 'C\u2089\u2087'],
        "octanonacont": [98, 'C\u2089\u2088'],
        "nonanonacont": [99, 'C\u2089\u2089'],
        "hect": [100, 'C\u2081\u2080\u2080'],
    }


    def get_sub(x):  # convert int to subscript
        org = "0123456789"
        sub = "₀₁₂₃₄₅₆₇₈₉"
        fin_res = x.maketrans(org, sub)
        return x.translate(fin_res)


    def alkane(x):  # CH4, C2H6
        L1 = list(x.partition("ane"))
        L1.pop(2)
        for i in Nomenclature:
            if L1[0] == i:
                a = (2 * (Nomenclature[i][0])) + 2
                H = 'H{}'.format(get_sub(str(a)))
                C = Nomenclature[i][1]
                print("Type of compound: Alkane")
                print("Formula: ", C + H)
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L1[0] == "meth":
                print("C — H\u2084")
            else:
                for i in Nomenclature:
                    if L1[0] == i:
                        st = ""
                        a = Nomenclature[i][0] - 2
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "CH\u2083")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "—CH\u2083")
        elif ch == 2:
            for i in Nomenclature:
                if L1[0] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H, end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(" + j.capitalize() + "ane)")


    def alkene(x):  # C2H4, C3H6
        L2 = list(x.partition("ene"))
        L2.pop(2)

        if "methene" == x:
            print("Compound doesn't exist.")
        else:
            for i in Nomenclature:
                if L2[0] == i:
                    a = (2 * (Nomenclature[i][0]))
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Alkene")
                    print("Formula :", C + H)
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L2[0] == "eth":
                print("CH\u2082 = CH\u2082")
            else:
                for i in Nomenclature:
                    if L2[0] == i:
                        st = ""
                        a = Nomenclature[i][0] - 3
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "CH = CH\u2082")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "—CH\u2083")
        elif ch == 2:
            for i in Nomenclature:
                if L2[0] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H, end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(" + j.capitalize() + "ene)")


    def alkyne(x):  # C2H2, C3H4
        L3 = list(x.partition("yne"))
        L3.pop(2)

        if "methyne" == x:
            print("Compound doesn't exist.")
        else:
            for i in Nomenclature:
                if L3[0] == i:
                    a = (2 * (Nomenclature[i][0])) - 2
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Alkyne")
                    print("Formula :", C + H)
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L3[0] == "eth":
                print("CH ≡ CH")
            else:
                for i in Nomenclature:
                    if L3[0] == i:
                        st = ""
                        a = Nomenclature[i][0] - 3
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "C ≡ CH")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "C ≡ CH")
        elif ch == 2:
            for i in Nomenclature:
                if L3[0] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H, end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(" + j.capitalize() + "yne)")


    def alkyl(x):  # CH3 , C2H5
        L4 = list(x.partition("yl"))
        L4.pop(2)

        for i in Nomenclature:
            if L4[0] == i:
                a = (2 * (Nomenclature[i][0])) + 1
                H = 'H{}'.format(get_sub(str(a)))
                C = Nomenclature[i][1]
                print("Alkyl group detected.")
                print("Group is written as ", "—" + C + H)


    def alcohol(x):  # CH4O, C2H6O
        L5 = list(x.partition("anol"))
        L5.pop(2)

        for i in Nomenclature:
            if L5[0] == i:
                a = (2 * (Nomenclature[i][0])) + 2
                H = 'H{}'.format(get_sub(str(a)))
                C = Nomenclature[i][1]
                print("Type of compound: Alcohol")
                print("Formula :", C + H + "O")
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L5[0] == "meth":
                print("CH\u2083—OH")
            else:
                for i in Nomenclature:
                    if L5[0] == i:
                        st = ""
                        a = Nomenclature[i][0] - 1
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "OH")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "OH")
        elif ch == 2:
            for i in Nomenclature:
                if L5[0] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H + "O", end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(" + j.capitalize() + "anol)")


    def aldehyde(x):  # CH2O , C2H4O
        L6 = list(x.partition("anal"))
        L6.pop(2)

        if x == "methanal":
            print("Formula: CH\u2082O")
        else:
            for i in Nomenclature:
                if L6[0] == i:
                    a = (2 * Nomenclature[i][0])
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Formula: ", C + H + "O")
                    print("Type of compound: Aldehyde")
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L6[0] == "meth":
                print("H — CHO")
            elif L6[0] == "eth":
                print("CH\u2083 — CHO")
            else:
                for i in Nomenclature:
                    if L6[0] == i:
                        st = ""
                        a = Nomenclature[i][0] - 2
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "CHO")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "CHO")
        elif ch == 2:
            for i in Nomenclature:
                if L6[0] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H + "O", end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(" + j.capitalize() + "anal)")


    def ketone(x):  # C3H6O, C4H8O
        L7 = list(x.partition("anone"))
        L7.pop(2)

        if x == "methanone" or x == "ethanone":
            print("Compound do not exist")
        else:
            for i in Nomenclature:
                if L7[0] == i:
                    a = (2 * (Nomenclature[i][0]))
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Ketone")
                    print("Formula :", C + H + "O")
            print("1. Display the expanded formula?")
            print("2. Display the next compound in homologue series?")
            ch = int(input("Enter choice: "))
            if ch == 1:
                if com.isalpha() == True:
                    if L7[0] == "prop":
                        c = "CH\u2083— CO —CH\u2083"
                    else:
                        for i in Nomenclature:
                            if L7[0] == i:
                                st = ""
                                a = Nomenclature[i][0] - 3
                                if a <= 5:
                                    for j in range(a):
                                        st += "CH\u2082"
                                        st += "—"
                                    print("CH\u2083—" + st + "CO—CH\u2083")
                                else:
                                    print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "CO—CH\u2083")
            elif ch == 2:
                for i in Nomenclature:
                    if L7[0] == i:
                        a += 2
                        H = 'H{}'.format(get_sub(str(a)))
                        b = Nomenclature[i][0] + 1
                        C = 'C{}'.format(get_sub(str(b)))
                print("Next Compound Formula: ", C + H + "O", end="")
                for j in Nomenclature:
                    if C == Nomenclature[j][1]:
                        print("(" + j.capitalize() + "anone)")


    def carboxylic(x):  # CH2O2,C2H4O2
        L8 = list(x.partition("anoic acid"))
        L8.pop(2)

        if "methanoic acid" == x:
            print("CH\u2082O\u2082")
        else:
            for i in Nomenclature:
                if L8[0] == i:
                    a = (2 * (Nomenclature[i][0]))
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Carboxylic Acid")
                    print("Formula :", C + H + "O\u2082")
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L8[0] == "meth":
                print("H — COOH")
            else:
                for i in Nomenclature:
                    if L8[0] == i:
                        st = ""
                        a = Nomenclature[i][0] - 2
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "COOH")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "COOH")
        elif ch == 2:
            for i in Nomenclature:
                if L8[0] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H + "O\u2082", end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(" + j.capitalize() + "anoic acid)")


    def cyanide(x):
        L9 = list(x.partition("anenitrile"))
        L9.pop(2)

        if x == "methanenitrile":
            print("Cyano group detected.")
            print("Formula: CHN")

        else:
            for i in Nomenclature:
                if L9[0] == i:
                    a = (2 * (Nomenclature[i][0])) - 1
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Cyanide")
                    print("Formula :", C + H + "N")
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L9[0] == "meth":
                print("H — CN")
            elif L9[0] == "eth":
                print("CH\u2083 — CN")
            else:
                for i in Nomenclature:
                    if L9[0] == i:
                        st = ""
                        a = Nomenclature[i][0] - 2
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "CN")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "CN")
        elif ch == 2:
            for i in Nomenclature:
                if L9[0] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H + "N", end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(" + j.capitalize() + "anenitrile)")


    def amide(x):
        L10 = list(x.partition("anamide"))
        L10.pop(2)

        if x == "methanamide":
            print("CH\u2083NO")

        else:
            for i in Nomenclature:
                if L10[0] == i:
                    a = (2 * (Nomenclature[i][0])) + 1
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Amide")
                    print("Formula :", C + H + "NO")
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L10[0] == "meth":
                print("H — CO — NH\u2082")
            elif L10[0] == "eth":
                print("CH\u2083 — CO — NH\u2082")
            else:
                for i in Nomenclature:
                    if L10[0] == i:
                        st = ""
                        a = Nomenclature[i][0] - 2
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "CO — NH\u2082")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "CO — NH\u2082")
        elif ch == 2:
            for i in Nomenclature:
                if L10[0] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H + "NO", end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(" + j.capitalize() + "anamide)")


    def fluoroalkane(x):
        if "ene" in x or "yne" in x:
            print("Compound does not exist.")

        elif "fluoro" in x:
            L11 = list(x.partition("fluoro"))
            L11.pop(0)
            L11[1] = L11[1].replace("ane", "")

            for i in Nomenclature:
                if L11[1] == i:
                    a = (2 * (Nomenclature[i][0])) + 1
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Haloalkane")
                    print("Formula :", C + H + "F")

        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L11[1] == "meth":
                print("CH\u2083 — F")
            else:
                for i in Nomenclature:
                    if L11[1] == i:
                        st = ""
                        a = Nomenclature[i][0] - 1
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "F")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "F")
        elif ch == 2:
            for i in Nomenclature:
                if L11[1] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H + "F", end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(fluoro" + j + "ane)")


    def chloroalkane(x):
        if "ene" in x or "yne" in x:
            print("Compound does not exist.")

        elif "chloro" in x:
            L12 = list(x.partition("chloro"))
            L12.pop(0)
            L12[1] = L12[1].replace("ane", "")

            for i in Nomenclature:
                if L12[1] == i:
                    a = (2 * (Nomenclature[i][0])) + 1
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Haloalkane")
                    print("Formula :", C + H + "Cl")
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L12[1] == "meth":
                print("CH\u2083 — Cl")
            else:
                for i in Nomenclature:
                    if L12[1] == i:
                        st = ""
                        a = Nomenclature[i][0] - 1
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "Cl")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "Cl")
        elif ch == 2:
            for i in Nomenclature:
                if L12[1] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H + "Cl", end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(chloro" + j + "ane)")


    def bromoalkane(x):
        if "ene" in x or "yne" in x:
            print("Compound does not exist.")

        elif "bromo" in x:
            L13 = list(x.partition("bromo"))
            L13.pop(0)
            L13[1] = L13[1].replace("ane", "")

            for i in Nomenclature:
                if L13[1] == i:
                    a = (2 * (Nomenclature[i][0])) + 1
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Haloalkane")
                    print("Formula :", C + H + "Br")
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L13[1] == "meth":
                print("CH\u2083 — Cl")
            else:
                for i in Nomenclature:
                    if L13[1] == i:
                        st = ""
                        a = Nomenclature[i][0] - 1
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "Br")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "Br")
        elif ch == 2:
            for i in Nomenclature:
                if L13[1] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H + "Br", end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(bromo" + j + "ane)")


    def iodoalkane(x):
        if "ene" in x or "yne" in x:
            print("Compound does not exist.")

        elif "iodo" in x:
            L14 = list(x.partition("iodo"))
            L14.pop(0)
            L14[1] = L14[1].replace("ane", "")

            for i in Nomenclature:
                if L14[1] == i:
                    a = (2 * (Nomenclature[i][0])) + 1
                    H = 'H{}'.format(get_sub(str(a)))
                    C = Nomenclature[i][1]
                    print("Type of compound: Haloalkane")
                    print("Formula :", C + H + "I")
        print("1. Display the expanded formula?")
        print("2. Display the next compound in homologue series?")
        ch = int(input("Enter choice: "))
        if ch == 1:
            if L14[1] == "meth":
                print("CH\u2083 — Cl")
            else:
                for i in Nomenclature:
                    if L14[1] == i:
                        st = ""
                        a = Nomenclature[i][0] - 1
                        if a <= 5:
                            for j in range(a):
                                st += "CH\u2082"
                                st += "—"
                            print("CH\u2083—" + st + "Cl")
                        else:
                            print("CH\u2083—" + "(CH\u2082)" + get_sub(str(a)) + "Cl")
        elif ch == 2:
            for i in Nomenclature:
                if L14[1] == i:
                    a += 2
                    H = 'H{}'.format(get_sub(str(a)))
                    b = Nomenclature[i][0] + 1
                    C = 'C{}'.format(get_sub(str(b)))
            print("Next Compound Formula: ", C + H + "Cl", end="")
            for j in Nomenclature:
                if C == Nomenclature[j][1]:
                    print("(iodo" + j + "ane)")


    # Halides
    if "fluoro" in com:
        fluoroalkane(com)

    elif "chloro" in com:
        chloroalkane(com)

    elif "bromo" in com:
        bromoalkane(com)

    elif "iodo" in com:
        iodoalkane(com)

    # Cyanide
    elif "anenitrile" in com:
        cyanide(com)

    # Alkane
    elif "ane" in com:
        alkane(com)

    # Alkene
    elif "ene" in com:
        alkene(com)

    # Alkyne
    elif "yne" in com:
        alkyne(com)

    # Alkyl
    elif "yl" in com:
        alkyl(com)

    # Alcohol
    elif "anol" in com:
        alcohol(com)

    # Aldehyde
    elif "anal" in com:
        aldehyde(com)

    # Ketone
    elif "anone" in com:
        ketone(com)

    # Carboxylic Acid
    elif "anoic acid" in com:
        carboxylic(com)

    # Amide
    elif "anamide" in com:
        amide(com)

    else:
        print("Compound not found in database or out of range.")
else:
    print("Enter correct choice.")
