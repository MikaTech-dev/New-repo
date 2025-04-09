# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module

from camelcase import CamelCase
# Import custom module
c = CamelCase()

today = date.today()
# today = datetime.date.today()
# timestamp = time.time()
timestamp = time()
print(today)
print (timestamp)

print (c.hump('hello every one'))
