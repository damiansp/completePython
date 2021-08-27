echo flags.py
python3 flags.py

echo flags_threadpool.py
python3 flags_threadpool.py -s DELAY a b c # -s: server

echo flags_threadpool_asyncio.py

# get 100 using 100 concurrent requests
python3 flags_threadpool_asyncio.py -s ERROR -al 100 -m 100 
