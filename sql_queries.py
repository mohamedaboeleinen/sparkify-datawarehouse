import configparser


# CONFIG
config = configparser.ConfigParser()
## provide path to the configuration file, you can fill in the values in the template provided
config.read('mydwh.cfg')
log_data= config.get('S3','LOG_DATA')
song_data= config.get('S3','SONG_DATA')
iam_role=config.get('IAM_ROLE','ARN')


# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= (""" CREATE TABLE IF NOT EXISTS staging_events (
                                  artist        varchar, 
                                  auth          varchar, 
                                  gender        varchar, 
                                  iteminSession int, 
                                  last_name     varchar, 
                                  length        decimal, 
                                  level         varchar, 
                                  location      varchar, 
                                  song          varchar, 
                                  start_time    timestamp, 
                                  user_agent    varchar, 
                                  user_id       int          
); 
""")

staging_songs_table_create = (""" CREATE TABLE IF NOT EXISTS staging_songs (
                                  song_id int,
                                  title varchar,
                                  duration decimal, 
                                  year int, 
                                  artist_id int, 
                                  artist_name varchar, 
                                  artist_latitude decimal, 
                                  artist_longitude decimal, 
                                  artist_location varchar, 
                                  num_songs int

);
""")
# TODO: change serial type to match amazon redshift, check identity (0,1)
songplay_table_create = (""" CREATE TABLE IF NOT exists songplays (
                             songplay_id serial PRIMARY KEY,
                             start_time timestamp NOT NULL, 
                             user_id int NOT NULL, 
                             level varchar,
                             song_id varchar, 
                             artist_id varchar,
                             session_id int NOT NULL, 
                             location varchar NOT NULL, 
                             user_agent varchar NOT NULL
);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                        user_id int PRIMARY KEY, 
                        first_name varchar NOT NULL, 
                        last_name varchar NOT NULL, 
                        gender varchar NOT NULL, 
                        level varchar NOT NULL
);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                        song_id varchar PRIMARY KEY,
                        title varchar NOT NULL, 
                        artist_id varchar NOT NULL, 
                        year int NOT NULL, 
                        duration decimal NOT NULL
);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                        artist_id varchar PRIMARY KEY,
                        name varchar NOT NULL, 
                        location varchar, 
                        longitude float, 
                        latitude float
);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                         start_time timestamp PRIMARY KEY, 
                         hour int NOT NULL, 
                         day int NOT NULL, 
                         week int NOT NULL, 
                         month int NOT NULL, 
                         year int NOT NULL, 
                         weekday int NOT NULL
);
""")

# STAGING TABLES

staging_events_copy = (""" copy staging_events FROM {}
                                credentials 'aws_iam_role={}'
                                gzip DELIMETER ';' 
                                region 'us-west-2'
""").format(log_data, iam_role)

staging_songs_copy = ("""copy staging_songs FROM {}
                                credentials 'aws_iam_role={}'
                                gzip DELIMETER ';' 
                                region 'us-west-2'
""").format(song_data, iam_role)

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
