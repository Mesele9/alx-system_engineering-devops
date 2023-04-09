# install nginx

package {'nginx':
  ensure  => 'present',
}

file_line {'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\ttadd_header X-Served-By \"${hostname}\";",
}

exec {'run':
  command => '/usr/sbin/service nginx restart',
}
