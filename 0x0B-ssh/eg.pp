# Client configuration file

file { '/home/745335237cf2/.ssh/config':
  ensure  => file,
  owner   => '745335237cf2',
  group   => '745335237cf2',
  mode    => '0600',
  content => "# SSH client configuration\n
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
  require => File['/home/745335237cf2'],
}

file { '/home/745335237cf2/.ssh':
  ensure => directory,
  owner  => '745335237cf2',
  group  => '745335237cf2',
  mode   => '0700',
  require => File['/home/745335237cf2'],
}

