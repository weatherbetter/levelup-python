from multiprocessing import Process

class HelloProcess(Process):
    def __init__(self, arg1, arg2):
        super(Process, self).__init__()
    
    def run(self):
        print("hello Process")

if __name__ == '__main__':
    p1 = HelloProcess(1, arg2 = "Hello")
    p1.start() # run 메서드를 찾아서 실행
    p1.join() # 앞 프로세스가 끝날때까지 대기가 필요할 경우
    p1.terminate() # 종료가 필요할 경우