
import unittest
from Family import Family
from Individual import Individual

class TestBirthBeforeDeathOfParents(unittest.TestCase):

  def test_invalid_birth(self):
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
                'DEAT': '12 Aug 1999',
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

        self.assertTrue(Family.instance_from_dict(fam_dict).errors)
    
  def test_valid_birth(self):
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
                'DEAT': '12 Aug 2002',
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

        self.assertFalse(Family.instance_from_dict(fam_dict).errors)
    

if __name__ == '__main__':
    unittest.main()
