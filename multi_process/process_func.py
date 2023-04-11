from multiprocessing import Process

def hello(arg1, arg2):
    print("hello Process")

if __name__ == '__main__':
    p1 = Process(target=hello, args=('123',), kwargs=dict(arg2='456'))
    p1.start()
    p1.join() # 앞 프로세스가 끝날때까지 대기가 필요할 경우
    p1.terminate() # 종료가 필요할 경우