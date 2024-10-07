import time
import uuid
from queue import Queue

queue = Queue()


def generate_request():
    request_id = uuid.uuid4()
    print(f"id: {request_id} generated")
    queue.put(request_id)


def process_request():
    if not queue.empty():
        request_id = queue.get()
        print(f"Request with id {request_id} processed")
    else:
        print("Request queue is empty")
    print(f"id {request_id} deleted")


if __name__ == '__main__':

    # Main thread: Generate and process requests with a delay
    print("ctrl + C to finish \n")
    while True:
        generate_request()
        process_request()
        time.sleep(1)  # Delay of 1 second before the next request

    print("Program has finished.")
