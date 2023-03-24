#kills a process named killmenow

exec { 'pkill -9 killmenow':
  command => '/usr/bin/pkill -9 killmenow'
}
