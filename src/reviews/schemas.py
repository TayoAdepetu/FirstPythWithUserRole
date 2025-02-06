from pydantic import BaseModel
import uuid
from datetime import datetime
from typing import Optional

class ReviewModel(BaseModel):
    id: int
    uid: uuid.UUID 
    rating: int 
    review_text: str
    user_uid: Optional[uuid.UUID] 
    book_uid: Optional[uuid.UUID] 
    created_at: datetime 
    updated_at: datetime 

class ReviewCreateModel:

    rating: int
    review_text: str
