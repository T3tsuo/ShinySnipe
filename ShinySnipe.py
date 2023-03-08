import os
import time

import filter, refresh_buy, move

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"

price = input("Enter search price for shiny: ")

time.sleep(2)

while True:
    # shake off afk timer
    move.one_block()
    # 10 minutes
    end_time = 600 + time.time()
    filter.run(price)
    refresh_buy.run(end_time)
