import unittest
from Family import Family
from Individual import Individual

class US04Tests(unittest.TestCase):
    
    def test_valid(self):
        p1_dict = { 'INDI': 'I1',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '24 Feb 1980',
                'DEAT': '20 Feb 2020',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I2',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '13 Feb 1980',
                'FAM': 'F0'
                }

        person3_dict = {'INDI': 'I3', 'NAME': 'Person /3', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person4_dict = {'INDI': 'I4', 'NAME': 'Person /4', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person5_dict = {'INDI': 'I5', 'NAME': 'Person /5', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person6_dict = {'INDI': 'I6', 'NAME': 'Person /6', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person7_dict = {'INDI': 'I7', 'NAME': 'Person /7', 'SEX': 'M', 'BIRT': '15 Feb 2019', 'FAM': 'F0'}

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        children = [person3_dict, person4_dict, person5_dict, person6_dict, person7_dict]

        for i in range(len(children)):
            children[i] = Individual.instance_from_dict(children[i])

        fam_dict = {'FAM': 'F0',
        'HUSB': husband,
        'WIFE': wife,
        'MARR': '14 FEB 2017',
        'CHIL': children}

        self.assertFalse(Family.instance_from_dict(fam_dict).errors)

    def test_invalid(self):
        p1_dict = { 'INDI': 'I1',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '24 Feb 1980',
                'DEAT': '20 Feb 1979',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I2',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '13 Feb 1980',
                'FAM': 'F0'
                }

        person3_dict = {'INDI': 'I3', 'NAME': 'Person /3', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person4_dict = {'INDI': 'I4', 'NAME': 'Person /4', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person5_dict = {'INDI': 'I5', 'NAME': 'Person /5', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person6_dict = {'INDI': 'I6', 'NAME': 'Person /6', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person7_dict = {'INDI': 'I7', 'NAME': 'Person /7', 'SEX': 'M', 'BIRT': '15 Feb 2019', 'FAM': 'F0'}

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        children = [person3_dict, person4_dict, person5_dict, person6_dict, person7_dict]

        for i in range(len(children)):
            children[i] = Individual.instance_from_dict(children[i])

        fam_dict = {'FAM': 'F0',
        'HUSB': husband,
        'WIFE': wife,
        'MARR': '14 FEB 2017',
        'CHIL': children}

        self.assertTrue(Family.instance_from_dict(fam_dict).errors)        

    def test_valid2(self):
        p1_dict = { 'INDI': 'I1',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '24 Feb 1980',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I2',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '13 Feb 1980',
                'DEAT': '20 Feb 2020',
                'FAM': 'F0'
                }

        person3_dict = {'INDI': 'I3', 'NAME': 'Person /3', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person4_dict = {'INDI': 'I4', 'NAME': 'Person /4', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person5_dict = {'INDI': 'I5', 'NAME': 'Person /5', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person6_dict = {'INDI': 'I6', 'NAME': 'Person /6', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person7_dict = {'INDI': 'I7', 'NAME': 'Person /7', 'SEX': 'M', 'BIRT': '15 Feb 2019', 'FAM': 'F0'}

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        children = [person3_dict, person4_dict, person5_dict, person6_dict, person7_dict]

        for i in range(len(children)):
            children[i] = Individual.instance_from_dict(children[i])

        fam_dict = {'FAM': 'F0',
        'HUSB': husband,
        'WIFE': wife,
        'MARR': '14 FEB 2017',
        'CHIL': children}

        self.assertFalse(Family.instance_from_dict(fam_dict).errors)

    def test_invalid2(self):
        p1_dict = { 'INDI': 'I1',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '24 Feb 1980',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I2',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '13 Feb 1980',
                'DEAT': '20 Feb 1977',
                'FAM': 'F0'
                }

        person3_dict = {'INDI': 'I3', 'NAME': 'Person /3', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person4_dict = {'INDI': 'I4', 'NAME': 'Person /4', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person5_dict = {'INDI': 'I5', 'NAME': 'Person /5', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person6_dict = {'INDI': 'I6', 'NAME': 'Person /6', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person7_dict = {'INDI': 'I7', 'NAME': 'Person /7', 'SEX': 'M', 'BIRT': '15 Feb 2019', 'FAM': 'F0'}

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        children = [person3_dict, person4_dict, person5_dict, person6_dict, person7_dict]

        for i in range(len(children)):
            children[i] = Individual.instance_from_dict(children[i])

        fam_dict = {'FAM': 'F0',
        'HUSB': husband,
        'WIFE': wife,
        'MARR': '14 FEB 2017',
        'CHIL': children}

        self.assertTrue(Family.instance_from_dict(fam_dict).errors)

    def test_valid3(self):
        p1_dict = { 'INDI': 'I1',
                'NAME': 'Person /One',
                'SEX': 'M',
                'BIRT': '24 Feb 1980',
                'FAM': 'F0'
                }
        p2_dict = { 'INDI': 'I2',
                'NAME': 'Person /Two',
                'SEX': 'F',
                'BIRT': '13 Feb 1980',
                'FAM': 'F0'
                }

        person3_dict = {'INDI': 'I3', 'NAME': 'Person /3', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'DEAT': '20 Feb 2040', 'FAM': 'F0'}
        person4_dict = {'INDI': 'I4', 'NAME': 'Person /4', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person5_dict = {'INDI': 'I5', 'NAME': 'Person /5', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person6_dict = {'INDI': 'I6', 'NAME': 'Person /6', 'SEX': 'M', 'BIRT': '15 Feb 2018', 'FAM': 'F0'}
        person7_dict = {'INDI': 'I7', 'NAME': 'Person /7', 'SEX': 'M', 'BIRT': '15 Feb 2019', 'FAM': 'F0'}

        husband = Individual.instance_from_dict(p1_dict)
        wife = Individual.instance_from_dict(p2_dict)
        children = [person3_dict, person4_dict, person5_dict, person6_dict, person7_dict]

        for i in range(len(children)):
            children[i] = Individual.instance_from_dict(children[i])

        fam_dict = {'FAM': 'F0',
        'HUSB': husband,
        'WIFE': wife,
        'MARR': '14 FEB 2017',
        'CHIL': children}

        self.assertFalse(Family.instance_from_dict(fam_dict).errors)

if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
