DROP DATABASE rcclub;
CREATE DATABASE rcclub;

\c rcclub
CREATE EXTENSION pgcrypto;
CREATE user clubbot WITH LOGIN;

create table events(id serial primary key,
					name text,
					day date,
					etime time,
					location text,
					contact text );

create table members (name text,
                      phone text,
                      email text PRIMARY KEY,
                      password text,
                      about text);

GRANT SELECT, INSERT ON events TO clubbot;
GRANT SELECT, INSERT ON members TO clubbot;
GRANT SELECT, USAGE ON events_id_seq TO clubbot;
