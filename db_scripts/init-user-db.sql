\set dbuser `echo "$POSTGRES_USER"`
\set dbname `echo "$POSTGRES_DB"`
\set pwd `echo "$POSTGRES_PASSWORD"`

CREATE USER :dbuser;
CREATE DATABASE :'dmname';
GRANT ALL PRIVILEGES ON DATABASE :'dbname' TO :'dbuser';
