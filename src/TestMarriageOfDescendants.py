import unittest
from Family import Family
from Individual import Individual

class MarriageOfSiblings(unittest.TestCase):

#     def test_valid_marriages(self):
#         p1_dict = { 'INDI': 'I0',
#                 'NAME': 'Person /One',
#                 'SEX': 'M',
#                 'BIRT': '8 Jan 1972',
#                 'FAM': 'F0'
#                 }
#         p2_dict = { 'INDI': 'I0',
#                 'NAME': 'Person /Two',
#                 'SEX': 'F',
#                 'BIRT': '11 Aug 1973',
#                 'FAM': 'F0'
#                 }
#         p3_dict = { 'INDI': 'I1',
#                 'NAME': 'Pperson /One',
#                 'SEX': 'F',
#                 'BIRT':'23 Apr 2000',
#                 'FAM': 'F0'
#                 }
#         p4_dict = { 'INDI': 'I1',
#                 'NAME': 'Personn /One',
#                 'SEX': 'M',
#                 'BIRT':'20 Mar 2001',
#                 'FAM': 'F0'
#                 }                
# 
#         husband = Individual.instance_from_dict(p1_dict)
#         wife = Individual.instance_from_dict(p2_dict)
#         child1 = Individual.instance_from_dict(p3_dict)
#         child2 = Individual.instance_from_dict(p4_dict)        
#         fam_dict = { 'FAM': 'F0',
#                 'HUSB': husband,
#                 'WIFE': wife,
#                 'MARR': '15 Mar 1994',
#                 'CHIL': [child1,child2],
#         }
# 
#         self.assertFalse(Family.instance_from_dict(fam_dict).anomalies)
#     
    def test_marriage_invalid(self):
        p1_dict = { 'INDI': 'I1',
                'NAME': 'A /Roberts',
                'SEX': 'M',
                'BIRT': '8 Jan 1900',
                'FAM': ['F0','F2'],
                }
        p2_dict = { 'INDI': 'I2',
                'NAME': 'Aa /Smith',
                'SEX': 'F',
                'BIRT': '11 Aug 1902',
                'FAM': 'F0'
                }
        p3_dict = { 'INDI': 'I3',
                'NAME': 'B /Roberts',
                'SEX': 'F',
                'BIRT':'23 Apr 1930',
                'FAM': 'F1'
                }
        p4_dict = { 'INDI': 'I4',
                'NAME': 'Bb /Banks',
                'SEX': 'M',
                'BIRT':'20 Mar 1932',
                'FAM': 'F1'
                }
        p5_dict = { 'INDI': 'I5',
                'NAME': 'C /Banks',
                'SEX': 'F',
                'BIRT':'20 Mar 1952',
                'FAM': 'F2',
                }                

        husband1 = Individual.instance_from_dict(p1_dict)
        wife1 = Individual.instance_from_dict(p2_dict)
        
        wife2 = Individual.instance_from_dict(p3_dict)
        husband2 = Individual.instance_from_dict(p4_dict)
        
        wife3 = Individual.instance_from_dict(p5_dict)       
        
        fam_dict1 = { 'FAM': 'F0',
                'HUSB': husband1,
                'WIFE': wife1,
                'MARR': '15 Mar 1929',
                'DIV': '17 Mar 1935',
                'CHIL': [wife2,husband2],
        }
        fam_dict2 = { 'FAM': 'F1',
                'HUSB': husband2,
                'WIFE': wife2,
                'MARR': '15 Jul 1968',
                'CHIL': [wife3],
        }
        fam_dict3 = { 'FAM': 'F2',
                'HUSB': husband1,
                'WIFE': wife3,
                'MARR': '15 Jul 1972',
        }

        Family.instance_from_dict(fam_dict3)
        Family.instance_from_dict(fam_dict2)
        Family.instance_from_dict(fam_dict1)       
        #self.assertTrue(Individual.instance_from_dict(p1_dict).anomalies)
        self.assertTrue(Family.instance_from_dict(fam_dict3).anomalies)
        


if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)