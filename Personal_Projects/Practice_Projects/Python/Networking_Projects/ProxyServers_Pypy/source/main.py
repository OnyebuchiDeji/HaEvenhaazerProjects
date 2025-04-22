"""
    Using the requests module, one can get the HTML file of that page.
    below `response.text` shows the HTML code

    Now, the website can extract information of you from your request.
    Here, a request is sent to a certain website that returns your IP information,
    including longitudinal and latitudinal location, called `https://ipinfo.io`.
    Every site can get this information, but this special site returns this data
    to you, the one who made the request.

    This way, all of one's info is exposed.
    This is where proxy servers are used.

    By using a proxy server, the request to that site is made indirectly through another device
    in the internet.
    You make the request but through that device, therefore the information available to the
    site you make the request to is not yours but that anonymous device's.

    There are such servers that one can use as proxies for just redirecting your request. 

    See the info returned from running
        ```response = requests.get("https://ipinfo.io/json")
            print(response.text)
        ```
            :
        {
            "ip": "160.5.250.81",
            "city": "Keele",
            "region": "England",
            "country": "GB",
            "loc": "53.0038,-2.2874",
            "org": "AS786 Jisc Services Limited",    
            "postal": "ST5",
            "timezone": "Europe/London",
            "readme": "https://ipinfo.io/missingauth"
        }

    Concerning proxy servers, you can Google 'Proxy Sever List'
    It will give a bunch of proxy servers you can use.

    Not just anonymity is targetted, but also to pretend thaat you're from 
    a different country.
"""

import requests


def eg1():
    response = requests.get("https://learncpp.com")
    print(response.text)

def eg2():
    #   Using the site's json API
    #   It gives much ingo
    response = requests.get("https://ipinfo.io/json")
    print(response.text)

def eg3():
    response = requests.get("https://ipinfo.io/json")
    print(f" City: {response.json()['city']}")
    print(f"Region: {response.json()['region']}")
    print(f"Country: {response.json()['country']}")
    print(f"Location: {response.json()['loc']}")



def main():
    #   Not all proxies work. Google a proxy list and get them
    # 'https': "https://52.183.8.192:3128",     # USA   <- didn't work
    # 'https': "https://140.277.69.170:6000",   # JAP  <-- also didn't work
    # 'https': "https://67.43.227.227:12633",     # CANADA <- didn't work
    proxies = {
        # 'https': "https://114.156.77.107:8080", # JAP
        # 'https': "https://157.100.7.218:999"        #   ECUADOR
        'https': "https://67.43.236.20:13735",       #   CANADA
    }
    response = requests.get("https://ipinfo.io/json", proxies=proxies)
    print(response.text)




if __name__ == "__main__":
    main()