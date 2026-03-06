from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("mongodb+srv://youtubepy:mutaib@cluster0.vxf3gop.mongodb.net/")
db = client["ytmanager"]
videos_collection = db["videos"]

#print(videos_collection)

def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})
def list_videos():
    for video in videos_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
def update_video(video_id, new_name, new_time):
    videos_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})
def delete_video(video_id):
    videos_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\nYouTube Video Manager")
        print("1. list all Videos")
        print("2. add a new Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video ID to update: ")
            new_name = input("Enter new video name: ")
            new_time = input("Enter new video time: ")
            update_video(video_id, new_name, new_time)
        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()