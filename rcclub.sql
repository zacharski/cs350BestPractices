CREATE DATABASE rcclub;

\c rcclub

create table events(id serial primary key,
					name text,
					day date,
					etime time,
					location text,
					contact text );

create table members (name text,
                      phone text,
                      email text,
                      about text);