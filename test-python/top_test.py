import os

id = os.getpid()
os.system(f"top -b -p {id} > top_res.log")
