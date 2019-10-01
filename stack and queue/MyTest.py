# def triangles():
#     N = [1]
#     while True:
#         yield N
#         N.append(0)
#         N = [N[i] + N[i - 1] for i in range(len(N))]
#
#
# if __name__ == "__main__":
#     n = 0
#     for t in triangles():
#         print(t)
#         n = n + 1
#         if n == 10:
#             break
#
#
# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2
#
# my_gen = all_even()
#
# # Generate the first 5 even numbers.
# for i in range(5):
#     print(next(my_gen))
#
# # Now go and do some other processing.
# do_something = 4
# do_something += 3
# print(do_something)
#
# # Now go back to generating more even numbers.
# for i in range(100):
#     print(next(my_gen))

# list = []
# def toUppers(L):
#     for item in L:
#         if isinstance(item, str):
#             list.append(item.upper())
#     return list
#
#
# print(toUppers(["Hello", "world", 101]))


# list1 = []
# list2 = []
# for num in range(100, 1000):
#     if(num % 10) ==(int(num/100)):
#         list1.append(num)
# list2 = ([n1 * 100 + n2 * 10 + n3 for n1 in range(1, 10) for n2 in range(10) for n3 in range(10) if n1 == n3])
#
# print(list1 == list2)
