from selenium import webdriver
import myfunctions
import unittest


class Testmyfunctions(unittest.TestCase):
    def testsquare(self):
        tested_numbers = [0,1,2,3,4,5]
        expected_results = {0:0,1:1,2:4,3:9,4:16,5:25}
        for n in tested_numbers:
            expected = expected_results[n]
            actual = myfunctions.square(n)
            self.assertEqual(expected,actual)

    def testadd(self):
        a = 2
        b = 5
        expected = a + b
        actual = myfunctions.add(a,b)
        self.assertEqual(expected,actual)

suite = unittest.TestSuite()
suite.addTest(Testmyfunctions('testsquare'))
suite.addTest(Testmyfunctions('testadd'))
loader = unittest.TestLoader()
loader.loadTestsFromTestCase(Testmyfunctions)

def runTests():    
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__': runTests()


    
