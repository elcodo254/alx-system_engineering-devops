#Fix bug by increasing amount of traffic handled on nginx server

#increase ULIMIT
exec { 'fix-default':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

#restart nginx
exec { 'nginx-restart':
  command => 'nginx restart'
  path    => '/etc/init.d/'
}
