# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('my_module/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Increase file limit for Nginx
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 4096'",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx service when configuration changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
  subscribe => File['/etc/nginx/nginx.conf', '/etc/default/nginx'],
}
