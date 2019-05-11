import requests

def get_habrhabr():
    r = requests.get('http://habrhabr.ru/')
    print(r.status_code)
    print(r.headers)
    print(r.content)

def find_pet_by_tag(tag):
    params = {'tags': tag}
    headers = {
    'Accept': 'application/xml'
    #'Accapt': 'application/json'
    }
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    r = requests.get(url, params = params, headers = headers)
    print(r.status_code, r.headers)
    print(r.content)

if __name__ == '__main__':
    #get_habrhabr()
    find_pet_by_tag('string')
