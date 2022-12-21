import time

import sqlmanager

sqlmanager.thingup()
time.sleep(2)
print(sqlmanager.encryptionread())
