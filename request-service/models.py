from mongoengine import Document, StringField, FloatField, IntField
from pydantic import BaseModel
from datetime import datetime as dt

#   Pedro Díaz | 23-05-2024
#   models.py:
#       clase BTCars(Document): Modelo definido para utilización de ODM 
#       (Object Document Modeling) utilizando mongoengine.
#       
#
#       clase BTCarsData(BaseModel): Modelo que utilizo para parsear datos 
#        ntes de guardar en DB.
#

class BTCars(Document):
    meta = {'collection' : 'btcars'}

    currency = StringField(max_length=32, required=True)
    bid_currency = StringField(max_length=32, required=True)
    ask_currency = StringField(max_length=32, required=True)
    purchase_price = FloatField(required=True)
    selling_price = FloatField(required=True)
    open_price = FloatField(required=True)
    market_identifier = StringField(max_length=32, required=True)
    timestamp = IntField(required=True)

    @property
    def serialize(self):
        return {
            'id' : str(self.id),
            'currency' : self.currency,
            'bid_currency' : self.bid_currency,
            'ask_currency' : self.ask_currency,
            'purchase_price' : self.purchase_price,
            'selling_price' : self.selling_price,
            'open_price' : self.open_price,
            'market_identifier' : self.market_identifier,
            'timestamp' : self.timestamp
        }
    
class BTCarsData(BaseModel):
    currency: str
    bid_currency: str
    ask_currency: str
    purchase_price: float
    selling_price: float
    open_price: float
    market_identifier: str
    timestamp: int