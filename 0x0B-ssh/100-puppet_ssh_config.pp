#  using Puppet to make changes to our configuration file
exec { 'echo':
  command => "/usr/bin/echo 'Host 155255-web-01\n  Hostname 18.210.14.42\n  IdentityFile ~/.ssh/school\n  BatchMode yes' > ~/.ssh/config",
  returns => [0,1,2]
}
