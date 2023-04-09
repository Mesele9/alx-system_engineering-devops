# install and configure nginx using puppet 

exec {'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure  => present,
}

file {'/etc/nginx/nginx.conf':
  ensure  => present,
  content => "add_header X-Served-By $hostname;",
}

exec {'run':
  command => '/usr/sbin/service nginx restart',
}
