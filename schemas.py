"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (retain for reference)
class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Hospitality design studio: inbound inquiry schema
class Inquiry(BaseModel):
    """
    Inquiries from the website contact form
    Collection name: "inquiry"
    """
    name: str = Field(..., min_length=2, description="Sender full name")
    email: EmailStr = Field(..., description="Sender email")
    phone: Optional[str] = Field(None, description="Contact number")
    resort_or_company: Optional[str] = Field(None, description="Resort or company name")
    project_type: Optional[Literal[
        "Branding",
        "Logo Design",
        "Menu Design",
        "Brochure / Flyer",
        "Seasonal / Festive",
        "Website / Digital",
        "Other"
    ]] = Field(None, description="Primary service of interest")
    message: str = Field(..., min_length=10, description="Project details and goals")
    budget_range: Optional[str] = Field(None, description="Approximate budget range")
    timeline: Optional[str] = Field(None, description="Desired timeline")
