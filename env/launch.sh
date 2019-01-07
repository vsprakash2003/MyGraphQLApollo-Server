# !/bin/sh
#
# Launch docker-compose with the database initiated
#

cd $(dirname $0)

# Rebuild the image (required if dependencies change)
docker-compose -f docker-compose.yml build

# Start the sqlite3 image in background mode
docker-compose -f docker-compose.yml up -d nouchka/sqlite3

# Give the db a sec to spin up (TODO: Query process and confirm we're running)
sleep 5

# Run npm scripts to build the spec and migrate the database
docker-compose -f docker-compose.yml run --entrypoint="sh -c \"alembic upgrade head\"" server

# Start web and server
docker-compose -f docker-compose.yml up