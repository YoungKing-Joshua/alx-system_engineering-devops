# Script to install nginx using puppet

class web server {
	package { 'nginx':
		ensure => 'present',
		}

	exec { 'install':
		command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
		provider => shell,
		}

	exec { 'Hello World!':
		command  => 'echo "Hello World!" | sudo dd status=none of=/var/www/html/redirect.html',
		provider => shell,
		}

	exec { 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.youtube.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
	provider => shell,
	}
	exec { 'run':
		command  => 'sudo service nginx restart',
		provider => shell,
		}
}
