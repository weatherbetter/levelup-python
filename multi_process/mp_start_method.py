import multiprocessing

def start_process():
    return 1

if __name__ == '__main__':
    # p1 = multiprocessing.Process(target=start_process)
    # p1.start()

    # print(multiprocessing.get_start_method()) # spawn

    multiprocessing.set_start_method('spawn')