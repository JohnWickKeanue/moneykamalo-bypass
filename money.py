
import time
import requests
from bs4 import BeautifulSoup 
print("Everything Looks Good! Lets Continue.")

url = "https://earn.moneykamalo.com/Delivery_Chinko"  #@param {type:"string"}


# leech with credits broo
# ---------------------------------------------------------------------------------------------------------------------

def money(url):
    
    client = requests.session()
    
    
    DOMAIN = "https://go.moneykamalo.com"

    url = url[:-1] if url[-1] == '/' else url

    code = url.split("/")[-1]
    
    final_url = f"{DOMAIN}/{code}"
    
    ref = "https://gorating.in/"
    
    h = {"referer": ref}
  
    resp = client.get(final_url,headers=h)
    
    soup = BeautifulSoup(resp.content, "html.parser")
    
    inputs = soup.find_all("input")
   
    data = { input.get('name'): input.get('value') for input in inputs }

    h = { "x-requested-with": "XMLHttpRequest" }
    
    time.sleep(5)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("
    
# ---------------------------------------------------------------------------------------------------------------------
print(money(url))
