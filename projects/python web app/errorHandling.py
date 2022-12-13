# using the requests library to access internet data
  
  import requests
  from requests import HTTPError Timeout
  
  def main():
  #use requests to issue a standard HTTP GET request
  
  try:
  #url = "http://httpbin.org/status/404"
  url = "http://httpbin.org/delay/5"
  result = requests.get(url, timeout=2)
  result.raise_for_status()
  printResults(result)
  except HTTPError as err:
  print("Error: {0}".format(err))
  except Timeout as err:
  print("Request timed out: {0}".format(err))

  #another error handling example
  try:
    f = open('testfile.txt')
  except FileNotFoundError as e:
    print(e)
  except Exception as e:
    print(e)
  else: # runs if no exception is raised in the try block
    print(f.read())
    f.close()
  finally: # runs regardless of whether an excetion was raised or not
    print("Executing Finally...")