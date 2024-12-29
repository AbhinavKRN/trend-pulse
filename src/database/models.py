from datetime import datetime
from typing import List, Optional
from pymongo import MongoClient
from bson import ObjectId

class TrendingTopic:
    def __init__(self, 
                 trend_names: List[str], 
                 timestamp: datetime,
                 ip_address: str,
                 _id: Optional[ObjectId] = None):
        self._id = _id or ObjectId()
        self.trend_names = trend_names
        self.timestamp = timestamp
        self.ip_address = ip_address

    def to_dict(self):
        return {
            "_id": self._id,
            "trend_names": self.trend_names,
            "timestamp": self.timestamp,
            "ip_address": self.ip_address
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            trend_names=data["trend_names"],
            timestamp=data["timestamp"],
            ip_address=data["ip_address"],
            _id=data.get("_id")
        )