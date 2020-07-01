# In the Python as in the JS also exist linked types and simple types, but in the Python compare of linked type can return True, because in some cases it can compare via value
# In Python do not exist constan variable, or if exist it is not use very often, and architecture of language allow do not have constants

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# # Some tricks
# def a(to_add, ent=[]):
#     ent.append(to_add)
#     return ent


# # Python does not re-initialized as an empty set — it used previous value
# print(a(1))
# print(a(1))
# print(a(1))

# # That's why use it
# def aa(to_add, ent=None):  # non required arg
#     if not ent:
#         ent = []
#     ent.append(to_add)
#     return ent


# print(aa(1))
# print(aa(1))
# print(aa(1))

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# In python when you import file or module it executes firstly as in js, and from this file or module exports all that was declare in it, and even import but by keyword

# # in aaa.py
# # # =================
# # const2 = 2

# # print(222)
# # # =================

# # in aa.py
# # # =================
# # import aaa

# # const = 1

# # print(aaa.const2)
# # print(123)
# # # =================

# import aa

# print('here')
# print(aa.const)
# print(aa.aaa.const2)
# print('end')

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# import random


# class Game:
#     def __init__(self, guess_word):
#         self.word = guess_word
#         self.list_word = []
#         for w in self.word:
#             self.list_word.append(w)
#         self.temp = 10
#         self.res = False

#         print('Your guess:')
#         while(self.temp != 0 and not(self.res)):
#             self.res = self.analyse(input())
#             self.temp -= 1

#         if self.res:
#             print('You are win!')
#         else:
#             print('You lose. The word was: ' + self.word)

#     def analyse(self, word):
#         if self.word == word:
#             return True
#         else:
#             print('In word \'' + word + '\' ' + str(self.compare(word)) + ' letter compares')
#             return False

#     def compare(self, my_word):
#         count = 0
#         copy_word_list = self.list_word.copy()
#         for w in my_word:
#             if w in copy_word_list:
#                 copy_word_list.remove(w)
#                 count += 1
#         return count


# def word_creator():
#     alphabet = 'ABCDEFGHIKLMNOPQRSTVXYZ'.lower()
#     res_word = ''

#     for _ in range(random.randint(5, 7)):
#         res_word += alphabet[random.randint(0, 22)]

#     return res_word


# win_word = word_creator()
# print(win_word)
# Game(win_word)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# def call_it(some_param=None):
#     if some_param:
#         return some_param
#     else:
#         pass


# print(call_it())
# print(call_it(some_param=2))
# print(call_it(3))

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# class Person:
#     def __init__(self, f_name, l_name):
#         self.firstname = f_name
#         self.lastname = l_name

#     def print_full_name(self):
#         print(self.firstname, self.lastname)  # print each variable between ' ' (space)


# class Man(Person):
#     def __init__(self, name, last_name):
#         super().__init__(name, last_name)
#         self.two_name = f'man {name}'
#         self.two_last = f'man {last_name}'

#     def print_full_name(self):
#         print('mr.', self.firstname, self.lastname)


# class Woman(Person):
#     def __init__(self, name, last_name):
#         super().__init__(name, last_name)
#         self.two_name = f'woman {name}'
#         self.two_last = f'woman {last_name}'

#     def print_full_name(self):
#         print('ms.', self.firstname, self.lastname)


# class Mid(Person):
#     def __init__(self, name, last_name):
#         super().__init__(name, last_name)
#         self.two_name = f'mid {name}'
#         self.two_last = f'mid {last_name}'

#     def print_full_name(self):
#         print('mid.', self.firstname, self.lastname)


# class Student(Mid, Man, Woman):
#     def __init__(self, f_name, l_name, age):
#         # assign self of Person to self of Student # put parameter self in __init__ method in first position by default, in each method of class
#         super().__init__(f_name, l_name)  # call at first Woman then Man and then Mid (from right to left)
#         self.age = age


# s = Student('big', 'man', 12)
# s.print_full_name()
# print(s.two_name)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# from string import Template

# one_start = 'Hello'
# one_end = 'world'
# print(Template('$a $b').substitute({'a': one_start, 'b': one_end}))


# class MyTemplate(Template):
#     delimiter = '#'


# two_start = 'Bye'
# print(MyTemplate('#a #b').substitute({'a': two_start, 'b': one_end}))

# three_start = 'One'
# three_end = 'more'
# print(f'{three_start} {three_end}')


# name = 'Eric'
# print('Let\'s talk about {}.'.format(name))
# print('Let\'s talk about {} and {}.'.format(name, 'Smith'))  # format in the order
# print('Let\'s talk about {0} and {1}. {0} is starts on E'.format(name, 'Smith'))  # format in by index
# last_name = 'Evans'
# age = 12.1
# print('Hello, %s %s, I am %s.' % (name, last_name, age))  # s - string
# print('Hello, %s %s, I am %d.' % (name, last_name, age))  # d - digits
# print('Hello, %s %s, I am %f.' % (name, last_name, age))  # f - float
# print('Hello, %s %s, I am %.3f.' % (name, last_name, age))  # this is specific float with 4 digits after comma

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# # compile is encourager
# print('check, if it starts ti execute, if you see it in console, this error is in runtime, if no, this error on compile time')


# def type_check(one: str, two: int, three: bool): # it does not work
#     print(one)
#     print(two)
#     print(three)


# type_check('word', 123, True)
# type_check('word', 'moon', True) # it do not throw an exception

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# from argparse import ArgumentParser # as I understood, mostly work with sys.argv


# def factorial(num: int, res: int = 1):
#     if num == 1:
#         return res
#     return factorial(num-1, res*num)


# parser = ArgumentParser()

# # adding multiple arguments
# parser.add_argument('process', help='operation to do')
# parser.add_argument('num', help='count factorial', type=int)
# parser.add_argument('-l', help='loging to console', action='store_true', default=False)
# parser.add_argument('-o', help='output result to file', action='store_true', default=False)

# # parse args which I allow and store it
# args = parser.parse_args()  # it allow run a validation in console and add to argument 'help'

# if args.process == 'go':
#     res = factorial(args.num)
#     if args.l:
#         print(res)
#     if args.o:
#         f = open('results', 'a')
#         f.write(f'factorial of {str(args.num)} is {str(res)}\n') # has to be closed, but if process will soon be close, it is not necessary
#         f.close()


# --------------------------------------------------------------------------------------------------------------------------------------------------------

# import re

# print(re.match('^as Always [a-zA-Z]*$', 'As always here', re.I).group(0)) # re.I means ignore lowercase or UPPERCASE

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# print('\\')
# print(r'\\') # raw string
# print(f'\\') # the same as first, but can have dynamic value in {}
# moon = 123
# print(f'''man is on the street
# {moon}
# i am at home
# ans want to walk
# really want(((
# ''') # multi line assignment

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Some tricks ))

# a = b = c = 1
# # a == 1
# # b == 1
# # c == 1

# our_list = [1, 2, 3]
# a, b, c = our_list
# # a == 1
# # b == 2
# # c == 3

# a, b = (1, 2)
# # a == 1
# # b == 2
# a, b = b, a
# # a == 2
# # b == 1

# # all() in Python as every() in JS
# # any() in Python as some() in JS
# all_true = [True, True, 1, 'hello']
# any_true = [0, False, True, '', []]
# all(all_true) == True
# any(all_true) == True
# all(any_true) == False
# any(any_true) == True

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# ===================
#   TUPLE DATATYPE
# ===================

# def bar():
#     print(1)


# # tuple is unique obj, you can not add or remove from it, and change value, at least by link, value which will not change his link after modifying can be changed (list)
# uniq_tuple = (123, 'foo', [1, 2, 3], bar)
# # uniq_tuple.append('abc') # throw an error
# # uniq_tuple.remove(123) # throw an error
# # uniq_tuple[1] = 1234 # throw an error
# uniq_tuple[2].append(4)  # good
# print(uniq_tuple)

# print(uniq_tuple[0])  # first
# print(uniq_tuple[-1])  # last

# tuple2 = uniq_tuple[2:]
# print(tuple2)  # slice from 2 index to last (including 2 index)

# tuple3 = uniq_tuple[:2]
# print(tuple3)  # slice from first to 2 index (not including 2 index) (total count in tuple is to what index were slicing)

# tuple4 = tuple3 + tuple2  # <tuple> + <list> will throw an error
# print(tuple4)
# print(tuple4 == uniq_tuple)  # sequence is necessary or False

# # So index before ':' is including, index after ':' is excluding

