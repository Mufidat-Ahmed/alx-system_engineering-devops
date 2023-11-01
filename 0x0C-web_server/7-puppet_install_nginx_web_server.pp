class { 'nginx':
  package_manage => 'present',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'file',
  content => "Hello World!\n",
  require => Class['nginx'],
}

nginx::resource::server { 'default':
  server_name => '_',
  location    => {
    '/'          => {
      root => '/var/www/html',
      index => 'index.nginx-debian.html',
    },
    '/redirect_me' => {
      rewrite => 'https://github.com/Mufidat-Ahmed permanent',
    },
    '/404.html'   => {
      internal => 'true',
    },
  },
  require     => File['/var/www/html/index.nginx-debian.html'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Class['nginx'],
}
