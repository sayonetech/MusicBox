

sudo mkdir /var/www
sudo mkdir -p /var/log/{uwsgi,nginx}
sudo mkdir -p /var/log/nginx/{musicbox,musicbox-reports}
sudo mkdir /etc/uwsgi

sudo chown ubuntu /var/www
sudo chown ubuntu /etc/uwsgi