# tuple5 = uniq_tuple[1:3]  # from 1 to 2 (including)
# print(len(tuple5))  # 2
# print(tuple5)

# tuple6 = uniq_tuple[:]  # all
# print(tuple6)
# print(tuple6 == uniq_tuple)

# tuple7 = uniq_tuple[::2]  # with :: index is adding to 0 or -1 and pull from tuple by index (step pull)
# print(tuple7)  # first 0, then 0+2=2, then 2+2=4 (4 not in tuple)

# tuple8 = uniq_tuple[::-2]
# print(tuple8)  # first is -1, then -1+(-2) = -3, then -3+(-2)=-5 (-5 not in tuple)

# # So we can reverse uniq_tuple simple by:
# tuple9 = uniq_tuple[::-1]  # reverse
# print(tuple9)

# # method
# print(len(uniq_tuple))
# print(uniq_tuple.count(123))  # exac value to count
# print(any(uniq_tuple))  # any ask is iterable
# print(any(()))  # False
# print(tuple([1, 2, 3, 4]))  # convert to tuple any iterable object
# arr = tuple([1, 2, 3, 4])
# print(max(arr))
# print(min(arr))
# print(sum(arr))

# print(arr[::-1])
# print(tuple(sorted(arr[::-1])))  # return list, so need to convert back to tuple

# (one, two) = arr[::-1][:2]  # js destructuration )))
# # [one, two] = arr[::-1][:2] # also good
# print(one, two)  # 4 3
# [one2, two2] = list(arr[::-1][:2])
# # (one2, two2) = list(arr[::-1][:2])
# print(one2, two2)  # 4 3

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# a = [1, 2, 3, 4]
# a.append([5, 6])
# print(a)

# a.pop()
# print(a)

# a.extend([5, 6])  # as a 'concat' in js
# print(a)

# a.insert(-2, 7)  # first is an index, and it can be even negative
# print(a)

# print(a.copy())

# print(a.count(1))

# # =======================
# print(type(a.__str__()))
# print(a.__dir__())  # exists method
# print(a.__len__())
# # and so on ...
# # =======================

# print(a.clear())
# print(a)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# def generator_func(word: str):  # generator as in js
#     for letter in word:
#         yield letter


# for letter in generator_func('biiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiig word'):
#     print(letter, end='')  # you can define end of printing ( you can not do it in js :) )

# print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# # # # Will not work
# # # p_func = def ():
# # #     print('Hi')

# # def p_func():
# #     print('Hi')


# # p_func()

# # same_p_func = p_func

# # same_p_func()

# const = ['bar', '', 0]

# # lambda is a short representation of def func, like (x,y)=>x+y in js (in this example '{}' should not exist)
# # lambda is a anonymous function (as an callback in js)
# bool_const = list(tuple(list(map(lambda x: bool(x), const)))) # just want to check is it possible to convert multiple times

# print(bool_const)
# # # wrong
# # try_p_func = def ():
# #     print('Hi')

# # def_lambda = lambda x, y: x + y # will also work!
# # print(def_lambda(5,55)) # 60

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Multithreading old ))

# # It will work because it import 'c' library for working with thread, but python by itself can not work with thread, all that it can do you can check without importing library (math, loop, operators and so on, it is really less functionality), or library which work only with python code
# # It works because it is a crypto functionality and in python as in node it can be works in separate thread, also in separate thread may works a file operation, like read or write
# import threading
# import bcrypt


# def toUnicodeObj(string):
#     return string.encode('utf-8')  # it == to b`${string}` (js string-template)


# passwords = ('password1234', 'iphone10rx256gb', '1q2w3e4r', 'q1w2e3r4')
# # map return <map object> tuple convert it to <tuple object> => ('foo', ...)
# array_of_pass = tuple(map(toUnicodeObj, passwords))
# passwords_uni = (b'password1234', b'iphone10rx256gb', b'1q2w3e4r', b'q1w2e3r4')

# # print(array_of_pass == passwords_uni) # True


# def hash_it_and_do_any(password):
#     hashPass = bcrypt.hashpw(password, bcrypt.gensalt())
#     print(bcrypt.checkpw(password, hashPass))


# for password in array_of_pass:  # passwords_uni also suitable
#     # without ',' python think I give 8 args, I dunno why, maybe ',' say end of the args, and do not allow put default args
#     threading.Thread(target=hash_it_and_do_any, args=(password,)).start()  # in multithread
#     # hash_it_and_do_any(password)  # sync

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# # It will not work, since it is not crypto functionality, so will work just like async code (maybe)
# import threading
# import random
# import time

# start = time.time()


# def count(times):
#     res = 0
#     for i in range(times):
#         res += i
#     print(f'Rusult of counting is {res}, in {time.time() - start}')


# for _ in range(5):
#     t = threading.Thread(target=count, args=(random.randint(50000000, 90000000),))
#     t.start()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# # Multithreading in Python I would like to compare with async i\o in node, when it put executing of some functionality to another thread in node (since it write on c++)
# # When I say some functionality, I mean all async code, and with await we just wait for result of it execution (like result method for thread in Python)
# import threading
# import time

# threads = []


# def sleep():
#     print('start sleeping for 1 sec')
#     time.sleep(1)
#     print('finish sleeping')


# for _ in range(5):
#     t = threading.Thread(target=sleep)
#     t.start()
#     # t.join() # will do all synchronous, since start and immediately join to main thread
#     threads.append(t)

# for thread in threads:
#     # as far as I understood in threading module exist class call Lock, which do the same think, it just join to main thread automatically and immediately
#     thread.join()

# print('Program is done')

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Multithreading ))

# from concurrent.futures import ThreadPoolExecutor
# import time


# def sleep(sec_to_sleep: int):
#     print(f'start sleeping for {sec_to_sleep} sec')
#     time.sleep(sec_to_sleep)
#     print('finish sleeping')
#     return f'I was sleeping for a {sec_to_sleep} but now I am peppy'


# # by with keyword it allow you to use thread as ThreadPoolExecutor(), because it assign it to variable under the hood (thread = ThreadPoolExecutor())
# with ThreadPoolExecutor() as thread:  # with - it is a keyword which declere a cell with ending which, force call a necessary method (in this case it call some sort of join (in threading module it join to main thread) to bound to main thread, for not allow main thread to spot until child is working)
#     res = []
#     secs = (5, 3, 1, 4, 2)
#     threads = [thread.submit(sleep, sec) for sec in secs]
#     # threads = (thread.submit(sleep, 2) for _ in range(10)) # I dunno why, but tuple do not run executing of threads
#     for runs_thread in threads:
#         # withot it start executing of each thread immediately without wait for finishing the previous one
#         # it works, because I want to get a results of executing threads and do something with it in this (main) thread, or may be build upon it result next thread
#         res.append(runs_thread.result())


# for r in res:
#     print(r)

# print('Main thread ends')

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Process old ))

# # Multiprocesses is very like a thread in implementation in Python, but this totally different
# # Process has no access to memory of main process, but thread has
# # Do not confuse it with process in node, because in Python subprocesses is like a process in node
# import multiprocessing
# import time


# def lets_have_a_sleep(sec_to_sleep):
#     print('Start sleep...')
#     time.sleep(sec_to_sleep)
#     print('Finish sleep...')


# multiprocessing.Process(target=lets_have_a_sleep, args=(2,)).start()
# multiprocessing.Process(target=lets_have_a_sleep, args=(3,)).start()

# print('Finish script')

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Process ))

# from concurrent.futures import ProcessPoolExecutor
# import time
# import random


# def lets_have_a_sleep(sec_to_sleep, uniq):
#     print(f'({uniq}) Start sleep for {sec_to_sleep}...')
#     time.sleep(sec_to_sleep)
#     print(f'({uniq}) Finish sleep...')


# with ProcessPoolExecutor() as executer:  # by this, it makes join automatically
#     # for sec in [random.randint(1, 5) for _ in range(5)]:
#     #     # in Python if you try to use function before declare it, you get an error
#     #     executer.submit(lets_have_a_sleep, sec) # start

#     # create as many process as item in args and start it (map instead loop), and with attach it to main process, for waiting next execution until all process in with cell will finish
#     # when you use range you do not include last number, but start from 0 (as in all programing langs), as in list or tuple slicing
#     executer.map(lets_have_a_sleep, [random.randint(1, 5) for _ in range(5)], (i for i in range(5)))

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Subprocess ))

# Subprocess can run bash scripts or another executable file and manage their data by message

# some.sh
# ================
# # /bin/bash
#
# echo 'Hello Man'
# ================

# import subprocess
# import sys

