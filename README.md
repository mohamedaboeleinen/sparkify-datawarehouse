# Udacity Data Warehouse course project
## etl-notebook
I used the etl-notebook as an oppurtunity to learn how to set up postgres database locally and also to practice using a jupyter notebook as a staging environment for my code before I try it in the amazon cluster to save time spent in the redshift cluster and thus saving $$$.
### Prerequisites 
1. psycopg2
2. pandas 
3. boto3
4. json
5. You need to have a postgres database running locally, with a database named 'dwhstaging', user named 'admin' and password 'admin'. You need to grant your user previledges to work on the public schema:


        postgres=# \c dwhstaging 
    
        You are now connected to database "dwhstaging" as user "postgres".

        dwhstaging=# GRANT ALL  ON SCHEMA public TO admin;

        GRANT

        dwhstaging=# GRANT ALL  ON SCHEMA public TO admin;

