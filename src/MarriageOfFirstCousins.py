import unittest
from Family import Family
from Individual import Individual

class MarriageOfFirstCousins(unittest.TestCase):

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
                'FAM': 'F0',
                'CHIL': ['I4'],
                }
        #Uncle
        p4_dict = {'INDI': 'I3',
                'NAME': 'Person /Four',
                'SEX': 'M',
                'BIRT': '24 Apr 2000',
                'FAM': 'F0',
                'CHIL': ['I4'],
                }

        #Niece
        p5_dict = {'INDI':'I4',
                'NAME': 'Person /Five',
                'SEX': 'F',
                'BIRT': '25 Sep 2025',
                'FAM': 'F0',
            }
        #Dad
        p6_dict = { 'INDI': 'I5',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p7_dict = {'INDI': 'I6',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Son
        p8_dict = {'INDI': 'I7',
                'NAME' : 'Person /Three',
                'SEX': 'M',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        aunt = Individual.instance_from_dict(p3_dict)
        uncle = Individual.instance_from_dict(p4_dict)
        niece = Individual.instance_from_dict(p5_dict)
        dad = Individual.instance_from_dict(p6_dict)
        mom = Individual.instance_from_dict(p7_dict)
        son = Individual.instance_from_dict(p8_dict)
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
                'CHIL': [son],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': uncle,
                'WIFE': aunt,
                'MARR': '16 Sep 2023',
                'CHIL': [niece],
        }
        Family.instance_from_dict(fam_dict3)
        Family.instance_from_dict(fam_dict2)
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
                'FAM': 'F0',
                'CHIL': ['I4'],
                }
        #Uncle
        p4_dict = {'INDI': 'I3',
                'NAME': 'Person /Four',
                'SEX': 'M',
                'BIRT': '24 Apr 2000',
                'FAM': 'F0',
                'CHIL': ['I4'],
                }

        #Niece
        p5_dict = {'INDI':'I4',
                'NAME': 'Person /Five',
                'SEX': 'F',
                'BIRT': '25 Sep 2025',
                'FAM': 'F0',
            }
        #Dad
        p6_dict = { 'INDI': 'I5',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p7_dict = {'INDI': 'I6',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Son
        p8_dict = {'INDI': 'I7',
                'NAME' : 'Person /Three',
                'SEX': 'M',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        aunt = Individual.instance_from_dict(p3_dict)
        uncle = Individual.instance_from_dict(p4_dict)
        niece = Individual.instance_from_dict(p5_dict)
        dad = Individual.instance_from_dict(p6_dict)
        mom = Individual.instance_from_dict(p7_dict)
        son = Individual.instance_from_dict(p8_dict)
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
                'CHIL': [son],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': son,
                'WIFE': niece,
                'MARR': '15 Sep 2044',
        }
        fam_dict4 = {'FAM': 'F3',
                'HUSB': uncle,
                'WIFE': aunt,
                'MARR': '14 Sep 2023',
                'CHIL': [niece],
        }
        Family.instance_from_dict(fam_dict2)
        Family.instance_from_dict(fam_dict4)
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
        #Aunt
        p3_dict = { 'INDI': 'I2',
                'NAME': 'Pperson /One',
                'SEX': 'F',
                'BIRT':'23 Apr 2000',
                'FAM': 'F0',
                'CHIL': ['I4'],
                }
        #Uncle
        p4_dict = {'INDI': 'I3',
                'NAME': 'Person /Four',
                'SEX': 'M',
                'BIRT': '24 Apr 2000',
                'FAM': 'F0',
                'CHIL': ['I4'],
                }

        #nephiew
        p5_dict = {'INDI':'I4',
                'NAME': 'Person /Five',
                'SEX': 'M',
                'BIRT': '25 Sep 2025',
                'FAM': 'F0',
            }
        #Dad
        p6_dict = { 'INDI': 'I5',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p7_dict = {'INDI': 'I6',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Daughter
        p8_dict = {'INDI': 'I7',
                'NAME' : 'Person /Three',
                'SEX': 'F',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        aunt = Individual.instance_from_dict(p3_dict)
        uncle = Individual.instance_from_dict(p4_dict)
        nephiew = Individual.instance_from_dict(p5_dict)
        dad = Individual.instance_from_dict(p6_dict)
        mom = Individual.instance_from_dict(p7_dict)
        daughter = Individual.instance_from_dict(p8_dict)
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
                'CHIL': [daughter],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': daughter,
                'WIFE': nephiew,
                'MARR': '15 Sep 2044',
        }
        fam_dict4 = {'FAM': 'F3',
                'HUSB': uncle,
                'WIFE': aunt,
                'MARR': '14 Sep 2023',
                'CHIL': [nephiew],
        }
        Family.instance_from_dict(fam_dict2)
        Family.instance_from_dict(fam_dict4)
        Family.instance_from_dict(fam_dict3)
   
        self.assertTrue(Family.instance_from_dict(fam_dict).marriage_check)

    def test_valid_marriages2(self):
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
                'FAM': 'F0',
                'CHIL': ['I4'],
                }
        #Uncle
        p4_dict = {'INDI': 'I3',
                'NAME': 'Person /Four',
                'SEX': 'M',
                'BIRT': '24 Apr 2000',
                'FAM': 'F0',
                'CHIL': ['I4'],
                }

        #Nephiew
        p5_dict = {'INDI':'I4',
                'NAME': 'Person /Five',
                'SEX': 'M',
                'BIRT': '25 Sep 2025',
                'FAM': 'F0',
            }
        #Dad
        p6_dict = { 'INDI': 'I5',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p7_dict = {'INDI': 'I6',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Daughter
        p8_dict = {'INDI': 'I7',
                'NAME' : 'Person /Three',
                'SEX': 'F',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        aunt = Individual.instance_from_dict(p3_dict)
        uncle = Individual.instance_from_dict(p4_dict)
        nephiew = Individual.instance_from_dict(p5_dict)
        dad = Individual.instance_from_dict(p6_dict)
        mom = Individual.instance_from_dict(p7_dict)
        daughter = Individual.instance_from_dict(p8_dict)
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
                'CHIL': [daughter],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': uncle,
                'WIFE': aunt,
                'MARR': '16 Sep 2023',
                'CHIL': [nephiew],
        }
        Family.instance_from_dict(fam_dict3)
        Family.instance_from_dict(fam_dict2)
        self.assertFalse(Family.instance_from_dict(fam_dict).anomalies)

    def test_valid_marriages3(self):
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
                'FAM': 'F0',
                'CHIL': ['I4'],
                }
        #Uncle
        p4_dict = {'INDI': 'I3',
                'NAME': 'Person /Four',
                'SEX': 'M',
                'BIRT': '24 Apr 2000',
                'FAM': 'F0',
                'CHIL': ['I4'],
                }

        #Niece
        p5_dict = {'INDI':'I4',
                'NAME': 'Person /Five',
                'SEX': 'F',
                'BIRT': '25 Sep 2025',
                'FAM': 'F0',
            }
        #Dad
        p6_dict = { 'INDI': 'I5',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Mom
        p7_dict = {'INDI': 'I6',
                'NAME': 'Persone /Two',
                'SEX': 'F',
                'BIRT': '20 Mar 2002',
                'FAM': 'F0',
                'CHIL': ['I5'],
                }
        #Son
        p8_dict = {'INDI': 'I7',
                'NAME' : 'Person /Three',
                'SEX': 'M',
                'BIRT': '25 Mar 2026',
                'FAM': 'F0'
                }
        #nephiew
        p9_dict = {'INDI':'I4',
                'NAME': 'Person /Fivee',
                'SEX': 'M',
                'BIRT': '25 Sep 2027',
                'FAM': 'F0',
            }

        grandpa = Individual.instance_from_dict(p1_dict)
        grandma = Individual.instance_from_dict(p2_dict)
        aunt = Individual.instance_from_dict(p3_dict)
        uncle = Individual.instance_from_dict(p4_dict)
        niece = Individual.instance_from_dict(p5_dict)
        dad = Individual.instance_from_dict(p6_dict)
        mom = Individual.instance_from_dict(p7_dict)
        son = Individual.instance_from_dict(p8_dict)
        nephiew = Individual.instance_from_dict(p9_dict)
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
                'CHIL': [son],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': uncle,
                'WIFE': aunt,
                'MARR': '16 Sep 2023',
                'CHIL': [niece, nephiew],
        }
        Family.instance_from_dict(fam_dict3)
        Family.instance_from_dict(fam_dict2)
        self.assertFalse(Family.instance_from_dict(fam_dict).anomalies)

if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
