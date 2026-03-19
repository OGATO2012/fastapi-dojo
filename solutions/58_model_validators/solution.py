from fastapi import FastAPI
from pydantic import BaseModel, model_validator
from typing import Optional

app = FastAPI()

class DateRange(BaseModel):
    start_date: str
    end_date: str
    
    @model_validator(mode="after")
    def check_date_order(self):
        if self.start_date >= self.end_date:
            raise ValueError("start_date must be before end_date")
        return self

class UserProfile(BaseModel):
    username: str
    password: str
    confirm_password: str
    
    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("passwords do not match")
        return self

@app.post("/date-range")
def validate_date_range(dr: DateRange):
    return {"start": dr.start_date, "end": dr.end_date, "valid": True}

@app.post("/register")
def register(profile: UserProfile):
    return {"username": profile.username, "registered": True}
