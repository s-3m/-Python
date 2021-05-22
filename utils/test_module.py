from utils import currency_rates
import sys

user_value = ''.join(sys.argv[1:])
currency_rates(user_value.upper())