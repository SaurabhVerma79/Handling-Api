import requests
def stockapi_freeapi():
    url="https://api.freeapi.app/api/v1/public/dogs?page=1&limit=10&query=Affenpinscher"
    response=requests.get(url)
    data=response.json()

    if data["success"] and "data" in  data:
        user_data=data["data"]
        limit=user_data["limit"]
        page=user_data["page"]
        totalItems=user_data["totalItems"]
        
        return limit,page,totalItems
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        limit,page,totalItems=stockapi_freeapi()
        print(f"limit:{limit},\nnextPage:{page},\ntotalItems:{totalItems}")
    except Exception as e:
        print(str(e))
if __name__=="__main__":
    main()