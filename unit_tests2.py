from test_laba2 import Formulas
import unittest

class TestFormulas(unittest.TestCase):

    def test_first_calculation1(self):
        F = Formulas(1)
        res = F.calculation_1()
        self.assertEqual(res, 6.96700000000000050)

    def test_first_calculation2(self):
        F = Formulas(1)
        res = F.calculation_2()
        self.assertEqual(res, 5.349)

    def test_first_calculation3(self):
        F = Formulas(1)
        res = F.calculation_3()
        self.assertEqual(res, 7.5280000000000005)

    def test_first_calculation4(self):
        F = Formulas(1)
        res = F.calculation_4()
        self.assertEqual(res, 6.363)

    def test_second_calculation1(self):
        F = Formulas(0.1)
        res = F.calculation_1()
        self.assertEqual(res, 0.29857780000000006)

    def test_second_calculation2(self):
        F = Formulas(0.1)
        res = F.calculation_2()
        self.assertEqual(res, 0.36809400000000003)

    def test_second_calculation3(self):
        F = Formulas(0.1)
        res = F.calculation_3()
        self.assertEqual(res, 0.37795000000000006)

    def test_second_calculation4(self):
        F = Formulas(0.1)
        res = F.calculation_4()
        self.assertEqual(res, 0.6363000000000001)

    def test_third_calculation1(self):
        F = Formulas(0)
        res = F.calculation_1()
        self.assertEqual(res, 0.0)

    def test_third_calculation2(self):
        F = Formulas(0)
        res = F.calculation_2()
        self.assertEqual(res, 0.0)

    def test_third_calculation3(self):
        F = Formulas(0)
        res = F.calculation_3()
        self.assertEqual(res, 0.0)

    def test_third_calculation4(self):
        F = Formulas(0)
        res = F.calculation_4()
        self.assertEqual(res, 0.0)

    def test_fourth_calculation1(self):
        F = Formulas(-5)
        res = F.calculation_1()
        self.assertEqual(res, 2714.815)

    def test_fourth_calculation2(self):
        F = Formulas(-5)
        res = F.calculation_2()
        self.assertEqual(res, -548.565)

    def test_fourth_calculation3(self):
        F = Formulas(-5)
        res = F.calculation_3()
        self.assertEqual(res, 87.31)

    def test_fourth_calculation4(self):
        F = Formulas(-5)
        res = F.calculation_4()
        self.assertEqual(res, -31.815)

    def test_fifth_calculation1(self):
        F = Formulas(-200)
        res = F.calculation_1()
        self.assertEqual(res, 7930487776.6)

    def test_fifth_calculation2(self):
        F = Formulas(-200)
        res = F.calculation_2()
        self.assertEqual(res, -30284694.6)

    def test_fifth_calculation3(self):
        F = Formulas(-200)
        res = F.calculation_3()
        self.assertEqual(res, 165927.4)

    def test_fifth_calculation4(self):
        F = Formulas(-200)
        res = F.calculation_4()
        self.assertEqual(res, -1272.6000000000001)

    def test_sixth_calculation1(self):
        F = Formulas(1000)
        res = F.calculation_1()
        self.assertEqual(res, 4970267414317.0)

    def test_sixth_calculation2(self):
        F = Formulas(1000)
        res = F.calculation_2()
        self.assertEqual(res, 3771705873.0)

    def test_sixth_calculation3(self):
        F = Formulas(1000)
        res = F.calculation_3()
        self.assertEqual(res, 4168363.0)

    def test_sixth_calculation4(self):
        F = Formulas(1000)
        res = F.calculation_4()
        self.assertEqual(res, 6363.0)

    def test_seventh_calculation1(self):
        F = Formulas(199)
        res = F.calculation_1()
        self.assertEqual(res, 7808767722.991)

    def test_seventh_calculation2(self):
        F = Formulas(199)
        res = F.calculation_2()
        self.assertEqual(res, 29651148.255000003)

    def test_seventh_calculation3(self):
        F = Formulas(199)
        res = F.calculation_3()
        self.assertEqual(res, 165607.402)

    def test_seventh_calculation4(self):
        F = Formulas(199)
        res = F.calculation_4()
        self.assertEqual(res, 1266.237)

    def test_eighth_calculation1(self):
        F = Formulas(192)
        res = F.calculation_1()
        self.assertEqual(res, 6767228151.744)

    def test_eighth_calculation2(self):
        F = Formulas(192.359)
        res = F.calculation_2()
        self.assertEqual(res, 26777781.43704989)

    def test_eighth_calculation3(self):
        F = Formulas(192.359)
        res = F.calculation_3()
        self.assertEqual(res, 154760.17034636502)

    def test_eighth_calculation4(self):
        F = Formulas(192.359)
        res = F.calculation_4()
        self.assertEqual(res, 1223.9803170000002)

    def test_ninth_calculation1(self):
        F = Formulas(200)
        res = F.calculation_1()
        self.assertEqual(res, 7966825103.4)

    def test_ninth_calculation2(self):
        F = Formulas(200)
        res = F.calculation_2()
        self.assertEqual(res, 30100854.6)

    def test_ninth_calculation3(self):
        F = Formulas(200)
        res = F.calculation_3()
        self.assertEqual(res, 167272.6)

    def test_ninth_calculation4(self):
        F = Formulas(200)
        res = F.calculation_4()
        self.assertEqual(res, 1272.6000000000001)

    def test_tenth_calculation1(self):
        F = Formulas(300)
        res = F.calculation_1()
        self.assertEqual(res, 40301794985.1)

    def test_tenth_calculation2(self):
        F = Formulas(300)
        res = F.calculation_2()
        self.assertEqual(res, 101692341.9)

    def test_tenth_calculation3(self):
        F = Formulas(300)
        res = F.calculation_3()
        self.assertEqual(res, 375858.9)

    def test_tenth_calculation4(self):
        F = Formulas(300)
        res = F.calculation_4()
        self.assertEqual(res, 1908.9)

