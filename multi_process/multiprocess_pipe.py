import multiprocessing
import time

def pro1(sender):
    sender.send("123")
    

def pro2(receiver):
    item = receiver.recv()
    print(item)

if __name__ == '__main__':
    # 양방향
    # ps, pr = multiprocessing.Pipe()
    # 단방향(한쪽은 데이터를 받고 다른 한쪽은 보낼수만 있다)
    ps, pr = multiprocessing.Pipe(False)
    p1 = multiprocessing.Process(target=pro1, args=(ps,))
    p2 = multiprocessing.Process(target=pro2, args=(pr,))

    p1.start()
    p2.start()