# !/bin/sh
#
# Launch docker-compose with the database initiated
#

cd $(dirname $0)

# Rebuild the image (required if dependencies change)
docker-compose -p Mydocker -f docker-compose.yml build

# Run npm scripts to build the spec and migrate the database
docker-compose -p Mydocker -f docker-compose.yml run --rm -d --entrypoint="sh -c \"alembic upgrade head\""

# Start web and server
docker-compose -f docker-compose.yml -p Mydocker up -d