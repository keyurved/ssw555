#!/usr/bin/env python
from Family import Family
from Individual import Individual
from prettytable import PrettyTable

"""project2.py SSW 555-WS Project 2 GEDCOM validator"""

__author__ = "Keyur Ved, Monica Razak, Jacob Ciesieleski, Bora Bibe"

import sys 

valid_tags = { 0: ["INDI", "FAM", "HEAD", "RLR", "NOTE", "TRLR"],
               1: ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"],
               2: ["DATE"]
            }

def validate(level, tag):
    return level in valid_tags.keys() and tag in valid_tags[level]

def process_tag(level, curr_dict, tag, arg):
    if tag == 'INDI':
        curr_dict = {'INDI': arg}
    else:
        if tag == "FAMS" or tag == "FAMC" or tag == "CHIL":
            if tag == "FAMS" or tag == "FAMC":
                tag = "FAM"
            arg = [arg]

            if tag in curr_dict:
                curr_dict[tag] += arg
            else:
                curr_dict[tag] = arg
        elif arg != '':
            curr_dict[tag] = arg

def process_file(file):
    indiv_ids = set()
    fam_ids = set()
    individuals = []
    curr_indiv = {}
    families = []
    curr_fam = {}
    prev_tag = ""
    fam_process = False

    with open(file, "r") as f:
        for line in f:
            line_splt = line.split()
            line_splt = list(map(lambda x: x.strip(), line_splt))

            level = int(line_splt[0])
            tag = line_splt[1]
            arg = ""

            if len(line_splt) > 2:
                arg = ' '.join(line_splt[2:])

                if line_splt[2] == "INDI" or line_splt[2] == "FAM":
                    tag = line_splt[2]
                    arg = line_splt[1]

                    if level == 0 and tag == "FAM":
                        if curr_indiv != {}:
                            if 'INDI' in curr_indiv.keys() and curr_indiv['INDI'] not in indiv_ids:
                                individuals.append(Individual.instance_from_dict(curr_indiv))
                                indiv_ids.add(curr_indiv['INDI'])
                            else:
                                print("ERROR: INDIVIDUAL: %s: already exists" % (curr_indiv['INDI']), file=sys.stderr)
                            curr_indiv = {}
                            fam_process = True
                
            if validate(level, tag):
                if not fam_process:
                    if level == 0:
                        if curr_indiv != {}:
                            if 'INDI' in curr_indiv.keys() and curr_indiv['INDI'] not in indiv_ids:
                                individuals.append(Individual.instance_from_dict(curr_indiv))
                                indiv_ids.add(curr_indiv['INDI'])
                            else:
                                print("ERROR: INDIVIDUAL: US22: %s: already exists" % (curr_indiv['INDI']), file=sys.stderr)
                        if tag == "INDI":
                            curr_indiv = {}
                            curr_indiv = {'INDI': arg}
                        else:
                            curr_indiv = {}
                    else:
                        if tag == "BIRT" or tag == "DEAT":
                            prev_tag = tag
                        elif tag == "DATE":
                            tag = prev_tag
                            prev_tag = ""
                    process_tag(level, curr_indiv, tag, arg)
                else:
                    if level == 0 and curr_fam != {}:
                        if 'FAM' in curr_fam.keys() and curr_fam['FAM'] not in fam_ids:
                            if 'CHIL' in curr_fam.keys():
                                children = curr_fam['CHIL']
                            curr_fam['CHIL'] = []

                            for indiv in individuals:
                                if indiv.id == curr_fam['HUSB']:
                                    curr_fam['HUSB'] = indiv
                                elif indiv.id == curr_fam['WIFE']:
                                    curr_fam['WIFE'] = indiv
                                elif indiv.id in children:
                                    curr_fam['CHIL'].append(indiv)

                            families.append(Family.instance_from_dict(curr_fam))
                            fam_ids.add(curr_fam['FAM'])
                        else:
                            print("ERROR: FAMILY: US22: %s: already exists" % curr_fam['FAM'], file=sys.stderr)
                        if tag == "FAM":
                            curr_fam = {"FAM": arg}
                        else:
                            curr_fam = {}
                    else:
                        if tag == "MARR" or tag == "DIV":
                            prev_tag = tag
                        elif tag == "DATE":
                            tag = prev_tag
                            prev_tag = ""
                        process_tag(level, curr_fam, tag, arg)
                   
    return individuals, families
            
def run():
    if len(sys.argv) <= 1:
        exit("Required arg <filename> missing") 

    indivs, fams = process_file(sys.argv[1])

    indiv_table = PrettyTable()
    deceased_table = PrettyTable()
    married_table = PrettyTable()
    indiv_table.field_names = Individual.row_headers
    deceased_table.field_names = Individual.row_headers
    num_deceased = 0
    married_table.field_names = Individual.row_headers
    num_married = 0
    
    unique = set()
    for indiv in indivs:
        temp = "NAME: "+str(indiv.name) + ", Birthday: " + str(indiv.bday)
        if temp in unique:
            print("ANOMALY: US23: DUPLICATE PERSON: ", temp, file=sys.stderr)
        else:
            unique.add(temp)
        if not indiv.alive:
            deceased_table.add_row(indiv.to_row())
            num_deceased += 1
        elif len(indiv.spouses) > 0:
            married_table.add_row(indiv.to_row())
            num_married += 1
        indiv_table.add_row(indiv.to_row())
        indiv.print_errors()
        indiv.print_anomalies()

    fam_table = PrettyTable()
    fam_table.field_names = Family.row_headers

    #Error Check for Bigomy between families
    for big1Fam in fams:
        for big2Fam in fams:
            if big1Fam.id is not big2Fam.id and big1Fam.husband == big2Fam.husband and (big1Fam.div_date is None and big2Fam.div_date is None):
                big2Fam.bigError(big2Fam.husband)
            if big1Fam.id is not big2Fam.id and big1Fam.wife == big2Fam.wife and (big2Fam.div_date is None and big2Fam.div_date is None):
                big2Fam.bigError(big2Fam.wife)            

    for fam in fams:
        #Marriage Check
        fam.marriage_check()
        #
        fam_table.add_row(fam.to_row())
        fam.print_errors()
        fam.print_anomalies()

    print("ALL INDIVIDUALS")
    print(indiv_table)
    if num_deceased > 0:
        print("US29: DECEASED INDIVIDUALS")
        print(deceased_table)
    
    if num_married > 0:
        print("US30: MARRIED ALIVE INDIVIDUALS")
        print(married_table)
    print(fam_table)


if __name__ == "__main__":
    run()
