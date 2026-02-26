#!/bin/bash

#update packages
sudo apt update -y

sudo apt install nginx -y

cd /var/www/html

for i in {1..3}; do
	sudo touch "page$i.html";
        sudo chmod 644 "page$i.html";
	sudo chown samvel:samvel "page$i.html";
done

if systemctl is-active --quiet nginx; then
	echo "Nginx is active"
	sudo systemctl restart nginx
else
	echo "Is not active"
	sudo systemctl start nginx

fi
	sudo journalctl -u nginx -n 5
