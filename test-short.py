import unittest 
import short

class Test(unittest.TestCase):

    def test_x1(self): #it checks the main method
        self.assertRaises(TypeError, short.process_input("","",1,3))
    
    def test_y1(self): #it checks the main method
        self.assertRaises(TypeError, short.process_input(1,"skdk",2,3))
               
    def test_x2(self): #it checks the main method
        self.assertRaises(TypeError, short.process_input(1,1,"alkdj",5))
        
    def test_y2(self): #it checks the main method
        self.assertRaises(TypeError, short.process_input(1,1,5,"a"))
    
    def test4(self): #it checks the main method
        self.assertEqual(0, short.shortest_distance(1,1,1,1))


if __name__ == '__main__':
    unittest.main()
