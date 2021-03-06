#header
exec {'ensure update':
command  => 'sudo apt update',
provider => shell
}
-> package {'nginx':
  ensure => 'installed'
  }
-> file_line {'header':
path  => '/etc/nginx/nginx.conf',
match => 'http {',
line  => "http {\n\tadd_header X-Served-By ${hostname};"
}
-> exec {'start':
command => '/usr/sbin/service nginx restart'
}
