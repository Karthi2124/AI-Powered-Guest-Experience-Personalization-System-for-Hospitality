import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["hotel_dashboard"]  
# File paths
downloads_path = "/home/hp/Documents/Assignment_4/" 

# Function to upload CSV data to MongoDB
def upload_csv_to_mongo(csv_file, collection_name):
    df = pd.read_excel(downloads_path + csv_file, engine="openpyxl")  
    data = df.to_dict(orient="records")
    db[collection_name].insert_many(data)
    print(f"Uploaded {len(data)} records to {collection_name}")

# Uploading Data
upload_csv_to_mongo("bookings.xlsx", "booking_data")
upload_csv_to_mongo("dining_info.xlsx", "dining_info")
upload_csv_to_mongo("reviews_data.xlsx", "reviews_data")

print("✅ Data uploaded successfully!")
