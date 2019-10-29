echo '---> Installing Nginx <----------'
sudo apt-get install nginx --yes
echo '---> Installing certbot <----------'
sudo apt-get install certbot --yes
sudo apt-get install certbot python-certbot-nginx --yes
echo '---> Installing pip <----------'
sudo apt-get install pip --yes
echo '---> Installing git <----------'
sudo apt-get install git --yes
sudo mkdir /var/www/html/.well-known
sudo mkdir /var/www/html/.well-known/acme-challenge
echo 'Cloning trivial REST API'
git clone https://github.com/mrncmoose/trivial_flask_api.git
cd ~/trivial_flask_api/trivial-api
echo '---> Installing Python packages <----------'
pip install -r requirements.txt
chmod 775 *.sh
