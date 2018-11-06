import unittest
from Family import Family
from Individual import Individual

class TestCorrectGender(unittest.TestCase):

    def test_both_valid(self):
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '28 Feb 1980',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '13 Feb 1980',
                'FAM': 'F0'
                }

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        fam_dict = { 'FAM': 'F0',
                'HUSB': husband,
                'WIFE': wife,
                'MARR': '15 Mar 2002',
        }

        self.assertFalse(Family.instance_from_dict(fam_dict).anomalies)
    
    def test_first_invalid(self):
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'F',
                'BIRT': '28 Feb 1980',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '13 Feb 1980',
                'FAM': 'F0'
                }

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        fam_dict = { 'FAM': 'F0',
                'HUSB': husband,
                'WIFE': wife,
                'MARR': '15 Mar 2002',
        }

        self.assertTrue(len(Family.instance_from_dict(fam_dict).anomalies) == 1)

    def test_second_invalid(self):
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '28 Feb 1980',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'M',
                'BIRT': '13 Feb 1980',
                'FAM': 'F0'
                }

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        fam_dict = { 'FAM': 'F0',
                'HUSB': husband,
                'WIFE': wife,
                'MARR': '15 Mar 2002',
        }

        self.assertTrue(len(Family.instance_from_dict(fam_dict).anomalies) == 1)

    def test_both_invalid(self):
        p1_dict = { 'INDI': 'I0',
                'NAME': 'Person /One',
                'SEX': 'F',
                'BIRT': '28 Feb 1980',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I1',
                'NAME': 'Person /Two',
                'SEX': 'M',
                'BIRT': '13 Feb 1980',
                'FAM': 'F0'
                }

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        fam_dict = { 'FAM': 'F0',
                'HUSB': husband,
                'WIFE': wife,
                'MARR': '15 Mar 2002',
        }

        self.assertTrue(len(Family.instance_from_dict(fam_dict).anomalies) == 2)

if __name__ == '__main__':
    unittest.main()