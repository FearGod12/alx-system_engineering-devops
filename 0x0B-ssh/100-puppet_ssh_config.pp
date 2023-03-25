#  using Puppet to make changes to our configuration file
file { '/home/vagrant/.ssh/config':
  ensure  => present,
  content => "Host 155255-web-01\n  Hostname 18.210.14.42\n  IdentityFile ~/.ssh/school\n  BatchMode yes"
}
