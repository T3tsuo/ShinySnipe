import os
import time

import filter

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"

time.sleep(2)
filter.run("1200000")