# # # here you are write command with python performance and directly to shell, but python performance only in finding main command
# # p1 = subprocess.run('ls')
# # print(p1.args)  # -- ^^ (exactly what you put)

# # # with shell=True it will write directly to shell, instead use Python for more finding main command and file with nested command for main command
# # # write directly to shell, but without Python performance
# # p3 = subprocess.run('bash /home/ander/Desktop/some.sh', shell=True)

# # # write directly to shell (list have to be, because Python do understood when its has to looking for command and when exactly file or nested command)
# # # write directly to shell, but with Python performance, and this performance force you to write command in list
# # p2 = subprocess.run(['bash', '/home/ander/Desktop/some.sh'])  # tuple also appropriate
# # print(p2.returncode)  # 0 - successful exit

# # # With capture_output=True appear 2 new property in returned object from execution subprocess, is - stdout and stderr
# # process_out = subprocess.run(['bash', '/home/ander/Desktop/some.sh'], capture_output=True)  # subprocesses runs in sync
# # # But out is encoded (that's why 'b' before string in out)
# # # if stderr empty string, then returncode 0, if not empty, then error occurred
# # print(process_out.stdout.decode(), end='')  # end='' since in out in the end already exist '\n'

# # process_out = subprocess.run(['bash', '/home/ander/Desktop/some.sh'],
# #                              capture_output=True, text=True)  # just make out decoded
# # print(process_out.stdout, end='')

# # # capture_output return stdout and stderr together, this make the same thing under the hood, but here we want get exactly stdout, without stderr
# # process_out = subprocess.run(['bash', '/home/ander/Desktop/some.sh'], stdout=subprocess.PIPE, text=True)
# # print(process_out)

# # with open('/home/ander/Desktop/some', 'a') as file:
# #     subprocess.run(['bash', '/home/ander/Desktop/some.sh'], stdout=file,
# #                    text=True)  # stdout can be any of output, even file

# # subprocess.run(['bash', '/home/ander/Desktop/some.sh'], stdout=sys.stdout, text=True)

# # subprocess.run(['bash', '/home/ander/Desktop/some.s'], check=True)  # allow print if error was occur

# # we just work with stream, in bash, it is like - 'bash /home/ander/Desktop/some.sh | grep Man'
# # ------------------------------------------------ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ <- this is input for 'grep Man'
# p1 = subprocess.run(['bash', '/home/ander/Desktop/some.sh'], stdout=subprocess.PIPE, text=True)
# print(subprocess.run(['grep', 'Man'], capture_output=True,
#                      text=True, input=p1.stdout.replace(' ', '\n')).stdout, end='')

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( os module ))

# import os  # this module, is like process object in node, by this we can manipulate on runing environment or get info of it

# print(dir(os)) # shows all method and and property in class instance (maybe)
# # os.getcwd()
# # os.chdir()
# # os.mkdir()
# # os.makedirs() # create with nested
# # os.listdir()
# # os.rmdir()
# # os.removedirs() # remove with nested
# # os.rename()
# # os.renames() # rename with nested
# # os.stat() # status of file

# # for i in os.walk('/home/ander/Desktop'): # this go though all folder and print all nested files and folder, while folder ends
# #     print(i)

# # os.cpu_count()

# # print(os.environ.get('mode'))  # env on local pc  # case sensitive (MODE)

# # os.path # manipulation or info of path in pc
# # print(dir(os.path))

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( sys module ))

# import sys  # sys and os functionality in node covers by process object

# # working with stream
# # sys.stdout
# # sys.stderr
# # sys.stdin

# # it returns args what you pass in running python command (python3.8 alg.py), you can past - 'python3.8 alg.py start', and then sys.argv will have ['alg.py', 'start']
# print(sys.argv)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( try-catch ))

# # 'block' and 'cell' word is the same

# # def call_it():
# #     try:
# #         # 1/0
# #         print(''+1)
# #     except ZeroDivisionError as z_error:  # catch exact Error type
# #         print('Learn math!')
# #         return 'Error occurred'
# #         print('This print after returning')
# #     except:  # general catch, this cell catch another Error type, which did not catch previous except cell, if general except write before except with particular Error type, those except will never excute, since except before it handel all errors
# #         print('There was an error')
# #         return 'Error occurred'
# #         print('This print after returning')
# #     else:
# #         return 'All looks good'
# #         print('This print after returning')
# #     finally:
# #         print('Last cell')
# #         return 'End'
# #         print('After end returning')

# # def call_it():
# #     try:
# #         # print(''+1)
# #         # raise 'Some Error'  # it is not allowed, only exact Error (BaseException is base for all Exception which can be arise)
# #         raise Exception('A lot of error', 'and pain')  # it allow you to raise an error by yourself
# #     except ZeroDivisionError as z_error:
# #         print('Learn math!')
# #         return 'Error with zero occurred'
# #         print('This print after returning')
# #     except BaseException as error:  # BaseException is a main Exception type, from which extends all other Except
# #         print('There was an error')
# #         print(error)  # for using error you have to define it in except block (cell) (BaseException is a base for all exception, so you can use it)
# #         return 'Some Error occurred'
# #         print('This print after returning')
# #     else:
# #         return 'All looks good'
# #         print('This print after returning')
# #     finally:
# #         print('Last cell')
# #         return 'End'
# #         print('After end returning')

# # def call_it():
# #     try:
# #         print(1+'')
# #     # if excepts blocks will not handle raised error, then this error will just arise (you should not allow happen it), in this example it will handle finally block, but it not the best way to handle error (always write general except cell to handle it)
# #     except ZeroDivisionError as z_error:
# #         print('Learn math!')
# #         return 'Error with zero occurred'
# #         print('This print after returning')  # never, since after return
# #     else:  # This cell will execute, if try block does not arise an error
# #         print('Try did not arise an error')
# #         return 'All looks good'  # you will never return it, since in finally exist his return, and those return will always execute last
# #         print('This print after returning')  # never, since after return
# #     finally:
# #         print('Last cell')
# #         return 'End'
# #         print('After end returning')  # never, since after return

# # def call_it():
# #     try:
# #         # 1/0
# #         # print(1+'')  # arise an error, since cell for handle this error is not here
# #         print(1) # else block executes
# #     except ZeroDivisionError as z_error:
# #         print('Learn math!')
# #         return 'Error with zero occurred'
# #         print('This print after returning')
# #     else:
# #         print('Try did not arise an error')
# #         return 'All looks good'
# #         print('This print after returning')


# # call_it()

# def call_it():
#     try:
#         print(1/0)
#     except ZeroDivisionError as z_error:
#         print('Learn math!')
#         # return 'Error with zero occurred'
#         # if you raise another error in except block, it will raise two error, and the last one will be, what you arise in except block, and you can handle it then, in except block, handle the last one error (you should handle it then, because double error hard to read and hard to find place where occurred)
#         raise Exception('Error with zero occurred')
#     else:
#         print('Try did not arise an error')
#         return 'All looks good'
#         print('This print after returning')
#     finally:  # finally block allways execute, if error arise, or if all works fine, even if 'return' pass in previous cell and even if raise error was execute in except block
#         print('Last cell')
#         return 'End'
#         print('After end returning')


# # try/catch for handle raise of error in 708 line (when it is on line 719), but it will appear in finally block will be comment
# try:
#     print(call_it())
# except BaseException as err:
#     print(err)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( List or tuple ))

# print([1, 2, 3]+[4, 5]) # concat

# root_elem = [1, 2, 3, 4, 5]

# mapped_elem1 = [x*x for x in root_elem]  # list comprehension
# mapped_elem2 = list(map(lambda x: x*x, root_elem))  # list() return list where each elem is an elem in iterable param

# print(mapped_elem1)
# print(mapped_elem2)

# # as a map and filter in js
# mapped_elem3 = [x*x for x in root_elem if x*x % 2 == 0]
# mapped_elem4 = [x for x in [y*y for y in root_elem] if x % 2 == 0]
# mapped_elem5 = list(map(lambda y: y*y, filter(lambda x: x % 2 == 0, root_elem)))

# # this is the same
# # print(mapped_elem3 == mapped_elem4)  # True
# print(mapped_elem3)
# print(mapped_elem4)
# print(mapped_elem5)

# mapped_elem6 = [(x, y) for x in 'abcd' for y in [1, 2, 3, 4]]
# print(mapped_elem6)

# # so here what I understood, if two for in comprehension then you can iterate them and make one elem with iteratable data type
# # this will not work if instead range we get random digits (not 1,2,3,4 but 5,3,7,1) so here is come zip() func
# mapped_elem7 = [r for r in [(x, y) for x in 'abcd' for y in [n+1 for n in range(4)]] if r[1] == 'abcd'.index(r[0])+1]
# print(mapped_elem7)

