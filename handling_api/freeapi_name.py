
import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    data = response.json()
    
        
    user_data = data["data"]
    
    if user_data:
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
      
        
    else:
        raise Exception("Failed to fetch random user data")

def main():
    print("Fetching random user data from FreeAPI...")

    try:
        username, country = fectch_random_user_freeapi()
        print(f"Username: {username}")
        print(f"Country: {country}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()