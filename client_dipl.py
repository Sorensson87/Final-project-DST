import requests

if __name__ == '__main__':

    r = requests.post('http://localhost:5000/predict', json=['active', 3, 1, 'miami', 2540, 'FL', 3, 0, 'townhouse', 4.5, 1.5, 1999, 0, 'gas', 1, '2 spaces', 15489, 255])
    print(r.json()['prediction'])