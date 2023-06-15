#Fix bug by increasing amount of traffic handled on nginx server

#increase ULIMIT
exec {
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

#restart nginx
exec {
  command => 'nginx restart'
  path    => 'etc/init.d/'
}
