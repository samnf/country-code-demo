import requests, json
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def get_default():
  return {}

# Returns an OK status
@app.get('/health')
async def get_health():
  return {'code': 200, 'status': 'OK'}

# Calls the travel advisory API, returns the status received 
@app.get('/diag')
async def get_diag():
  url = 'https://www.travel-advisory.info/api'
  r = requests.get(url).json()['api_status']['reply']
  return {'api_status': r['status'], 'api_code': r['code'], 'api_note': r['note']}

# Lookup of country code, returns country name
@app.get('/lookup')
async def lookup_code(countryCode: str):
  countryCode = countryCode.upper()
  try: 
    countryName = find_country_api([countryCode])[countryCode]['name']
  except: 
    return {'error': 'Country code not found'}
  return {'code': countryCode, 'name': countryName}

# Searches for a country name (case insensitive) and returns a code if found
@app.get('/convert')
async def convert_name(countryName: str):
  
  countryData = find_country_api('')
  for country in countryData: 
    # make lowercase for case-insensitive comparison
    if countryData[country]['name'].lower() == countryName.lower(): 
      return {'code': country, 'name': countryData[country]['name']}
    
  return {'error': 'Country name not found'}
  
def find_country_api(code):
  params = ''
  if code: 
    params = { 'countrycode': code }
    
  url = 'https://www.travel-advisory.info/api'
  r = requests.get(url, params=params)
  return r.json()['data']
