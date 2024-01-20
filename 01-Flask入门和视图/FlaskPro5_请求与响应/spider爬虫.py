import requests


# post 请求
# res = requests.post('http://127.0.0.1:5001/request/',
#                     data={'name': 'lucy', 'age': 33}
#                     )
# print(res.text)


# get 请求
res = requests.get('http://127.0.0.1:5001/request/?name=lisi&age=33',
                   cookies={'name':'hello'})
print(res.text)