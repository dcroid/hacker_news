#!/usr/bin/env bash


_c_path=$PWD
_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd $_path


docker-compose build
docker-compose up -d mysql redis
docker-compose run web bash scripts/migrate.sh
docker-compose run web bash scripts/get_news.sh
echo "Finished update"

cd "$_c_path"