# mapped_elem8 = zip('abcd', [5, 2, 4, 9, 7])  # 7 will ignore, as well as if letter would be more
# print(list(mapped_elem8))

# # In Python dictionary as a key can not only a string, like in JS, but also an object, digits and so on
# mapped_elem9 = {letter: num for letter, num in zip('abcd', [5, 2, 4, 9, 7])}  # here 7 will ignore as well
# print(mapped_elem9)

# mapped_elem10 = {letter: num for letter, num in mapped_elem7 if num != 4}  # comprehension with dictionary
# print(mapped_elem10)

# # {1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8} the same if:
# print(list(set([1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8])))  # make original list by set

# # set data structure has brackets as a dictionary, but withot key, make value unique
# # you can think, in dictionary key is unique, but value don't, so in set key is a value, but set also sort it
# mapped_elem11 = {x for x in [1, 4, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8]}  # uniq and sorted
# print(mapped_elem11)


# def map_generator(num):
#     for n in num:
#         yield n*n


# # generator could replace map and filter and all another same functionality
# mapped_elem12 = list(map_generator(root_elem))  # generator is iterable
# print(mapped_elem12)


# def reduce_generator(word, iterable_keys):
#     for i in range(len(word)):
#         yield (word[i], iterable_keys[i])


# mapped_elem13 = reduce_generator('abcd', '76542')  # 2 ignore, as in zip()

# # convert to dictionary
# print(dict(mapped_elem13))
# print(dict([(1, 1), (2, 2)]))  # in dict key could be str or int
# print(dict([['1', 1], ['2', 2]]))
# print('abcd'[1])  # you could pass index to every iterable object

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( iterable and iterator ))

# arr = [1, 2, 3, 4]
# # we can count the len of a list because it is iterable, but no every iterable object can count its length
# print(arr.__len__())  # this method call special or dunder method
# print('__iter__' in dir(arr))


# def f():
#     yield 1
#     yield 2


# # print(f().__len__())  # raise error (f() return generator)

# # if not every iterable object has __len__ method, but __iter__ method has every iterable object, because when we iterate through iterable object we call exact it method
# print('__iter__' in dir(f()))

# print(f())  # return generator
# iterator = f()  # assign to variable, for do not create new state of iterator, because it will always get fist value of iterable object
# # iterator = iter(f())  # the same, since __iter__ method return just self (since self is iterator and iterable)
# while True:
#     try:
#         print(next(iterator))  # change iterator state, that it has already get one object from iterable object
#     except StopIteration:  # when you call next() to the iterator, which has already achieve last value of iterable object, it arise an StopIteration error
#         break

# iter_arr = iter(arr)
# print(next(iter_arr))
# print(next(iter_arr))
# print(next(iter_arr))
# print(next(iter_arr))
# # print(next(iter_arr))  # once get to this point raise the exception and stop thread
# # print(next(iter_arr))  # this also redundant
# # print(next(iter_arr))  # this also redundant
# print('next(iter_arr)')

# # ================================================================================================================================================================================================================================================================
# # So iterable object its an object which has dunder method __iter__, and this method return an object which implement functionality of saving state on which one value it stop to iterate the iterable object.
# # This object, which iterable object return by calling __iter__ method, call iterator, and its has another dunder method, which call __next__, it calls for the object which return this iterator and this iterator remember which amount of value it already get.
# # And if iterators call next, when all values from iterable object ends, iterators has to arise an StopIteration error.
# # One object can be iterator and iterable at one time, in this case on __iter__ method it has to return itself (self), as a generator.
# # ================================================================================================================================================================================================================================================================

# class MyIterableObj:
#     def __init__(self, a: int, b: int):
#         self.value: int = a + b
#         self.times: int = 1
#         self.max_times: int = b

#     def __iter__(self):  # I think, 'self' param is required, because python understood to which class this method assign (since self is a link to the exact class, where you are, I think)
#         return self

#     def __next__(self):  # Or 'self' required, for using it inside method, and it put automatically, since it is method in class, and has to work with the properties in class (but what if I do not work with properties in class? <- (Then why this method should exist? Every method has to work with class properties))
#         if self.times > self.max_times:
#             raise StopIteration
#         self.times += 1
#         return self.value


# a = MyIterableObj(1, 5)  # show 1 + 5 (sum of param) value, 5 (second param) times
# for b in a:
#     print(b)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# # how to mutate tuple in Python)))
# a = (1, 2, 3, 4)
# a = list(a)
# a.append(5)
# print(tuple(a))

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( link to memory ))

# a, b, c = 1, '2', False
# d = [1, 2, 3, 4]


# def e():
#     print(1)


# class f:
#     def __init__(self, some_val):
#         self.one = some_val


# g = map(e, d)


# print(id(a))  # print id of a value stored in local memory
# print(id(b))
# print(id(c))
# print(id(d))
# print(e)
# print(id(e))
# print(id(f))
# print(g)
# print(id(g))

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( __name__ ))

# def a():
#     print('aaa')

# # This is using for calling function, if we execute this file, or if this file using only like a module, then we do not want to execute this function on global level, and prefer only to export defined variable, it say to file only to declare variable, and do not execute any logic, if this is a module
# if __name__ == '__main__':
#     a()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( == vs is ))
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# # '==' compare with the value in the variable
# # 'is' compare id of a value
# print(a == b)  # True, since value is the same
# print(a == c)  # True, since value and even id is the same
# print(a is b)  # False, since link is different
# print(f'a: {id(a)}')
# print(f'b: {id(b)}')
# print(id(a) == id(b)) # False
# print(a is c)  # True, since link is the same

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Scopes ))

# 'arise', 'raise' or 'throw' is the same
# 'error' and 'exception' is the same

# Scope in Python works in way: local -> enclosing -> global -> build-in
# enclosing it when not a global but already not a local, for example it when function call inside another function
# if you reassign any variable on higher level, you lost previous functionality, if you reassign 'dir' function on local level, then on this level you will get only reassigned functionality, if on global you will use reassigned functionality only in this file, since in each file itself global scope
# So, do not reassign build-in function or global (from local or enclosing scope by 'global' keyword)

# import builtins  # this module is a reference to build-in variable
# import random  # add to global scope object random with variable defined in global scope in random.py (__init__.py in the case if this is module) file, since you can create any local scope, by having function in global scope

# # Proof of the exporting every variable from module, which declare on global scope
# # that's why we need something like '_' before nameing of variable, for saying do not use it, when export (like a private variable in module)
# print(random.Random().randint)  # ------------------ this is
# print(random._inst.randint == random.randint)  # --- the same

# print(builtins.dir == dir) #

# print(dir(builtins))
# print(builtins.dir(dir))  # --- the same
# print(dir(dir))  # ------------ the same
# print(dir.__dir__())  # ------- the same
# print([1, 2, 3, 4].__dir__())

# # from builtins import *  # After this import, we do not have build-in scope, since all build-in variable in the global level, besides builtins.vars()

# # build-in
# file = __file__

# # global
# d = 3


# def aa():
#     # enclosing
#     c = 2

#     def bb():
#         # local
#         print(c)  # get from enclosing scope
#         print(d)  # get from global scope
#         print(file)  # get from global scope
#         print(__file__)  # get from build-in scope

#     bb()


# aa()

# import random  # do not use it, just want to check is it make change to global scope

# x = 1


# def yy():
#     y = 2
#     print((globals()))  # prints global variable whenever it call
#     print(y)
#     print(x)


# yy()
# # print(y)  # raise an exception
# print(x)

# # This function uses global variable s
# def f(param):  # param is also in local scope, but defined in global
#     some = 1
#     print(some)
#     # print(s)
#     # s = 'Fuck it'

#     # you can use it s variable in function even before define it in global scope, but if you call this func before define it, you get an error, in the same way it works in js
#     # 'global' use for redefine variable in global level, since read it can in any way, this key word should not use, or you do something wrong, since it harder to follow definition of variables
#     global s  # you have to declare that in function will be global var before use it var
#     s = 'I love JS'  # since you say that s comes from global scope, then you redefine globals

#     # without global this variable will exist only in this scope, and after execution function will be gone, like 'some' in 916 line , when it on 926
#     global ss  # and it not only redefine existing variable, and also define new, which did not create in global scope, and now will be
#     ss = 'I love machine learning'


