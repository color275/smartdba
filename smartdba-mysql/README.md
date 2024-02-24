# Dockerfile Run
```
# docker network rm smartdba
# docker volume rm smartdba-db
docker network create smartdba
docker volume create --name smartdba-db

docker run --name smartdba-mysql --network smartdba -v ${PWD}:/etc/mysql/conf.d -v smartdba-db:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=admin -d -p 0.0.0.0:3306:3306 mysql:8.0

mysql -uroot -padmin -h 0.0.0.0 -e "create database smartdba;"
mysql -uroot -padmin -h 0.0.0.0 -e "create user smartdba@'%' identified by 'smartdba';"
mysql -uroot -padmin -h 0.0.0.0 -e "grant all privileges on smartdba.* to smartdba@'%';"

# If you need a smartdba.sql file, please contact me separately
unzip sql/smartdba.zip -d ./sql/
mysql -uroot -padmin -h 0.0.0.0 smartdba < sql/smartdba.sql
```
