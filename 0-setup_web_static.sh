#!/usr/bin/env bash
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
<head>
    <title></title>
</head>
<body> 
</body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -snf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu. /data/
sudo sed -i "26ilocation /hbnb_static/ {" /etc/nginx/sites-available/default
sudo sed -i "27ialias /data/web_static/current/;" /etc/nginx/sites-available/default
sudo sed -i "28iautoindex off;" /etc/nginx/sites-available/default 
sudo sed -i "29i}" /etc/nginx/sites-available/default
sudo service nginx restart