# # Global scope
# s = 'I love Python'
# f('macaco')  # since you use global s in this function, you redefine it, and also create new ss
# print(s)  # and now instead of 'I love Python' you get redefined 'I love JS'
# print(ss)  # new one, created from local scope via global keyword


# def b():
#     global c
#     c = 1


# def a():
#     print(c)


# b()
# a()

# aa.py
# ===================
# def lalala():
#     print(dir([]))
# ===================

# import aa
# import random


# def dir(*args, **kwargs):
#     return args


# aa.lalala() # works as typical dir() function, even if I reassign it in this file


# # Closure (backpack), like in js
# def a():
#     x = 'lalala'

#     def b():
#         print(x)
#     return b


# b = a()
# b()


# # nonlocal
# # closure in more nesting and with nonlocal and global keyword
# x = 1


# def muu():
#     # nonlocal x  # if nearest x is in global scope, then it will not take it, and arise an error as not found nonlocal 'x' variable in enclosing scope
#     global x
#     x = 1.5

#     def foo():
#         # nonlocal x  # arise an error since nearest x is global
#         x = 2

#         def bar():
#             # as far as I understand, if closure in Python solve the same issue, so each time when you define a function it gets hided __closure__ function in which saves local scope of a scope where it declare, including another 'closures', and when we use nonlocal it dig into first closure and looking for variable, if no, then into the next close, and when find just create variable with the same name in its local scope with the value which is a link to value which has variable pulled from the closure, and if variable is global, then it is no in closure, and nonlocal can not find it
#             nonlocal x  # redefine x on level higher or some levels higher, while not find it, but if nearest x is in global scope, then it will not take it, and arise an error as not found nonlocal 'x' variable in enclosing scope
#             x = 3
#             print(x)
#         bar()
#         print(x)
#     foo()
#     print(x)


# muu()
# print(x)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( IPython ))

# works only in IPython
# %run aa.py

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Tricks and tips ))

# a = '' or 0 or 11
# print(a)  # 11

# a = '' if '' else 11
# print(a)

# a = 2 and 1 and 3  # 3 ( as && in JS )
# print(a)

# _ make number easer to read
# print(10000000 is 10_000_000)  # print warning, but has the same link in memory
# print(f'{10_000_000:,}')

# # This is stupied
# a, b, *c = (1, 2) and [3, 4, 5, 6, 7]

# print(a)
# print(b)
# print(c)

# a, *c = (1, 2) and {'one': 1, 2: 22, 't': 'three', 'f': 5}
# c = [a] + c  # keys of dict
# for x in map(lambda key: {'one': 1, 2: 22, 't': 'three', 'f': 5}[key], c):
#     print(x)

# a, b, *c = list((1, 2)) + [3, 4, 5, 6, 7]
# a, b, *c, d = (1, 2) + tuple([3, 4, 5, 6, 7])
# a, b, *_, c, d = [1, 2, 3, 4, 5, 6, 7]  # '_' variable is a redandunt, by this possibility we can skip some value, which we do not need

# print(a)
# print(b)
# print(c)
# print(d)


# # In the Python, when we work with the instance, we can not get attribute from it in dynamic way, as with dictionary (dict[key]), we can get exact attribute only through the dot, but how it can be with dynamic key, here we have getattr, setattr and delattr
# def redefine_inst(inst, dict_to_define: dict):
#     for key, val in dict_to_define.items():
#         try:
#             getattr(inst, key)
#         except AttributeError:
#             setattr(inst, key, val)

#     del_keys = [key for key in filter(lambda x: x not in dict_to_define.keys(), inst.__dict__.keys())]
#     for del_key in del_keys:
#         delattr(inst, del_key)

# class Bar:
#     pass

# bar_instance = Bar()

# redefine_inst(bar_instance, {'beer': 3, 'juice': 5})
# redefine_inst(bar_instance, {'name': 'hohoho', 'juice': 6})

# print(bar_instance.__dict__)

# --------------------------------------------------------------------------------------------------------------------------------------------------------


# (( Keywords ))


# # to get quick info of exact keyword
# help('assert')


# # assert

# import asyncio
# assert 1 == 1  # it use more for tests
# # assert 1 == 2  # AssertionError


# AsyncIO
# # async - await

# # It works in Python totally in the same way as in JS
# async def foo():
#     return 1

# # since in Python event-loop is build in from 3.7 version (3.7+), in the worst case you have to create event-loop from asyncio module, by 'asyncio.set_event_loop'
# foo1 = asyncio.run(foo())
# print(foo1)


# # pass

# # equivalent to leave block clear
# def Some():
#     if 'some' == 'some':
#         return 'some'
#     else:
#         pass  # I think it's like return undefined in JS


# False
# Boolean negative


# None
# empty type and value


# True
# Boolean positive

# and
# as && in JS


# as
# Use with import and 'with' keyword, for assign returned value to the created variable


# break
# Uses in loop (for, while) for interapt executing


# continue
# Uses in loop (for, while) to step to the next iteration execution


# class
# Uses to create a class as in JS


# def
# Defined a function


# del
# delete variable or key in dictionary, or attribute in instance

# if
# if statement as in JS

# elif
# Not very good practice to use
# In case where 'if' did not work 'elif' define one more condition to execute another block of logic, as 'else if' in JS

# else
# Not very good practice to use
# In case where 'if' and 'elif' did not work 'else' define block of logic which will work in the worst case, as 'else' in JS


# try
# Define block of code, where error will handle in 'except' cell


# except
# catch an error to handle in, it can catch exact type error, to handel in the special way


# finally
# Part of 'try' statement, which will execute in any case, even if error was arise, or if try works fine, or even if try works fine and return a value


# for
# for loop with exact number of iteration


# from
# Part of import statement


# import
# Import another file (module) to the current file (module), which define new variable, where will be a dictionary of global variable in the imported file (module)


# global
# Scope defined keyword, which changed or create variable in the global scope

# nonlocal
# Scope defined keyword, which changed or create variable in the upper scope, arise an error if closer variable will be in global scope


# in
# Checks for existing elem in list, tuple, dict


# is
# Checks for the same link in memory


# lambda
# Like one line arrow function in JS


# not
# LIke '!' in JS


# or
# as || in JS


# raise
# Error arise, like 'throw' in JS


# return
# Return value from executed function


# while
# While loop, loop with no exact step of iterations


# with
# Statement for executing a functionality, and assign result of it executing to a value, and which in the end of itself cell executing call operation of exiting


# yield
# Keyword for generator, to return middle value in iterator


# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( with keyword ))

# # class DeadException(Exception):  # it create the class with the same functionality as Exception class has
# #     pass

# class DeadException(Exception):  # it is the same as Exception class, but except one one arg and have extra prop 'm' with message
#     def __init__(self, msg):
#         self.m = msg


# # This class can work with 'with' keyword, since has __enter__ and __exit__ right setted dunder method
# class Shit:
#     def __init__(self, ate):
#         self.clean_ass = True
#         self.stomach = f'~~~{ate}~~~'
#         self.pants_on = True
#         self.your_weight = 100

#     def prepare(self):
#         print('find a bush')

#     def ends_comming(self):
#         print('Screaming, because didn\'t find a paper')

#     def doing(self, weight: int):
#         self.clean_ass = False
#         print(f'Oh... A bunch of 80 kilo of {self.stomach}')
#         self.your_weight -= weight
#         if self.your_weight <= 0:
#             raise DeadException('You shit all yourself')

#     def __enter__(self):
#         self.prepare()
#         self.pants_on = False
#         return self  # What returns in __enter__ method, those will assigned to variable after 'as' in 'with' statement

#     # __exit__ dunder method invoke even if error was arise, that's why we need additional arguments. Additional arguments is for handle error, if __exit__ call because exception was raised, if not, this three args will be None
#     def __exit__(self, exc_type, exc_val, traceback):
#         if not exc_type or exc_type.__name__ != 'DeadException':
#             if self.clean_ass == False:
#                 self.ends_comming()
#             else:
#                 print('Couldn\'t...')
#             self.pants_on = True
#             print('Leave the place of the crime')


# try:
#     with Shit('Pizza') as lalala:  # 'lalala' become variable in global (or local) scope
#         lalala.doing(80)
#         lalala.doing(80)
#         lalala.doing(80)
# except DeadException as err:
#     print(err)
#     # print(err.m) # the same message which Exception will have in first index of args (args is a tuple), since DeadException accept only one args, that means in Exception will exist one element, and so: err == err.m

# print(f'Now you are {lalala.your_weight} kilo')

# exit()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Context ))

# The same functionality as before code has, but with contextlib module, decorator and generator

# import contextlib


# class DeadException(Exception):
#     pass


