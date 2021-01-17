import os

id = os.getpid()
os.system(f"pmap {id} > res.log")
