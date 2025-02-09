import unittest
from problem import sort


class TestSort(unittest.TestCase):
    def test_standard(self):
        #within boundries of size and weight
        assert "STANDARD" == sort(10,10,10,10)
    
    def test_volume(self):
        #check that 1,000,000 cm^3 returns special
        assert "SPECIAL" == sort(100, 100, 100, 14)
    
    def test_sides(self):
        #check that side larger than 150 cm returns special
        assert "SPECIAL" == sort(155, 100, 20, 19)

    def test_mass(self):
        #check that mass greater than 20kgs returns special
        assert "SPECIAL" == sort(149, 10, 14, 25)

    def test_boundry_mass(self):
        #check that 20 kgs returns special
        assert "SPECIAL" == sort(100, 10, 14, 20)

    def test_boundry_sides(self):
        #check that 150 cm side returns special
        assert "SPECIAL" == sort(150, 10, 14, 15)
    
    def test_boundry_sides(self):
        #check that mass and side exceeding or at the limit returns Rejected
        assert "REJECTED" == sort(155, 10, 14, 25)
    
    def test_boundry_sides(self):
        #check that mass and side or at the limit returns Rejected
        assert "REJECTED" == sort(150, 10, 14, 20)

if __name__ == '__main__':
    unittest.main()