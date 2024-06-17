import uvicorn
import multiprocessing
from db import DB
DB.initialize('test.db')

from service.service1 import app as service1_app
from service.service2 import app as service2_app
from client import app as client_app


def run_service1():
    uvicorn.run(service1_app, host='0.0.0.0', port=8800)

def run_service2():
    uvicorn.run(service2_app, host='0.0.0.0', port=9000)

def run_client():
    uvicorn.run(client_app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    
    service1_process = multiprocessing.Process(target=run_service1)
    service2_process = multiprocessing.Process(target=run_service2)
    client_process = multiprocessing.Process(target=run_client)
    service1_process.start()
    service2_process.start()
    client_process.start()
    service1_process.join()
    service2_process.join()
    client_process.join()


