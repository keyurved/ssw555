import unittest
from Family import Family
from Individual import Individual

class MarriageOfAuntUncle(unittest.TestCase):

    def test_valid_marriages(self):
        #Grandpa
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0',
                'CHIL': ['I2','I3'],
                }
        #Grandma
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0',
                'CHIL': ['I2','I3'],
                }
        #Aunt
        p3_dict = { 'INDI': 'I2',
                'NAME': 'Pperson /One',
                'SEX': 'F',
                'BIRT':'23 Apr 2000',
                'FAM': 'F0'
                }
        #Dad
        p4_dict = { 'INDI': 'I3',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p5_dict = {'INDI': 'I4',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Nephiew
        p6_dict = {'INDI': 'I5',
                'NAME' : 'Person /Three',
                'SEX': 'M',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        aunt = Individual.instance_from_dict(p3_dict)
        dad = Individual.instance_from_dict(p4_dict)
        mom = Individual.instance_from_dict(p5_dict)
        nephiew = Individual.instance_from_dict(p6_dict)
        fam_dict = { 'FAM': 'F0',
                'HUSB': grandpa,
                'WIFE': grandma,
                'MARR': '15 Mar 1994',
                'CHIL': [aunt,dad],
        }
        fam_dict2 = { 'FAM': 'F1',
                'HUSB': dad,
                'WIFE': mom,
                'MARR': '16 Aug 2024',
                'CHIL': [nephiew],
        }

        self.assertFalse(Family.instance_from_dict(fam_dict).anomalies)
    
    def test_marriage_invalid(self):
        #Grandpa
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0',
                'CHIL': ['I2','I3'],
                }
        #Grandma
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0',
                'CHIL': ['I2','I3'],
                }
        #Aunt
        p3_dict = { 'INDI': 'I2',
                'NAME': 'Pperson /One',
                'SEX': 'F',
                'BIRT':'23 Apr 2000',
                'FAM': 'F0'
                }
        #Dad
        p4_dict = { 'INDI': 'I3',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p5_dict = {'INDI': 'I4',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Nephiew
        p6_dict = {'INDI': 'I5',
                'NAME' : 'Person /Three',
                'SEX': 'M',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        aunt = Individual.instance_from_dict(p3_dict)
        dad = Individual.instance_from_dict(p4_dict)
        mom = Individual.instance_from_dict(p5_dict)
        nephiew = Individual.instance_from_dict(p6_dict)
        fam_dict = { 'FAM': 'F0',
                'HUSB': grandpa,
                'WIFE': grandma,
                'MARR': '15 Mar 1994',
                'CHIL': [aunt,dad],
        }
        fam_dict2 = { 'FAM': 'F1',
                'HUSB': dad,
                'WIFE': mom,
                'MARR': '16 Aug 2024',
                'CHIL': [nephiew],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': nephiew,
                'WIFE': aunt,
                'MARR': '15 Sep 2044',
        }
        Family.instance_from_dict(fam_dict2)
        Family.instance_from_dict(fam_dict3)
   
        self.assertTrue(Family.instance_from_dict(fam_dict).marriage_check)

    def test_marriage_invalid2(self):
        #Grandpa
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0',
                'CHIL': ['I2','I3'],
                }
        #Grandma
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0',
                'CHIL': ['I2','I3'],
                }
        #Uncle
        p3_dict = { 'INDI': 'I2',
                'NAME': 'Pperson /One',
                'SEX': 'M',
                'BIRT':'23 Apr 2000',
                'FAM': 'F0'
                }
        #Dad
        p4_dict = { 'INDI': 'I3',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p5_dict = {'INDI': 'I4',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Niece
        p6_dict = {'INDI': 'I5',
                'NAME' : 'Person /Three',
                'SEX': 'F',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        uncle = Individual.instance_from_dict(p3_dict)
        dad = Individual.instance_from_dict(p4_dict)
        mom = Individual.instance_from_dict(p5_dict)
        niece = Individual.instance_from_dict(p6_dict)
        fam_dict = { 'FAM': 'F0',
                'HUSB': grandpa,
                'WIFE': grandma,
                'MARR': '15 Mar 1994',
                'CHIL': [uncle,dad],
        }
        fam_dict2 = { 'FAM': 'F1',
                'HUSB': dad,
                'WIFE': mom,
                'MARR': '16 Aug 2024',
                'CHIL': [niece],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': uncle,
                'WIFE': niece,
                'MARR': '15 Sep 2044',
        }
        Family.instance_from_dict(fam_dict2)
        Family.instance_from_dict(fam_dict3)
   
        self.assertTrue(Family.instance_from_dict(fam_dict).marriage_check)

    def test_marriage_valid2(self):
        #Grandpa
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0',
                'CHIL': ['I3'],
                }
        #Grandma
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0',
                'CHIL': ['I3'],
                }
        #wife
        p3_dict = { 'INDI': 'I2',
                'NAME': 'Pperson /One',
                'SEX': 'F',
                'BIRT':'23 Apr 2025',
                'FAM': 'F0'
                }
        #Dad
        p4_dict = { 'INDI': 'I3',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p5_dict = {'INDI': 'I4',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Nephiew
        p6_dict = {'INDI': 'I5',
                'NAME' : 'Person /Three',
                'SEX': 'M',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        wife = Individual.instance_from_dict(p3_dict)
        dad = Individual.instance_from_dict(p4_dict)
        mom = Individual.instance_from_dict(p5_dict)
        nephiew = Individual.instance_from_dict(p6_dict)
        fam_dict = { 'FAM': 'F0',
                'HUSB': grandpa,
                'WIFE': grandma,
                'MARR': '15 Mar 1994',
                'CHIL': [dad],
        }
        fam_dict2 = { 'FAM': 'F1',
                'HUSB': dad,
                'WIFE': mom,
                'MARR': '16 Aug 2024',
                'CHIL': [nephiew],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': nephiew,
                'WIFE': wife,
                'MARR': '15 Sep 2044',
        }
        Family.instance_from_dict(fam_dict2)
        Family.instance_from_dict(fam_dict3)
   
        self.assertFalse(Family.instance_from_dict(fam_dict).anomalies)

    def test_marriage_valid3(self):
        #Grandpa
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0',
                'CHIL': ['I3'],
                }
        #Grandma
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0',
                'CHIL': ['I3'],
                }
        #husband
        p3_dict = { 'INDI': 'I2',
                'NAME': 'Pperson /One',
                'SEX': 'M',
                'BIRT':'23 Apr 2025',
                'FAM': 'F0'
                }
        #Dad
        p4_dict = { 'INDI': 'I3',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p5_dict = {'INDI': 'I4',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Niece
        p6_dict = {'INDI': 'I5',
                'NAME' : 'Person /Three',
                'SEX': 'F',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        husband = Individual.instance_from_dict(p3_dict)
        dad = Individual.instance_from_dict(p4_dict)
        mom = Individual.instance_from_dict(p5_dict)
        niece = Individual.instance_from_dict(p6_dict)
        fam_dict = { 'FAM': 'F0',
                'HUSB': grandpa,
                'WIFE': grandma,
                'MARR': '15 Mar 1994',
                'CHIL': [dad],
        }
        fam_dict2 = { 'FAM': 'F1',
                'HUSB': dad,
                'WIFE': mom,
                'MARR': '16 Aug 2024',
                'CHIL': [niece],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': husband,
                'WIFE': niece,
                'MARR': '15 Sep 2044',
        }
        Family.instance_from_dict(fam_dict2)
        Family.instance_from_dict(fam_dict3)
   
        self.assertFalse(Family.instance_from_dict(fam_dict).anomalies)

if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
