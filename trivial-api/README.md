# Trivial REST API in Flask

### This is a trivial REST API that may be used as a simple demo.
---
Fred T. Dunaway:  fred.t.dunaway@gmail.com
---

## Set up
1. clone this repository (git clone https://github.com/mrncmoose/trivial_flask_api)
1. cd ~/trivial_flask_api/trivial-api
1. pip install -r requirements.txt
1. chmod 775 *.sh

## Running
./start.sh

## Stopping
./stop.sh

## Testing
To test the local REST API:
curl -u admin:change-me! -H "Accept: application/json" -H "Content-Type: application/json" -i http://localhost:5001/thermal/api/v1.0/current_temp

To test the reverse proxy:
curl -u admin:change-me! -H "Accept: application/json" -H "Content-Type: application/json" -i https://gcptest.ddns.net/thermal/api/v1.0/current_temp

### To Do's:
* Edit the file 'gcptest.ddns.net.conf' to change the domain name as required.
* Copy the file 'gcptest.ddns.net.conf' to /etc/nginx/sites-enabled/<your domain name here>.conf

### Use Jenkins to build & Test
Change for jenkins pickup two

wget -q --auth-no-challenge --user admin --password admin --output-document - \
'http://localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'

Jenkins-Crumb:b3b21fdc1e9ba7f0ddd9466af5935925bd0e8fb170927b58628b2fb8d9bf45ab
