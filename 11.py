
"1 usul"
# a={1,2,3,4,5,6,7,8,9,10}
# my_list = list(a)
# a_iter=iter(a)
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))


# import time
# k= list(range(1,10000))
# a_time=time.time()
# a_iter=iter(k)
# while True:
#     try:
#         next(a_iter)
#     except StopIteration:
#         break
# b_time=time.time()
# n=b_time-a_time
# print(n)




"2 usul"
# def try_generatot(a):
#     n=a
#     n+=0
#     yield n*1
#     n+=1
#     yield n*2
#     n += 1
#     yield n*9
# result=try_generatot(1)
# print(next(result))
# print(next(result))
# print(next(result))



# def generator(y):
#     n=y
#     n*=3
#     yield n
#
#     n+=12
#     yield n
#
#     n-=9
#     yield n
# result=generator(27)
# print(result)



"3 usul"
# class Counter:
#     def __init__(self,start,stop):
#         self.start=start-1
#         self.stop=stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start-=1
#
#         if self.start>self.stop:
#             return self.start
#         raise StopIteration
#
# for item in Counter(10,-10):
#     print(item)


#
# class Counter:
#     def __init__(self, start, stop):
#
#         self.current = start  # Start counting from this value.
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.stop:
#             value = self.current
#             self.current -= 1
#         raise StopIteration
#
#
# for item in Counter(200, -100):
#     print(item)



"4 usul"
generator=(i for i in range(1,51) if i %4==0)
for i in generator:
    print(i)



generator= (i for i in range(101,205) if i%5==0)
for i in generator:
    print(i)