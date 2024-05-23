from api import db
#   Pedro Díaz | 23-05-2024
#   models.py:
#       clase BTCars(Document): Modelo definido para utilización de ODM 
#       (Object Document Modeling) utilizando mongoengine.
#       
#
#       clase BTCarsData(BaseModel): Modelo que utilizo para parsear datos 
#        ntes de guardar en DB.
#

class BTCars(db.Document):
    meta = {'collection' : 'btcars'}

    currency = db.StringField(max_length=32, required=True)
    bid_currency = db.StringField(max_length=32, required=True)
    ask_currency = db.StringField(max_length=32, required=True)
    purchase_price = db.FloatField(required=True)
    selling_price = db.FloatField(required=True)
    open_price = db.FloatField(required=True)
    market_identifier = db.StringField(max_length=32, required=True)
    timestamp = db.IntField(required=True)

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