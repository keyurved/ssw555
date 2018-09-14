# Monica Razak
# Project 2 SSW 555
# I pledge my honor that I have abided by the Stevens Honor System

#from prettytable import PrettyTable

#x = PrettyTable()
#9
#x.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Dead", "Child", "Spouse"]

#y = PrettyTable()
#8
#y.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

GEDCOMdict = {
    'INDI': 0,
    'NAME': 1,
    'SEX': 1,
    'BIRT': 1,
    'DEAT': 1,
    'FAMC': 1,
    'FAMS': 1,
    'FAM': 0,
    'MARR': 1,
    'HUSB': 1,
    'WIFE': 1,
    'CHIL': 1,
    'DIV': 1,
    'DATE': 2,
    'HEAD': 0,
    'TRLR': 0,
    'NOTE': 0,
}

exceptions = ['INDI', 'FAM']

currLine = [];

saveLines = [];
saveAll = [];

dictSet = set(GEDCOMdict.keys());

currINDI = False

fileName = input("Enter a GEDCOM filename you would like to check: ")
gedcomFile = open(fileName, 'r');

for line in gedcomFile:

    for arg in line.split():
        currLine.append(arg)
    print("-->" + line, end="")
    print("<--", end="")
    
    if len(currLine) > 0:
        print(currLine[0] + "|", end="")
        if len(currLine) <= 2:
            if currLine[1] in exceptions:
                print(currLine[1]+"|N"+currLine[0],end=" ")
            elif str(GEDCOMdict[currLine[1]]) == currLine[0]:
                saveLines.append([currLine[1]])
                print(str(currLine[1]) + "|Y",end=" ")
            else:
                print(str(currLine[1]) + "|N",end=" ")
        else:
            if currLine[1] in exceptions:
                print(currLine[1]+"|N|", end="");
                for elem in currLine[2:]:
                    print(str(elem), end=" ")
            elif currLine[2] in exceptions:
                if str(GEDCOMdict[currLine[2]]) == currLine[0]:
                    checkKeys = set();
                    
                    for item in saveLines:
                        print(item)
                        print(item[0])
                        if item[0] in GEDCOMdict.keys():
                            checkKeys.add(item)
                    missingKeys = dictSet - checkKeys
                    if len(missingKeys) != 0:
                         for item in missingKeys:
                             saveLines.append([item])
                             saveLines.append(['N/A'])
                        
                    saveAll.append(saveLines)
                    saveLines.clear()
                    print(currLine[2]+"|Y|"+currLine[1], end="")
                    saveLines.append([currLine[2]])
                    saveLines.append([currLine[1]])
                else:
                    print(currLine[2]+"|N|"+currLine[1], end="")    
            elif currLine[1] in GEDCOMdict:
                if str(GEDCOMdict[currLine[1]]) == currLine[0]:
                    print(str(currLine[1])+"|Y|",end="")
                    saveLines.append([currLine[1]])
                    saveLines.append([currLine[2:]])
                    for elem in currLine[2:]:
                        #saveLines.append([elem])
                        print(str(elem), end=" ")
                else:
                    print(str(currLine[1])+"|N|",end="")
                    for elem in currLine[2:]:
                        print(str(elem), end=" ")
            else:
                print(str(currLine[1]) + "|N|", end="")
                for elem in currLine[2:]:
                    print(str(elem), end=" ")
    currLine.clear();
    print("");

saveAll.append(saveLines)       
print(saveAll)

