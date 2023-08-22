import requests

APIK = 'PMAK-64e4bb196f77cc00317e8823-7034fe5c6bd767f31d50a34a8ffaef9478'
CID = '29277476-31f418e2-b5ad-4cba-8b58-25c09020bab0'

REQUESTS_URL = 'https://api.getpostman.com/collections/{CID}/requests'


data = {
    "headers": "",
    "method": "GET",
    "data": [],
    "dataMode": "raw",
    "rawModeData": "",
    "url": "https://api.example.com/your_endpoint",
    "description": "",
    "collectionId": CID
}

