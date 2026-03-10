import os
import os.path
import glob
import csv
from datetime import datetime

import mysql.connector as MyConn

mydb = MyConn.connect(host='localhost', username='root', password='admin', database='a1')
print("connected")

