# Asychronours exection
import time
import threading
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_characters():
    for i in ['A', 'B', 'C', 'D', 'E']:
        print(i)
        time.sleep(1)
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_characters)
thread1.start()
thread2.start()

print(f"Is thread1 alive? {thread1.is_alive()}")  # True

thread1.join()
thread2.join()

print(f"Is thread1 alive? {thread1.is_alive}")
print("All threads executed..")
#-----------------------------------------------------------------------------------

# we can give name for threads..
import threading
def print_hello():
    print(f"Hello from {threading.current_thread().name}!")

# creating a thread with name
thread = threading.Thread(target=print_hello, name = "MyThread")
thread.start()          # Hello from MyThread!

#---------------------------------------------------------------------------------------------------------------

# daemon thread:- it z  a thread which will leaves automaticaly when "Main thread" leave d program
import threading
import time
def background_task():
    while True:
        print("Background task running...")
        time.sleep(1)
# create a daemon thread
thread = threading.Thread(target = background_task)
thread.daemon = True    # set d thread as a daemon
thread.start()

# main prgm ends here
time.sleep(3)
print("Main prgm ends.")
'''
Background task running...
Background task running...
Background task running...
Main prgm ends.
'''
#----------------------------------------------------------
'''
d/f methods in this are:---
 1) start()
 2) join() :-- it will wait for all threads to execute and thn go nxt task..
 3) is_alive() :--- gives True or False

'''