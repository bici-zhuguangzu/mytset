package { 'httpd':
    ensure => installed,
}


file { 'name':
    ensure => file,
}

service { 'mysql':
    enable      => true,
    ensure      => running,
    #hasrestart => true,
    #hasstatus  => true,
    #require    => Class["config"],
}
cron { 'ls':
    command  => 'curl',
    user     => 'root',
    month    => '*',
    monthday => '*',
    hour     => '*',
    minute   => '*',
}
yumrepo { 'epel':
    baseurl    => 'yum',
    descr      => 'The epel repository',
    enabled    => '1',
    gpgcheck   => '1',
    gpgkey     => 'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-epel',
    mirrorlist => ''
}
exec { 'ls':
    command      => '/bin/echo',
    #path        => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
    refreshonly => true,
    require => package[http]
    noifity => base::service
}