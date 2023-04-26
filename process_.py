import os
from multiprocessing import Process


# pid값 출력하기
# print('hello os')
# print('my pid is', os.getpid())

def foo():
    print('child process', os.getpid()) # 자식 프로세스 pid 
    print('my parent is', os.getppid()) # 부모 프로세스 pid


    # 여기서부터 실행해
if __name__ == '__main__': 
    print('parent process', os.getpid()) # 18224

    # child1 = Process  →  child1이라는 새로운 프로세스를 만들 것
    # (target = foo)    →  foo를 실행하는 프로세스
    # .start()          →  만들면 바로실행해
    child1 = Process(target = foo).start() 
    # child process = 21336 , my parant is = 18224
    child2 = Process(target = foo).start()
    # child process = 3252 , my parant is = 18224
    child3 = Process(target = foo).start() 
    # child process = 7356 , my parant is = 18224


def foo():
    print('This is foo', os.getpid())

def bar():
    print('This is bar', os.getpid())
    
def baz():
    print('This is baz', os.getpid())

if __name__ == '__main__':
    print('parent process', os.getpid())
    child1 = Process(target = foo).start() # 18600
    child2 = Process(target = bar).start() # 20552
    child3 = Process(target = baz).start() # 19524
    
# 3개 중 하나가 문제가 생겨도 다른 프로세스에 영향을 주지 않는다.