# class Shit:
#     def __init__(self, ate):
#         self.clean_ass = True
#         self.stomach = f'~~~{ate}~~~'
#         self.pants_on = True
#         self.your_weight = 100

#     def prepare(self):
#         print('find a bush')

#     def ends_comming(self):
#         print('Screaming, because didn\'t find a paper')

#     def doing(self, weight: int):
#         self.clean_ass = False
#         print(f'Oh... A bunch of {weight} kilo of {self.stomach}')
#         self.your_weight -= weight
#         if self.your_weight <= 0:
#             raise DeadException('You shit all yourself')

#     def start(self):
#         self.prepare()
#         self.pants_on = False

#     def finish(self, exc_type=None, exc_val=None, traceback=None):
#         if not exc_type or exc_type.__name__ != 'DeadException':
#             if self.clean_ass == False:
#                 self.ends_comming()
#             else:
#                 print('Couldn\'t...')
#             self.pants_on = True
#             print('Leave the place of the crime')


# @contextlib.contextmanager
# def shit(food):
#     shiting = Shit(food)
#     shiting.start()
#     yield shiting  # with this approach in generator func you have to have one yield and all that above executes before block of code in 'with' statement and all after in exit, yield returns value to the param with use in 'as' keyword in 'with' statement
#     shiting.finish()


# try:
#     with shit('Gumburger') as s:
#         s.doing(400)
#         s.doing(8)
# except DeadException as e:
#     print(e)

# print(f'You are {s.your_weight} in weight')

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Decorator ))

# In Python high-oreder function work as in JS, but not so agile like in JS (in a way of Python, like you can not assign function to variable in one line, you need to create a function and then link assign to variable), and call it like first-class function
# Python allow us work with first-class function us like in JS with high-order function because Python has the same work with closure as JS has


# def a():
#     def b():
#         print('a b')
#     return b
# a()() # WORKS!


# def my_d(original_func):  # decorator for func in Python get only one args, and this is an original function
#     print(original_func.__name__)

#     def stub():
#         pass
#     return stub  # Decorator has to return callable value


# @my_d
# def a():
#     print('aa')


# # actually prints a name of func, not what prints in function definition
# a()  # actually call decorator func, and in it you we can do whatewer you want, even stub it

# def my_d2(*args, **kwargs):
#     # print(args, kwargs)  # tuple and dictionary
#     # print(*args, **kwargs) # arise an error because in kwargs may exist key-value, which print function doesn't has

#     def decor(original_func):  # decorator executes before function declare, for declare it with decorator
#         def layer(*args2, **kwargs2):  # this is execute when we call function on which pass this decorator, and then we have in enclosing scope original func, and call it inside those func which decorator call instead of original, by this we can repeat logic of 'bind' method in JS, and context can define as well
#             return original_func(*args, *args2, **kwargs, **kwargs2)  # first ordinary args and then key-args
#         return layer
#     return decor


# @my_d2('a', d='d', q='q')  # first ordinary args and then key-args
# def a(a, b, c, d, *args, **kwargs):
#     print(kwargs['q'])  # want to get from context, which decorator can assign as well
#     return a, b, c, d


# print(a(c='cc', b='bb'))

# # Show decorator executes queue

# Since decorator executes in this first queue, then it is better to return function instead of executes it
# And most of all decorator use as adopter, which means return changed original function
# def executor_decorator(org_func):
#     org_func()

# # You don't even need to execute this function, it executes because you pass decorator on it, which executes it, since execute once after declaring original function
# # In this way it executes in the first queue, since while everything is declaring, decorator executes
# @executor_decorator
# def main_func():
#     print(123)

# # Do not use it, but know that this approach exist
# class my_dd(object):
#     def __init__(self, original_function):
#         self.org_func = original_function

#     def __call__(self, *args, **kwargs):
#         return self.org_func(*args, **kwargs)


# @my_dd
# def twice_print(m):
#     print(m)
#     return m


# print(twice_print('qm'))


# from functools import wraps # decorator, which change function options (function variables) to the one which passed in as arg
# import logging  # package for logging in file
# import time


# def my_time(org_f):
#     file_path = __file__.split('/')  # __file__ is a path to a running file
#     del file_path[len(file_path)-1]
#     logging.basicConfig(filename=f"{'/'.join(file_path)}/{org_f.__name__}.log", level=logging.INFO)

#     @wraps(org_f)
#     def decorator_call(*args, **kwargs):
#         start = time.time()
#         result = org_f(*args, **kwargs)
#         finish = time.time() - start
#         logging.info(f'Running {org_f.__name__} takes {finish} sec')
#         return result
#     return decorator_call


# def my_log(org_f):
#     file_path = __file__.split('/')
#     del file_path[len(file_path)-1]
#     logging.basicConfig(filename=f"{'/'.join(file_path)}/{org_f.__name__}.log", level=logging.INFO)

#     @wraps(org_f)
#     def decorator_call(*args, **kwargs):
#         logging.info(f'Run {org_f.__name__} with {args} {kwargs}')
#         return org_f(*args, **kwargs)
#     return decorator_call


# # Decorator can execute twice, first time in the first queue (once after declare func on which decorator passed) and the second one, when original function execute itself
# # Here is can be one more execution before first (or more then one), when decorator execute itself, in this case firstly it executes all decorators func and then decorator wrapper
# # ====================================
# # What if decorator execution returns new func, which accept an arg which may change upon the previous args, and it's may be recursive, while 'end' args given
# # @my_d('1')('0')('0')('1')('0')('end')
# # ====================================
# @my_time
# @my_log
# def my_func(sleep):
#     print('Hi')
#     time.sleep(sleep)
#     return f'Sorry, I was sleeping for a {sleep} sec)))'


# print(my_func(2))

# # Summarize
# @decorator
# def function():
#     pass

# # equivalent to this
# function = decorator(function)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Duck typing ))
# If something bahave like a duck, then this is a duck, since it solve all what we need from duck
# If something doing what we need, even if it not exact what we need, but solve all our issue from those what we really need, then it what we need

# Just use Pythonic approach for writing code, for this pourpose use try-catch statement

# arr = [1, 2, 3, 4, 5]
# val = 11

# Non-Pythonic
# if val in arr:
#     print(arr.index(val))
# else:
#     print(f'In {arr} does not exist {val} value')  # with string template everything connvert to str automatically
#     # print('In ' + str(arr) + ' does not exist ' + val + ' value')

# Pythonic
# try:
#     print(arr.index(val))
# except ValueError as e:
#     print(f'In {arr} does not exist {val} value')
#     print(e)  # for not exit from application

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( OOP ))


# define a constructor of a class in Python is an __init__ method instead constructor() as in js (or maybe in Python constructor of a class call as init, because constructor is an appropriate calling for js)


# class People():
#     # like static in js, but can call from instance, not only from class
#     count_of_hand = 2  # something that general, that not default value, since it is general for all instance

#     def __init__(self, name):
#         self.name = name
#         self.alive = True  # default value

#     def die(self, lastwords):  # so we need 'self' to know to what instance we call this method, for get right properties and mutate with instance, if your method do not use properties you still have to pass it, since Python passing it automatically
#         self.alive = False
#         del self.name  # can do it since python not strick typing lang
#         print(lastwords)
#         print('dead')

#     def change_people(self):
#         # self.count_of_hand += 1 # if we do it, its just create new instance prop, upon general, and did not change general
#         People.count_of_hand += 1

# p1 = People(name='Ben')
# # did not see count_of_hand since it is a reference to class as well as methods
# print(p1.__dict__)  # make dictionary from property in this instance (in instance constructor)
# p1.age = 32  # Since Python is not strick typing lang, it allow to has not strick schema of object (instance)
# print(p1.__dict__)  # make dictionary only from properties, methods and general property will be ignore

# print(p1)
# print(p1.age)  # add it to this instance outside of the class
# print(p1.name)
# print(p1.alive)
# print(p1.count_of_hand)  # general property

# # the same if type:
# # People.die(p1)  # since when we create instance and call in it method it pass instance, in the calling method param, at the first place
# p1.die('Buy bitcoin',)  # still pass instance in the first param of calling method
# print(p1.__dict__)
# print(p1.alive)
# print(p1.age)
# # print(p1.name)  # arise an error, since dead people do not have name
# # print(p1.some)  # arise an error, since do not have this method

# p2 = People('Shone')
# print(p2.__dict__)
# print(p2.alive)
# print(p2.count_of_hand)  # 2
# p2.change_people()  # 'Shone' change general prop for all People instance
# print(p2.count_of_hand)  # 3
# print(p1.count_of_hand)  # 3

