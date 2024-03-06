import requests
def stockapi_freeapi():
    url="https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response=requests.get(url)
    data=response.json()

    if data["success"] and "data" in  data:
        user_data=data["data"]
        Name=user_data["Name"]
        ListingDate=user_data["ListingDate"]
        return Name,ListingDate
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        Name,ListingDate=stockapi_freeapi()
        print(f"Name:{Name},\nListingDate:{ListingDate}")
    except Exception as e:
        print(str(e))
if __name__=="__main__":
    main()