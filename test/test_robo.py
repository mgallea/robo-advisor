from app.functions import *

def test_to_usd():
	a = to_usd(3)
	assert a == "$3.00"
	b = to_usd(10)
	assert b == "$10.00"
	c = to_usd(1000)
	assert c == "$1,000.00"
	d = to_usd(1000000)
	assert d == "$1,000,000.00"