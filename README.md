# LFP
Large file processor Assignment



#Steps to run code
docker-compose up -d


#Details of all the tables and their schema

All the tables are stored in one database. There is one table which contains all the records of products.csv file and another table which contains the aggregated information of `sku` and `no. of products`.
The database gets initiliazed automatically after it creates an image. And MongoDB created a new collection name itself when we do bulk insert operation for the first time. 

Commands to recreate the tables 
In docker-compose.yml file the database name is initiliazed
In the code, the collection name is specified. Change the collection name and rebuild the docker container to insert the data to the desired collection.

#Points to achieve

Completed the a), b), d) and e)


For c) I've assumed that to update existing products, we would want to update either name or product or both of the fields given "sku" value.


![Screen Shot 2021-04-10 at 8 06 38 PM](https://user-images.githubusercontent.com/5204856/114278377-23e06580-9a4d-11eb-9afd-d0137a239ac2.png)

![Screen Shot 2021-04-10 at 8 06 13 PM](https://user-images.githubusercontent.com/5204856/114278369-1fb44800-9a4d-11eb-9ca3-7d43e83664b1.png)

#What would you improve if given more days

Optimise the ingestion part



