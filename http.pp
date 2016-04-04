# Class: httpd
#
# This class installs httpd
#
# Parameters:
#
# Actions:
#   - Install httpd
#   - Manage httpd service
#
# Requires:
#
# Sample Usage:
#
class httpd {
    class install {
        package {
            'package':
                ensure => present;
        }
    }

    class config {
        file {
            '/etc/httpd':
                ensure  => directory,
                owner   => root,
                group   => root,
                mode    => 700,
                require => Class["install"];

            '/etc/httpd/config':
                ensure  => present,
                owner   => root,
                group   => root,
                mode    => 600,
                require => Class['install'];
                #content => template ('httpd/config.erb");
                #source => [
                #   'puppet:///modules/httpd/${fqdn}.conf',
                #   'puppet:///modules/httpd/httpd.conf'
                #];
        }

        #logrotate::file { 'httpd':
        #   source => "/etc/logrotate.d/httpd',
        #   log => "/var/log/logfile.log",
        #}
    }

    class service {
        service { 'httpd':
            enable      => true,
            ensure      => running,
            #hasrestart => true,
            #hasstatus  => true,
            require     => Class["config"],
        }
    }

    include install
    include config
    include service

    Class["install"] ->
    Class["config"] ->
    Class["service"]
}
