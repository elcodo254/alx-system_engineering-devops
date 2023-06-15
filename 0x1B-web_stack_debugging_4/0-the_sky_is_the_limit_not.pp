#Fix bug by increasing amount of traffic handled on nginx server

#increase ULIMIT
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
#restart nginx
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
