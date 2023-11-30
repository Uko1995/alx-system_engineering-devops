# site.pp or your_manifest.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define the Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  content => "\
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        return 200 'Hello World!';
    }

    location /redirect_me {
        return 301 https://example.com/redirected-page;
    }
}
",
  notify  => Service['nginx'],
}

# Restart Nginx when the configuration changes
file { '/etc/nginx/sites-available/default':
  notify => Service['nginx'],
}

