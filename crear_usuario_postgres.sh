#!/bin/bash


sudo -i -u postgres psql <<EOF
DO
\$do\$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles WHERE rolname = 'curro'
   ) THEN
      CREATE ROLE curro WITH SUPERUSER CREATEDB CREATEROLE LOGIN PASSWORD '1';
   END IF;
END
\$do\$;
EOF
