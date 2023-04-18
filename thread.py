import threading
import os


def foo():
    print('thread id', threading.get_native_id()) # 스레드 id
    print('process id', os.getpid())              # 프로세스 pid


# 동일한 작업을 하는 스레드 생성하기
if __name__ == '__main__':
    print('process id', os.getpid())  # process id 14164

    # thread1 = threading.Thread  →  thread1이라는 새로운 스레드를 만들 것
    thread1 = threading.Thread(target=foo).start()  
    # process id 14164 , thread id 22200
    thread2 = threading.Thread(target=foo).start()
    # process id 14164 , thread id 10036
    thread3 = threading.Thread(target=foo).start()
    # process id 14164 , thread id 19470

# 세개의 각기 다른 스레드지만, 같은 프로세스를 공유하기 때문에 스레드 id는 모두 다르고, 프로세스 id는 동일하다


def foo():
    print('This is foo')


def bar():
    print('This is bar')


def baz():
    print('This is baz')


# 각기 다른 작업을 하는 스레드 생성하기
if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()  
    thread2 = threading.Thread(target=bar).start()  
    thread3 = threading.Thread(target=baz).start()  

# 당연하게도 스레드ID는 다르고, PID 값은 모두 동일하다. 