# # If we do it, its just create new property in instance upon general, but did not change general
# # So with p1 or p2 (instance or self) we make instance (local) prop, if want work with general have to use People (class)
# # Via p1 or p2 (instance) we can have access to general prop (read it) but manipulate with them have to through People (class)
# p2.count_of_hand = p2.count_of_hand + 2
# p2.count_of_hand += 2
# print(p2.count_of_hand)  # 7
# print(p1.count_of_hand)  # 3

# # When we use static in JS, we make those method or property available only from class, not from instance (but in Python you can get it from instance, but not change, only if in the method and through class, but this params still general for everyone)

# # Or we can have access to static method through __proto__ and constructor, since static method in constructor of class, and this constructor with all variable of prototype in __proto__ of instance
# # ==================================
# # function static_method(...args) {
# #     console.log('bbbb')
# # }
# # instance.__proto__.constructor.static_method = static_method
# # ==================================

# # Because instance in JS have access only to 'this' and prototype, but static method in constructor, so we do not overwrite prototype of class in this way, but we still have a link to static method through constructor, so performance of not overwriting prototype we do not get, since we overwriting constructor, and as I thought we have link only to prototype, and static method not in it, and so we do not overwrite object, to which all reference, but instance link to prototype and constructor, where static method, as well, so instead of overwriting prototype, we write constructor, it is not a performance, it is just a case
# # Static method allow us to store it only in one place, that's make it general for all instance created from this class
# # So what is this 'one' place? This is a constructor in the prototype, so in the instance of class we will have '__proto__'
# # Which will send to prototype of this class, and this prototype has constructor of this class and method for itself
# # And in this constructor we will have a static method and property
# # Also in the __proto__ also exist constructor besides methods, which is of the class, and inside it live static property
# # So that why we can say class.property and get answer, because we use object which returns class constructor, do not consuse it with constructor of the instance
# # Shortly constructor of the class is a static method and properties, and constructor of the instance is an invoked defined constructor of the class with your arguments, and those constructor which you define in class definition is all about how to create constructor of instance
# # And in the constructor exist all your ready to use property, to which you can have access, by - 'instance.property', and the same works for class - 'class.property'
# # Example:
# # class A{
# #     constructor (a) {
# #         this.a = a;
# #     }
# # }
# # const a = new A('b');
# # # Since in a exist constructor with 'a' key-value where value is 'b'
# # console.log(a.a); # 'b'
# # And so it works for class constructor
# # But for class constructor you do not need to specify how to create this constructor, it creates when you create a class, and you can only add to them some new properties, by static keyword

# # So the static method or property do not add any performance, it just create method and property in the way, that JS may not worry about with which properties (this) it has to execute a function (maybe brings some performance)
# # And if property make static, then property becomes general for all instance, but you can not take it from instance, but it related to them

# # When we create ordinary method, it pass in the prototype of class and then, when create instance of this class, it creates link to this prototype calling it __proto__
# # So we can create this method only one and use it when we need, but pass right property with which this method has to work (this), it handels in the js arch layer, when we call method from exact instance, it somehow takes its property and work with them inside method

# # In the Python, object works as in js, but instead of store static in constructor and another in prototype, Python store it in one place, in class definition
# print(People.__dict__)  # Show all method and property, to which instance reference
# print(dir(People))  # Show all method and property, to which instance reference and all manipulation with classes itself


# class Company:
#     level = 1  # general parameter

#     def __init__(self, name, special):
#         self.name = name
#         self.special = special

#     def is_tech_company(self):  # ordinary method
#         if self.special == 'phone' or self.special == 'tech':
#             return True
#         return False

#     @classmethod
#     def defineSpecialByName(cls, name):  # classmethod, it is like ordinary method, but instead of accept first argument as instance, it gets class, which allow you to create instance, or call eather staticmethod or classmethod
#         if name == 'Apple':
#             special = 'phone'  # scope allow you create variable in statement and use it in global scope
#         return cls(name, special)

#     @classmethod
#     def levelUp(cls):  # also you can call it from instance
#         cls.level -= -1

#     @staticmethod
#     def about_best_companies():  # staticmethod, it is a method which do not accepts class or instance, it is like a separate function, but it bind to class, because his logic appropriate to class logic
#         print('Tech companies are the best')

#     @staticmethod
#     def just_level_up():  # also you can call it from instance
#         Company.level += 1

# =====================================
# Actually in Python OOP all methods in class are "static" or "classes", since it can be call from class directly, but it force us to pass instance, class or nothing in param in this case, and decorators for class or static method handle a rise error, since Python want to have an instance in first param place
# In this way also work inheritance, when you write class.__init__(self, *args), inside __init__ you change self obj, and so you get changed self by another class
# But when in inheritance people write super().__init__(*args), I think we just create an instance, like class() (super()), and call from it method __init__, but ....
# =====================================

# c1 = Company('Microsoft', 'tech')
# print(c1.is_tech_company())
# print(c1.level)
# c2 = Company.defineSpecialByName('Apple')
# print(c2.is_tech_company())
# c1.levelUp()
# Company.levelUp()
# print(Company.level)
# print(c1.level)
# print(c2.level)
# Company.about_best_companies()
# Company.just_level_up()
# print(Company.level)
# print(c1.level)
# print(c2.level)


# class Employee:
#     def __init__(self, f_name, l_name, pay):
#         self.first_name = f_name
#         self.last_name = l_name
#         self.salary = pay
#         self.email = f'{self.first_name}.{self.last_name}@example.com'

#     def fire_yourself(self):
#         self.salary = 0
#         del self.email

#     def you_hire(self, pay):
#         self.salary = pay
#         self.email = f'{self.first_name}.{self.last_name}@example.com'

# class AnotherEmployee(Employee):  # does nothing, just repeat log of Employee with new name
#     pass

# class Manager(Employee):
#     def __init__(self, name, sername, pay, level):
#         # it is okay, I understood it, it call __init__ like an ordinary method
#         Employee.__init__(self, name, sername, pay)
#         # # So I understood, after call super it returns extended class, and something also, and this somthing pass right self in the calling of __init__ method
#         # super().__init__(name, sername, pay)
#         self.level = level

#     def fire_someone(self, someone):
#         try:
#             self.level
#         except AttributeError:
#             print('You are not in possibility to fire now')
#         else:
#             if self.level <= 3:
#                 someone.salary = 0
#                 del someone.email
#             else:
#                 print('You are not in possibility to fire now')

#     def fire_yourself(self):
#         Employee.fire_yourself(self)
#         del self.level

#     # 1 lvl is the best
#     def lvl_up(self):
#         self.level += 1

#     def lvl_down(self):
#         if self.level != 1:
#             self.level -= 1

# # # Shows what class accept, what method has, shows generals prop, and dunder method
# # print(help(AnotherEmployee('Pit', 'Jorge', 500000)))

# # the same as Employee, but have a possib to fire another guys
# m1 = Manager('Karl', 'Galaham', '10000000000000 per sec', 3)
# # m1.fire_yourself()
# e1 = Employee('Anastasy', 'Sobl', '999999999999 per sec')
# e2 = Employee('Lyci', 'Merk', 5)
# m1.fire_someone(e2)
# m1.lvl_down()
# e3 = Employee('Bob', 'Reny', 9999999999999999999999999)
# m1.fire_someone(e3)
# e4 = Employee('Shone', 'Lazy', 1)
# m1.lvl_up()
# m1.lvl_up()
# m1.fire_someone(e3)
# print(e1.__dict__)
# m1.fire_someone(e1)
# m1.fire_yourself()
# print(e1.__dict__)
# print(m1.__dict__)  # even None field


# class A:
#     def __init__(self, a):
#         self.a = a

#     def shout(self):
#         shout = ''
#         for _ in range(10):
#             shout += self.a
#         print(shout)

# class B:
#     def __init__(self, b):
#         self.b = b

#     def bark(self):
#         shout = []
#         for _ in range(10):
#             shout.append(self.b)
#         print('-'.join(shout))

# class C(A, B): # multipule inheritance
#     def __init__(self, a, b, c):
#         A.__init__(self, a)
#         B.__init__(self, b)
#         self.c = c

#     def silent(self):
#         print('Silent is ' + self.c)

# c = C('aaooo', 'bark', 'tsssss')
# c.shout()
# c.bark()
# c.silent()


# # check instance to class type
# print()  # empty line
# print('isinstance')
# print(isinstance(m1, Manager))  # True
# print(isinstance(m1, Employee))  # True, since extends from it
# print(isinstance(e1, Manager))  # False
# print(isinstance(e1, Employee))  # True

