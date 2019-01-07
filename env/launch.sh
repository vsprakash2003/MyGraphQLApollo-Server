# !/bin/sh
#
# Launch docker-compose with the database initiated
#

cd $(dirname $0)

# Rebuild the image (required if dependencies change)
docker-compose -f docker-compose.yml build

# Build and start docker
docker-compose -f docker-compose.yml up -d

# Give the db a sec to spin up
sleep 5

# Run npm scripts to build the spec and migrate the database
docker-compose -f docker-compose.yml -p Mydocker run --rm -d --entrypoint="sh -c \"alembic upgrade head\""

# Start web and server
docker-compose -f docker-compose.yml up -d