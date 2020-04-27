# n = int(input())
# d = dict()
# for i in range(1, n+1):
#     d[i]=i*i
# print(d)


person = {
    'name': 'ductn',
    'age' : '20',
    'option': {
        'alo': 'lo cc'
    },
    'sex' : '404',
    'status': 'single'
}
#person['status'] = 'married'

del person['name']
print(person['option']['alo'])
