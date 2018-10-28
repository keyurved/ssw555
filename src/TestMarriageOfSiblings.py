import unittest
from Family import Family
from Individual import Individual

class MarriageOfSiblings(unittest.TestCase):

    def test_valid_marriages(self):
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I0',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0'
                }
        p3_dict = { 'INDI': 'I1',
                'NAME': 'Pperson /One',
                'SEX': 'F',
                'BIRT':'23 Apr 2000',
                'FAM': 'F0'
                }
        p4_dict = { 'INDI': 'I1',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0'
                }                

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        child1 = Individual.instance_from_dict(p3_dict)
        child2 = Individual.instance_from_dict(p4_dict)        
        fam_dict = { 'FAM': 'F0',
                'HUSB': husband,
                'WIFE': wife,
                'MARR': '15 Mar 1994',
                'CHIL': [child1,child2],
        }

        self.assertFalse(Family.instance_from_dict(fam_dict).anomalies)
    
    def test_marriage_invalid(self):
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0'
                }
        p3_dict = { 'INDI': 'I2',
                'NAME': 'Pperson /One',
                'SEX': 'F',
                'BIRT':'23 Apr 2000',
                'FAM': 'F0'
                }
        p4_dict = { 'INDI': 'I3',
                'NAME': 'Personn /One',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0'
                }                

        husband1 = Individual.instance_from_dict(p1_dict)
        wife1 = Individual.instance_from_dict(p2_dict)
        child1 = Individual.instance_from_dict(p3_dict)
        child2 = Individual.instance_from_dict(p4_dict)       
        fam_dict = { 'FAM': 'F0',
                'HUSB': husband1,
                'WIFE': wife1,
                'MARR': '15 Mar 1994',
                'CHIL': [child1,child2],
        }
        fam_dict2 = { 'FAM': 'F1',
                'HUSB': child2,
                'WIFE': child1,
                'MARR': '15 Jul 2018',
        }
        Family.instance_from_dict(fam_dict2)
        self.assertTrue(Family.instance_from_dict(fam_dict).anomalies)
        


if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)