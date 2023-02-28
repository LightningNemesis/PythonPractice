## Python Data Structures to JSON:
```
https://www.python-engineer.com/courses/advancedpython/11-json/?query=JSON
```


## Process
An instance of a program (e.g. a Python Interpreter)

Pros:
+ Utilizes advantage of multiple CPUs/cores
+ Separate memore space -> not shared between processes
+ New process is isolated/independent from other processes
+ Processes are interruptable i.e. can be killed

Cons:
- Heavyweight
- More time for starting a process than a thread
- More memory '''
- inter Process Communication (IPC) is complicated

## Threads
An entity of a process: can be scheduled
Note: A process can spawn multiple threads

Pros:
+ Lightweight
+ Can be started faster than a process
+ Great for I/O tasks (talking to slow devices)

Cons:
- Limited by GIL: Only 1 thread at a time 
- Shares the same memory space
- Not iterruptable/killable
- Need to be careful with race conditions: since common memory space, 2 threads can attempt to modify same variable (race condition)


Global Interpreor Lock (GIL):
- Allows only 1 thread to run at a time in python (in cpython)

Workaround:
- Use multiprocessing
- Free threaded Python implementations : Jython, IronPython
- use python wrappers for third party libraries: Numpy, scipy




 
