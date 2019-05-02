from app.functions import *
import requests
import os
from dotenv import load_dotenv
import pytest
import json

CI_ENV = os.environ.get("CI", "OOPS") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
SKIP_REASON = "to avoid issuing requests from the CI server"

def test_to_usd():
	a = to_usd(3)
	assert a == "$3.00"
	b = to_usd(10)
	assert b == "$10.00"
	c = to_usd(1000)
	assert c == "$1,000.00"
	d = to_usd(1000000)
	assert d == "$1,000,000.00"

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_conf_url():
	load_dotenv()
	api_key = os.environ.get("ALPHAVANTAGE_API_KEY", "OOPS")
	assert api_key != "OOPS"

	symbol = "AAPL"
	response = compile_url(symbol, api_key)
	assert response["Meta Data"]["2. Symbol"] == symbol
	if "Error" in response:
		assert 1 == "There is an error with the AlphaVantage API"

