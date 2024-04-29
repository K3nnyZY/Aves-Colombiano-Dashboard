-- CREATE DATABASE IF NOT EXISTS aves --
SELECT 'CREATE DATABASE aves-colombia-db'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'aves-colombia-db')\gexec
