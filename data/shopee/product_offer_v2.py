from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import List

class ProductOfferNode(BaseModel):
    productName: str
    itemId: int
    commissionRate: str
    commission: str
    price: str
    sales: int
    imageUrl: HttpUrl
    shopName: str
    productLink: HttpUrl
    offerLink: HttpUrl
    periodStartTime: datetime
    periodEndTime: datetime
    priceMin: str
    priceMax: str
    productCatIds: List[int]
    ratingStar: str
    priceDiscountRate: int
    shopId: int
    shopType: List[int]
    sellerCommissionRate: str
    shopeeCommissionRate: str

class ProductOfferV2(BaseModel):
    nodes: List[ProductOfferNode]

class Data(BaseModel):
    productOfferV2: ProductOfferV2

class ProductOfferV2Object(BaseModel):
    data: Data