# /////////////////////////////////////////////////////////////////////////////////////////////////

    def test_eleventh_calculation1(self):
        F = Formulas("x")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_eleventh_calculation2(self):
        F = Formulas("x")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_eleventh_calculation3(self):
        F = Formulas("x")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_eleventh_calculation4(self):
        F = Formulas("x")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twelfth_calculation1(self):
        F = Formulas("151")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twelfth_calculation2(self):
        F = Formulas("151")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twelfth_calculation3(self):
        F = Formulas("151")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twelfth_calculation4(self):
        F = Formulas("151")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_thirteenth_calculation1(self):
        F = Formulas("0-")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_thirteenth_calculation2(self):
        F = Formulas("0-")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_thirteenth_calculation3(self):
        F = Formulas("0-")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_thirteenth_calculation4(self):
        F = Formulas("0-")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_fourteenth_calculation1(self):
        F = Formulas("=1")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_fourteenth_calculation2(self):
        F = Formulas("=1")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_fourteenth_calculation3(self):
        F = Formulas("=1")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_fourteenth_calculation4(self):
        F = Formulas("=1")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_fifteenth_calculation1(self):
        F = Formulas("k0771+")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_fifteenth_calculation2(self):
        F = Formulas("k0771+")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_fifteenth_calculation3(self):
        F = Formulas("k0771+")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_fifteenth_calculation4(self):
        F = Formulas("k0771+")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_sixteenth_calculation1(self):
        F = Formulas("lkj")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_sixteenth_calculation2(self):
        F = Formulas("lkj")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_sixteenth_calculation3(self):
        F = Formulas("lkj")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_sixteenth_calculation4(self):
        F = Formulas("lkj")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_seventeenth_calculation1(self):
        F = Formulas("*5+")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_seventeenth_calculation2(self):
        F = Formulas("*5+")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_seventeenth_calculation3(self):
        F = Formulas("*5+")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_seventeenth_calculation4(self):
        F = Formulas("*5+")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_eighteenth_calculation1(self):
        F = Formulas("98u")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_eighteenth_calculation2(self):
        F = Formulas("98u")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_eighteenth_calculation3(self):
        F = Formulas("98u")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_eighteenth_calculation4(self):
        F = Formulas("98u")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_nineteenth_calculation1(self):
        F = Formulas("  `")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_nineteenth_calculation2(self):
        F = Formulas("  `")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_nineteenth_calculation3(self):
        F = Formulas("  `")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_nineteenth_calculation4(self):
        F = Formulas("  `")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twentieth_calculation1(self):
        F = Formulas("/74k")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twentieth_calculation_2(self):
        F = Formulas("/74k")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twentieth_calculation3(self):
        F = Formulas("/74k")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twentieth_calculation4(self):
        F = Formulas("/74k")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twenty_first_calculation1(self):
        F = Formulas("одisd")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twenty_first_calculation2(self):
        F = Formulas("одisd")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twenty_first_calculation3(self):
        F = Formulas("одisd")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twenty_first_calculation4(self):
        F = Formulas("одisd")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twenty_second_calculation1(self):
        F = Formulas("sd484")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twenty_second_calculation2(self):
        F = Formulas("sd484")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twenty_second_calculation3(self):
        F = Formulas("sd484")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twenty_second_calculation4(self):
        F = Formulas("sd484")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twenty_third_calculation1(self):
        F = Formulas("ada84вм")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twenty_third_calculation2(self):
        F = Formulas("ada84вм")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twenty_third_calculation3(self):
        F = Formulas("ada84вм")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twenty_third_calculation4(self):
        F = Formulas("ada84вм")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twenty_fourth_calculation1(self):
        F = Formulas("фвісы2ыс15")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twenty_fourth_calculation2(self):
        F = Formulas("фвісы2ыс15")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twenty_fourth_calculation3(self):
        F = Formulas("фвісы2ыс15")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twenty_fourth_calculation4(self):
        F = Formulas("фвісы2ыс15")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twenty_fifth_calculation1(self):
        F = Formulas("48увсdv84")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twenty_fifth_calculation2(self):
        F = Formulas("48увсdv84")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twenty_fifth_calculation3(self):
        F = Formulas("48увсdv84")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twenty_fifth_calculation4(self):
        F = Formulas("48увсdv84")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twenty_sixth_calculation1(self):
        F = Formulas("lka462")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twenty_sixth_calculation2(self):
        F = Formulas("lka462")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twenty_sixth_calculation3(self):
        F = Formulas("lka462")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twenty_sixth_calculation4(self):
        F = Formulas("lka462")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twenty_seventh_calculation1(self):
        F = Formulas("*5+a4сі")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twenty_seventh_calculation2(self):
        F = Formulas("*5+a4сі")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twenty_seventh_calculation3(self):
        F = Formulas("*5+a4сі")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twenty_seventh_calculation4(self):
        F = Formulas("*5+a4сі")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twenty_eighth_calculation1(self):
        F = Formulas("9a4841ccd8u")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twenty_eighth_calculation2(self):
        F = Formulas("9a4841ccd8u")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twenty_eighth_calculation3(self):
        F = Formulas("9a4841ccd8u")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twenty_eighth_calculation4(self):
        F = Formulas("9a4841ccd8u")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_twenty_ninth_calculation1(self):
        F = Formulas("511`  `")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_twenty_ninth_calculation2(self):
        F = Formulas("511`  `")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_twenty_ninth_calculation3(self):
        F = Formulas("511`  `")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_twenty_ninth_calculation4(self):
        F = Formulas("511`  `")
        res = F.calculation_4()
        self.assertEqual(res, "Error")

    def test_thirtieth_calculation1(self):
        F = Formulas("/74dac826k")
        res = F.calculation_1()
        self.assertEqual(res, "Error")

    def test_thirtieth_calculation2(self):
        F = Formulas("/74dac826k")
        res = F.calculation_2()
        self.assertEqual(res, "Error")

    def test_thirtieth_calculation3(self):
        F = Formulas("/74dac826k")
        res = F.calculation_3()
        self.assertEqual(res, "Error")

    def test_thirtieth_calculation4(self):
        F = Formulas("/74dac826k")
        res = F.calculation_4()
        self.assertEqual(res, "Error")


if __name__ == '__main__':
    unittest.main()