from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId
from typing import Optional, List

class DatabaseManager:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://avi4u14369:dpdjWmGQU3bQ4EPh@cluster69.09plh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster69')
        self.db = self.client['Cluster69']
        self.collection = self.db.trends

    def save_trends(self, trends: List[str], ip_address: str) -> str:
        """Save trending topics to database."""
        document = {
            'trends': trends,
            'ip_address': ip_address,
            'timestamp': datetime.utcnow() 
        }
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def get_trends_by_id(self, trend_id: str) -> Optional[dict]:
        """Retrieve trending topics by ID."""
        try:
            trend = self.collection.find_one({"_id": ObjectId(trend_id)})
            if trend:
                
                trend['_id'] = str(trend['_id'])
                
                trend.setdefault('timestamp', datetime.utcnow())
                return trend
            return None
        except Exception as e:
            print(f"Error retrieving trends: {str(e)}")
            return None