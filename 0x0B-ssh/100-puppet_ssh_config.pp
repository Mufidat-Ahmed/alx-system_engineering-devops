#Client configuration file

file { '/home/745335237cf2/.ssh/config':
  ensure  => file,
  owner   => '745335237cf2',
  group   => '745335237cf2',
  mode    => '0600',
  content => "# SSH client configuration\n
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
}