# # check is the class
# print()  # empty line
# print('issubclass')
# print(issubclass(Employee, Manager))  # False
# print(issubclass(Manager, Employee))  # True, since Employee is a subclass for Manager


# In the Python do not exist private method, it is work in it by dial between programers, if method have double _ in the begining of the name in method, then do not use this method in public way
# If method has double _ in the begining and in the end of name, the this method is dunder, it means, this method call by system, and help it in it some build-in function like: repr() -> __repr__, dir() -> __dir__, dict() -> __dict__, iter() -> __iter__, next() -> __next__, str() -> __str__, len() -> __len__, ...
# Dunder method can be also called by 'with' keyword (__exit__ and __enter__) or while creating constructor (__init__)
# When you write '+' under the hood it call __add__ dunder method, and it requires to have on the both side variable with the same type

# As an alternative in JS, we just create new method, which call when we want to get exact info of instance, for example, when we want an representation of class, we just can create and call method for representation, like toRepresent, or if we want to conwert it to string, we create and call method toString or toJSON, which created in class, in Python it make in more elegant way, but not necessary, you can still make it in a way as in JS, unlike it cool that +-*/= call this dunder method, and you can reassign it, but it still not necessary, since you can create a separate method for it, and I think, this is what you will do

# import json

# class Foo():
#     def __init__(self, one_p: int, two_p: int):
#         self.one = one_p
#         self.two = two_p

#     def __add__(self, other):
#         return Foo(self.one + other.one, self.two + other.two)

#     def __repr__(self) -> str:  # __repr__ method has always return a string
#         return json.dumps(self.__dict__)

#     def __len__(self) -> int:
#         return 2

#     __str__ = __repr__

# foo1 = Foo(2, 3)
# foo2 = Foo(4, 11)
# print(foo1)
# foo3 = foo1 + foo2
# print(len(foo3))
# print(str(foo3))
# print(foo1 + foo2)  # __add__ and __repr__

# So after this dunders, I got why we need to pass 'self', even in __init__ method, because it calls from exact instance, for set 'self' (instance), since before calling __init__ it already create instance and assing to variable


# import json

# class Innovator():

#     def __init__(self, name, last, invention):
#         self.name = name
#         self.last_name = last
#         self.invention = invention

#     @property  # one way of creating getter, but in this way you can not create setter, withit getter
#     def fullname(self):
#         # Fuck, man, it's so hard to understand in what cases we have to use dunder methods, and in what it build-in methods
#         # self.name, self.last_name = another_name.split(' ')
#         try:
#             return f'{self.prefix} {self.name} {self.last_name}'
#         except AttributeError:
#             return f'{self.name} {self.last_name}'

#     @fullname.setter  # in this way you can not create setter, withit getter, the same as deleter
#     def fullname(self, new_fullname):
#         self.name, self.last_name = new_fullname.split(' ')

#     @fullname.deleter  # for 'del' keyword
#     def fullname(self):
#         del self.name
#         del self.last_name

#     def __repr__(self):
#         res = {}
#         for key in list(self.__dict__.keys()).__add__(['fullname', 'created_shit']):
#             try:
#                 res[key] = getattr(self, key)
#             except AttributeError:
#                 continue
#         return json.dumps(res)

#     def _get_created_shit(self):
#         return f'{self.fullname} doscover {self.invention}'
#     # the second way of creating getter, in this way getter and setter and deleter is independent
#     created_shit = property(fget=_get_created_shit)

#     def _set_prefix_name(self, prefix: str):
#         if len(prefix) == 0:
#             del self.prefix
#         else:
#             self.prefix = prefix
#     prefix_name = property(fset=_set_prefix_name)

# elon = Innovator('Elon', 'Mask', 'Rocket')
# print(elon)
# elon.fullname = 'Stive Jobs'
# print(elon)
# elon.fullname = 'Elon Mask'
# elon.prefix_name = 'Mr.'
# print(elon)
# elon.prefix_name = ''
# print(elon)
# del elon.fullname
# print(elon)


# --------------------------------------------------------------------------------------------------------------------------------------------------------

# OOP Metaclasses


# @property
# def add_getter(self):
#     # very dangerouse operation, but I am sure that everything will be okay, since control the situation, in the prod do not do it
#     return self.xx + self.x

# def add_attr(self):
#     self.xx = 5

# # In Python exit several way to create a class: one with class keyword and the second one is though 'type' function
# # The 'type' function somehow can tell us a type of value, and create a class itself
# # So I think, 'type' function can define base object in app, and this is what class actually need and do by this 'type' function
# Test1 = type('Test1', (), {'x': 3, 'add_attr': add_attr, 'sum_it': add_getter})

# class Test2:
#     def __init__(self):
#         self.x = 3

# # Test1 and Test2 extremely equivalent as a class (but attr different), besides with class keyword IDE can show you hint
# t1 = Test1()
# t2 = Test2()
# print(t1.x)
# t1.add_attr()
# print(t1.xx)
# print(t1.sum_it)
# print(t2.x)

# # Since geting type of Test2, which was created via class keyword, return <class 'type'>, then I believe under the hood class uses 'type' function
# print(type(Test1()))
# print(type(type(Test1())))  # also the same as 'type(Test1)' it can be because every 'type(base_obj)' return <class 'type'>
# print(type(Test1))
# print(type(Test2))


# class MetaClass(type):  # extend  redefine __new__ method, to get 'self', instead of 'cls', it is a good practice (maybe)
#     # In Meta is a bad practice change method or attr name, since hints will lie you
#     # Meta in Python work in the way, where you can define extra attr or extend from some another class, here is not some hided fields, to which you can get access through some module, like in JS is a reflect-metadata, in Python it is in class itself
#     def __new__(self, class_name, extended, attributes):  # __new__ method call before __init__, but as you see, after create an instace
#         print(self)  # self here is a MetaClass
#         attributes['__analyse__'] = True
#         return type(class_name, extended, attributes)

# class Some(metaclass=MetaClass):
#     def __init__(self, one, two):
#         self.first = one
#         self.second = two

#     def print_attr(self):
#         res = [res_key for res_key in filter(lambda x: not x.startswith(
#             '__') and not x.endswith('__'), self.__dict__.keys())]
#         print(res)

# s = Some(11, 22)
# s2 = type('Some2', (), {'a': 5, 'b': 6})()  # Class for compare
# s.print_attr()
# print(s.__dict__)

# def anls(o):
#     try:
#         if o.__analyse__ == True:
#             print(sum(o.__dict__.values()))
#     except AttributeError:  # just ignore if do not exist field '__analyse__'
#         pass

# anls(s)
# anls(s2)

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# (( Mistakes ))

# just describe a mistake, which you may do:

# 1. Call module name as existing one
# 2. Call variable name as existing one, which reassign functionality existing, since in Python do not exist constant variable
# 3. Do not pass in function default arguments, which is immutable, for example:

# # In the past it declare default value only once, and then set to variable link of created value, and use it as default link in memory to value, so that's why when we execute function twice with default value it works with the not defined value
# # But now it defines and not change, since it concatenates, that means not mutate entering list, I think it works so for immutable in Python
# def add_U(user, list_U=['Someone first']):
#     # do not mutate list
#     if isinstance(user, list):
#         return list_U + user
#     return list_U + [user]

#     # # mutate list
#     # if isinstance(user, list):
#     #     for u in user:
#     #         list_U.append(u)
#     # else:
#     #     list_U.append(user)
#     # return list_U

# users = ['Elon Mask', 'Bogdan Paranitsa', 'Bart Wood']
# print(add_U('Andrii Statsenko', users))
# print(add_U('Bill Gates'))
# print(add_U(['Every Masons', 'Illuminates']))


# # One more example with default args:
# var = 1

# def get_variable():
#     return var

# def increment_var(var=get_variable()):  # as you already know, 'var' defines only once, what means 'get_variable()' executes only once
#     var += 1
#     return var

# print(increment_var())  # var is 2
# var = 100
# print(increment_var())  # var is 2 again, but expect 101
# print(get_variable())  # 100
# print(increment_var())

# To fix that all, you just need to define variable in every execution of function, for this just define default args as None (as not required, and then in execution defines for them value)

# 4. zip, map, filter,reduce and so on returns a generator, that means if we iterator through them, it will not iterate again, his end value was achieved, so it is the end, now it will return void
# If you need a result of some of this function, just make it result = list(generator)

# 5. Using * in import, it is mistake because it may be hard to debag, since something can be overwrite

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Coursehunters python algorithms №1
# class Unique():
