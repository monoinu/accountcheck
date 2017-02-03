pythonでリクエストを取得
>>> r = requests.get('https://twitter.com/donabeno')
>>> r.status_code
200
>>> r = requests.get('https://twitter.com/fasdfadsgergfasfdsage')
>>> r.status_code
404
>>> r.status_code == requests.codes.ok
False
>>> r = requests.get('https://twitter.com/donabeno')
>>> r.status_code == requests.codes.ok
True
>>> r.status_code
200
>>>
>>>
>>>
>>> r = requests.get('https://github.com/monoinu')
>>> r.status_code
200
>>> r.status_code == requests.codes.ok
True
>>> r = requests.get('https://github.com/monoinugfsdgdfgsgfgfdsggf')
>>> r.status_code
404
>>> r.status_code == requests.codes.ok
False
>>>
>>>
>>> quit()
[root@localhost tmp]#
[root@localhost tmp]#
[root@localhost tmp]#



>>> url = twitter + account
>>> print url
https://twitter.com/fdjksajfkajfkjfadjk
>>>
>>> r = requests.get(url)
>>> r.status_code
404
>>> account = "monoinu"
>>> r = requests.get(url)
>>> r.status_code
404
>>> r = requests.get(twitter + account)
>>> r.status_code
200
>>>
>>>
>>>
>>>
