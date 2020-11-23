#!/usr/bin/python

import sys, getopt, requests, re, json

def main(argv):
  country_codes = []
  
  # set default values
  source = 'api'
  listen = 0
  
  try: 
    opts, args = getopt.getopt(argv, '', ['help','countryCode=','source=','listen='])
    print('\nCountry Code Lookup, Author: Sam Fulton\n')

  except getopt.GetoptError:
    print("Invalid options found")
    help()
    sys.exit(2)
  
  # Override all commands if '--help' option set
  if '--help' in argv: 
    help()
    sys.exit(0)

  for opt, arg in opts: 
    if opt == '--countryCode': 
      # Regex to validate country code
      if not bool(re.match('^[A-Za-z]{2}$', arg)):
        print(f'{opt}={arg} needs to be a 2 letter country code.')
        help()
        sys.exit(2)
      country_codes.append(str(arg))
      
    elif opt == '--source': 
      source = arg 

    elif opt == '--listen': 
      try: 
        listen = int(arg)
      except: 
        print(f'--listen={arg} must be an integer')
        help()
        sys.exit(2)
    
  if not country_codes and listen == 0: 
    print("--countryCode option not found, listen mode not enabled ")
    help()
    sys.exit(2)

  if source == 'api': 
    find_country_api(country_codes)
  elif source == 'file': 
    find_country_file(country_codes)
  else: 
    print(f'Invalid source option "{source}"')
    help()
    sys.exit(2)


def find_country_api(codes):
  for code in codes: 
    params = { 'countrycode': code }
    url = 'https://www.travel-advisory.info/api'
    r = requests.get(url, params=params)
    country_name = r.json()['data'][code]['name']
    print(f'{code} = {country_name}')
  
def find_country_file(codes):
  with open('data.json') as f: 
    country_data = json.load(f)['data']
  # for code in codes: 
  for code in codes: 
    name = country_data[code]['name']
    print(f'{code} = {name}')

def help():
  print("""
  Options: 

--help              Display help
--countryCode=XX    Required if not in listen mode. Country code to look up (can be set multiple times)
--source=api,file   Set data source to api or local json file. Default=api
--listen=NNNN       Enables listen api mode on specified port. 0 or not set = off
""")

if __name__ == "__main__":
   main(sys.argv[1:])