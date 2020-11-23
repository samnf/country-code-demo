#!/usr/bin/python

import sys, getopt

def main(argv):
  country_codes = []
  source = 'api'
  listen = 0
  
  try: 
    opts, args = getopt.getopt(argv, '', ['help','countryCode=','source=','listen='])

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
      country_codes.append(str(arg))
    elif opt == '--source': 
      source = arg 
    elif opt == '--listen': 
      listen = arg 
  
  if not country_codes: 
    print("--countryCode option not found. ")
    help()


def help():
  print("""Options: 

--help              Display help
--countryCode=XX    Required. Country code to look up (can be set multiple times)
--source=api,file   Set data source to api or local json file. Default=api
--listen=NNNN       Enables listen api mode on specified port. 0 or not set = off
""")

if __name__ == "__main__":
   main(sys.argv[1:])