from pymongo import MongoClient

# MongoDB connection string
connection_string = "mongodb+srv://dhruv:dhruv1234@cluster0.knlmy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a MongoClient object
client = MongoClient(connection_string)

# Access the database
db = client.get_database('PythonConnection')  #  database name

# Access a collection
collection = db.get_collection('test')    

# Test connection by printing the count of documents in the collection
print(f"Number of documents in the collection: {collection.count_documents({})}")

# Close the connection
client.close()
