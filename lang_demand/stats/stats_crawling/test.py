# listt = {1: [2, 3],
#         4: [5, 6]}
#
# for i in listt.items():
#     i = list(i)
#     # listt[i[0]].append(100)
#     listt[i[0]][1]=300
# print(listt)
# #
# a = 'ab  c de'
# a= a.replace(' ', '')
# print(a)


a = '123,333.90'
dot = a.index('.')
a = a[:dot]
print(a)
