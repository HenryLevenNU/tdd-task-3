from main import sound_effect

def test_fizz_happy():
    assert sound_effect(3) == "Fizz"
    assert sound_effect(9) == "Fizz"
    assert sound_effect(-12) == "Fizz"


def test_buzz_happy():
    assert sound_effect(5) == "Buzz"
    assert sound_effect(20) == "Buzz"
    assert sound_effect(-10) == "Buzz"


def test_no_sound_effect():
    assert sound_effect(17) == "No fizzing... No buzzing..."
    assert sound_effect(-14) == "No fizzing... No buzzing..."
    assert sound_effect(0.5) == "No fizzing... No buzzing..."

def test_fizz_buzz():
    assert sound_effect(15) == "FizzBuzz"
    assert sound_effect(0) == "FizzBuzz"
    assert sound_effect(-30) == "FizzBuzz"