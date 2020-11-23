import requests, json
from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
async def get_health():
  return {'code': 200, 'status': 'OK'}

@app.get('/diag')
async def get_diag():
  url = 'https://www.travel-advisory.info/api'
  r = requests.get(url).json()['api_status']['reply']
  return {'api_status': r['status'], 'api_code': r['code'], 'api_note': r['note']}

@app.get('/lookup')
async def lookup_code(countryCode: str):
  countryName = find_country_api([countryCode])[countryCode]['name']
  return {'code': countryCode, 'name': countryName}

@app.get('/convert')
async def convert_name(countryName: str):
  
  countryData = find_country_api('')
  for country in countryData: 
    # make lowercase for case-insensitive comparison
    if countryData[country]['name'].lower() == countryName.lower(): 
      return {'code': country, 'name': countryData[country]['name']}
    
  return {'error': 'Country not found'}
  
def find_country_api(code):
  params = ''
  if code: 
    params = { 'countrycode': code }
    
  url = 'https://www.travel-advisory.info/api'
  r = requests.get(url, params=params)
  return r.json()['data']
