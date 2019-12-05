student = {
    'name': 'Hello',
    'id': 234,
    'class': 12
}

student['last_name'] = 'Kowalski'

try:
    last_name = student['last_name']
    numbered_last_name = 3 + last_name
except KeyError:
    print('error finding last_name')
except TypeError as error:
    print('error from type error')
    print(error)
except Exception:
    print('Unknown error')

print('The code executes!')
