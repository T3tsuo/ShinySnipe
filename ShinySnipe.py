import os
import time

import filter, refresh_buy

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"

time.sleep(2)
# 10 minutes
end_time = 600 + time.time()
filter.run("1000")
refresh_buy.run(end_time)
