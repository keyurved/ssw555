import unittest
from Family import Family
from Individual import Individual

class US25Tests(unittest.TestCase):

    def test_invalid_first_names(self):
        p1_dict = { 'INDI': 'I0',
                'NAME': 'James /Bond',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I0',
                'NAME': 'Sarah /Bond',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0'
                }
        p3_dict = { 'INDI': 'I1',
                'NAME': 'Jill /Bond',
                'SEX': 'F',
                'BIRT':'23 Apr 2000',
                'FAM': 'F0'
                }
        p4_dict = { 'INDI': 'I1',
                'NAME': 'John /Bond',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0'
                } 
        p5_dict = { 'INDI': 'I1',
                'NAME': 'John /Bond',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0'
                }                                

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        child1 = Individual.instance_from_dict(p3_dict)
        child2 = Individual.instance_from_dict(p4_dict)        
        child3 = Individual.instance_from_dict(p5_dict)                
        fam_dict = { 'FAM': 'F0',
                'HUSB': husband,
                'WIFE': wife,
                'MARR': '15 Mar 1994',
                'CHIL': [child1,child2,child3],
        }

        self.assertTrue(Family.instance_from_dict(fam_dict).anomalies)
    
    def test_valid_first_names(self):

        p2_dict = { 'INDI': 'I0',
                'NAME': 'Sarah /Bond',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0'
                }
        p3_dict = { 'INDI': 'I1',
                'NAME': 'Jill /Bond',
                'SEX': 'F',
                'BIRT':'23 Apr 2000',
                'FAM': 'F0'
                }
        p4_dict = { 'INDI': 'I1',
                'NAME': 'Max /Bond',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0'
                }                

        wife = Individual.instance_from_dict(p2_dict)
        child1 = Individual.instance_from_dict(p3_dict)
        child2 = Individual.instance_from_dict(p4_dict)   
        p1_dict = { 'INDI': 'I0',
                'NAME': 'James /Bond',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0',
                'CHIL': [child1, child2]
                }    
        husband = Individual.instance_from_dict(p1_dict)                         
        fam_dict = { 'FAM': 'F0',
                'HUSB': husband,
                'WIFE': wife,
                'MARR': '15 Mar 1994',
                'CHIL': [child1,child2],
        }

        self.assertFalse(Family.instance_from_dict(fam_dict).anomalies)
        


if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)