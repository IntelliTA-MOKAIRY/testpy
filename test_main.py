import sys
from greeting import make_greeting

def test_make_greeting():
    result = make_greeting("Alice")
    if result != "Hello, Alice!":
        print(f"FAIL: Expected 'Hello, Alice!' but got '{result}'", file=sys.stderr)
        sys.exit(1)
    
    print("PASS: test_make_greeting")

if __name__ == "__main__":
    test_make_greeting()
