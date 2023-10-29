# Puppet manifest to configure SSH client

file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "# SSH client configuration\n
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
}
