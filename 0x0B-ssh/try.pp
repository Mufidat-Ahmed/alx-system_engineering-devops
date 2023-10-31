#Client configuration file

file { '/root/.ssh/config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "# SSH client configuration\n
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
  require => File['/root/.ssh'],
}

file { '/root/.ssh':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0700',
}
