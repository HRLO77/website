# make sure to run this file with python __main__.py --user to start up the server and api properly (local).
import uvicorn
import sys

if sys.argv[1] == 'True':
    uvicorn.run('backend:app', host='0.0.0.0', port=8000) # edit this line to change what interface and port the server binds to
else:
    uvicorn.run('backend:app')
