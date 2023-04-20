class nginx_custom_header {

  # Update the apt package manager
  exec { 'apt-update':
    command => 'apt-get update',
    path    => ['/usr/bin', '/usr/sbin'],
    timeout => 0,
  }

  # Install Nginx server
  package { 'nginx':
    ensure  => installed,
    require => Exec['apt-update'],
  }

  # Add custom header to Nginx configuration
  file_line { 'nginx-custom-header':
    path    => '/etc/nginx/nginx.conf',
    line    => 'add_header X-Served-By $hostname;',
    require => Package['nginx'],
  }

  # Restart Nginx server
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File_line['nginx-custom-header'],
  }
}

include nginx_custom_header
