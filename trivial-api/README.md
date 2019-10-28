# Trivial REST API in Flask
This is a trivial REST API that may be used as a simple demo.
Fred T. Dunaway
fred.t.dunaway@gmail.com

## Set up
1. clone this repository
1. pip install -r requirements.txt
1. chmod 775 *.sh

## Running
* ./start.sh

## Stopping
* ./stop.sh

## Testing
* curl -u admin:change-me! -H "Accept: application/json" -H "Content-Type: application/json" -i http://localhost:5001/thermal/api/v1.0/current_temp
