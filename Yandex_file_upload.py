import requests


HOST = 'https://cloud-api.yandex.net:443'

class YandexUploader:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': self.token}

    def upload_file(self, file_name):
        url = HOST+'/v1/disk/resources/upload'
        params = {'path': file_name, 'overwrite': 'true'}
        response = requests.get(url, params=params, headers=self.headers)
        response = requests.put(response.json()['href'])
        if response.status_code == 201:
            return 'Файл успешно загружен на диск'


if __name__ == '__main__':
    token = ''
    uploader = YandexUploader(token)
    print(uploader.upload_file('list_of_smth.txt'))
    print(uploader.upload_file('test.txt'))