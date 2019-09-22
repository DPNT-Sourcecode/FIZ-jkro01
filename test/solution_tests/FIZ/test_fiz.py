from solutions.FIZ import fizz_buzz_solution

class TestFiz():
    def test_fiz(self):
        assert fizz_buzz_solution.fizz_buzz(3) == 'fizz'
        assert fizz_buzz_solution.fizz_buzz(9) == 'fizz'
        assert fizz_buzz_solution.fizz_buzz(20) == 'buzz'
        assert fizz_buzz_solution.fizz_buzz(15) == 'fizz buzz'
        assert fizz_buzz_solution.fizz_buzz(11) == '11'
        assert fizz_buzz_solution.fizz_buzz(301) == 'fizz'
        assert fizz_buzz_solution.fizz_buzz(551) == 'buzz'

