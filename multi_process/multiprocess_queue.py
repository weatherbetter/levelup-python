import multiprocessing
import time

def pro1(q):
    # q에 데이터를 넣는다
    for i in range(100):
        q.put(str(i))
        time.sleep(0.1)

def pro2(q):
    # q에 데이터를 빼낸다
    for i in range(100):
        item = q.get()
        print(item)

if __name__ == '__main__':
    # Queue
    queue = multiprocessing.Queue()
    # # SimpleQueue
    # queue = multiprocessing.SimpleQueue()
    # # JoinableQueue
    # queue = multiprocessing.JoinableQueue()
    
    p1 = multiprocessing.Process(target=pro1, args=(queue,))
    p2 = multiprocessing.Process(target=pro2, args=(queue,))

    p1.start()
    p2.start()