import unittest
from Family import Family
from Individual import Individual

class US25Tests(unittest.TestCase):
    
   
    
    def test_valid_corr(self):

        p3_dict = { 'INDI': 'I2',
                'NAME': 'Jill /Bond',
                'SEX': 'F',
                'BIRT':'23 Apr 2000',
                'FAM': 'F0'
                }
        p4_dict = { 'INDI': 'I3',
                'NAME': 'Max /Bond',
                'SEX': 'M',
                'BIRT':'20 Mar 2001',
                'FAM': 'F0'
                }                

        child1 = Individual.instance_from_dict(p3_dict)
        child2 = Individual.instance_from_dict(p4_dict) 
        
        p1_dict = { 'INDI': 'I0',
                'NAME': 'James /Bond',
                'SEX': 'M',
                'BIRT': '8 Jan 1972',
                'FAM': 'F0',
                'CHIL':[child2]
                }
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Sarah /Bond',
                'SEX': 'F',
                'BIRT': '11 Aug 1973',
                'FAM': 'F0',
                'CHIL':[child2]
                }                          
        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)                        
        fam_dict = { 'FAM': 'F0',
                'HUSB': husband,
                'WIFE': wife,
                'MARR': '15 Mar 1994',
                'CHIL': [child1],
        }

        self.assertFalse(Family.instance_from_dict(fam_dict).errors)



if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)