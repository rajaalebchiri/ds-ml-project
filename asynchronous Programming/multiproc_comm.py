import multiprocessing


def process1_send_function(conn, events):
    for event in events:
        conn.send(event)
        print(f"Event Sent: {event}")


def process2_recv_function(conn):
    while True:
        event = conn.recv()
        if event == "eod":
            print("Event Received: End of Day")
            return
        print(f"Event Received: {event}")


# Queue Version
def process1_queue_version(queue, events):
    for event in events:
        queue.put(event)
        print(f"Event Sent: {event}")


def process2_queue_version(queue):
    while True:
        event = queue.get()
        if event == "eod":
            print("Event Received: End of Day")
            return
        print(f"Event Received: {event}")


def run():
    events = ["get up", "brush your teeth", "shower", "work", "eod"]
    # Pipe Version
    """conn1, conn2 = multiprocessing.Pipe()
    process_1 = multiprocessing.Process(target=process1_send_function, args=(conn1, events))
    process_2 = multiprocessing.Process(target=process2_recv_function, args=(conn2,))"""
    # Queue Version
    queue = multiprocessing.Queue()
    process_1 = multiprocessing.Process(
        target=process1_queue_version, args=(queue, events)
    )
    process_2 = multiprocessing.Process(target=process2_queue_version, args=(queue,))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()


if __name__ == "__main__":
    run()
