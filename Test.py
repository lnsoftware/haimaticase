
# dicttest = []
# d = dicttest
# d.append('a')
# d.append('b')
# d.append('c')
# d.insert(2,'d')
# d.append('c')
# d.append('b')
# print(d)
# a = d.pop()# 默认删除最后一个元素，加索引能删除指定位置的元素，如pop(0)代表删除第一个元素，并能保留它的值
# print(d)
# print(a)
# del d[0]
# print(d)
# 根据值删除元素

# e = []
# for i in d:
#     if not i in e:
#         e.append(i)
# print(e)

# print(list(range(0,100,2)))
testlist = []

# for k,v in test_a.items():
#     print(k,v)
# for name in test_a.keys():
#     print(name)
# for value in test_a.values():
#     print(value)
for test_num in range(0,10):
    test_a = {
        'a': 'lemon',
        'b': 'testone',
        'c': 'testtwo'
    }
    testlist.append(test_a)

# for test in testlist[:5]:
#     print(test)
for test in testlist[3:5]:
    if test['b'] == 'testone':
        test['b'] = 'test1'
        test['a'] = 'orange'
        test['c'] = 'test2'
for test in testlist[0:5]:
    print(test)


