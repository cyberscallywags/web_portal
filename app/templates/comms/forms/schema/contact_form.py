from pydantic import BaseModel, EmailStr
from datetime import datetime

# Contact form data model
class ContactFormData(BaseModel):
    formType: str
    name: str
    email: EmailStr
    role: str = ""
    message: str = ""
    consent: bool
    submitted_at: str

    def __init__(self, **data):
        data['submitted_at'] = datetime.utcnow().isoformat()
        super().__init__(**data)
