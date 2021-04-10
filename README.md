# LFP
Large file processor Assignment



## Steps to run code

docker-compose up -d

This command will ingest the records as well make the aggregated table with the specified columns.

There is a separate function to do the updation of products table which is commented in the code. 
It takes sku and new values of the fields 
product -  'new_product'
name- 'new_name' 
as an input
Uncomment it on line 116 to test it as well



## Details of all the tables and their schema

All the tables are stored in one database. There is one table which contains all the records of products.csv file named 'test_collection' and another table which contains the aggregated information of `sku` and `no. of products` called 'newTableName'.
The database gets initiliazed automatically after it creates an image. And MongoDB created a new collection name itself when we do bulk insert operation for the first time.

Commands to recreate the tables 
In docker-compose.yml file the database name is initiliased
In the code, in class constructor, the collection name is specified. Change the collection name and rebuild the docker container to insert the data to the desired collection.

## Points to achieve

Completed the a), b), d) and e)


For c) I've assumed that to update existing products, we would want to update either name or product or both of the fields given the "sku" value.


![Screen Shot 2021-04-10 at 8 06 38 PM](https://user-images.githubusercontent.com/5204856/114278377-23e06580-9a4d-11eb-9afd-d0137a239ac2.png)

![Screen Shot 2021-04-10 at 8 06 13 PM](https://user-images.githubusercontent.com/5204856/114278369-1fb44800-9a4d-11eb-9ca3-7d43e83664b1.png)

## What would you improve if given more days

Revisit the updation part and do more EDA on the data.



