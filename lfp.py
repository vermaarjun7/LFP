import pandas as pd
import motor.motor_asyncio
import asyncio
batch_size = 1000

class LFP:

    def __init__(self, dbname, collectionName, fileName):

        self._conn = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:password@mongo:27017/')
        self._db = self._conn[dbname]
        self._connName = collectionName
        self.df = pd.read_csv(fileName)
        print('connected')


    async def do_insert(self):

        _dfToDicts = self.df.to_dict(orient='records')
        result = await self._db[self._connName].insert_many(_dfToDicts)
        print('inserted %d docs' % (len(result.inserted_ids),))

    def runInsert(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.do_insert())

    async def updateRecord(self, sku, new_product=None, new_name=None,  new_description=None):

        fields_to_set = {}

        if new_description is not None:
            fields_to_set['description'] = new_description

        if new_name is not None:
            fields_to_set['name'] = new_name

        if new_product is not None:
            fields_to_set['product'] = new_product


        _filter = {'sku': sku}
        update_doc = {}

        if fields_to_set:
            update_doc['$set'] = fields_to_set


        await self._db[self._connName].update_one(_filter, update_doc)


    def runUpdate(self, sku, new_product=None, new_name=None,  new_description=None):

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.updateRecord(sku, new_product, new_name,  new_description))


    async def aggTable(self):

        pipeline = [

            {
                '$group': {
                    '_id': {
                        'name': '$name'
                    },
                    'num_products': {'$sum': 1}
                }

            },

            {
                '$project': {
                    'no\uff0Eof products': '$num_products'
                }
            },


            {
                '$out': 'newTableName'
            }
        ]

        cursor = self._db[self._connName].aggregate(pipeline)
        async for doc in cursor:
            print(doc)


    def runAgg(self):

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.aggTable())












if __name__ == '__main__':

    fileName = '/app/products.csv'
    db_name = 'userData'
    collection_name = 'test_collection'

    database = LFP(db_name, collection_name, fileName)

    #1st part
    database.runInsert()

    #2nd part
    #database.runUpdate('lay-raise-best-end', 'new_product', 'new_name')

    #3rd part
    database.runAgg()

