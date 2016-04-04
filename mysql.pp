# Class: mysql
#
# This class installs mysql
#
# Parameters:
#
# Actions:
#   - Install mysql
#   - Manage mysql service
#
# Requires:
#
# Sample Usage:
#
class mysql {
    # Class: user
    #
    #
    class user {
        # resources
        user { 'guangzu':
          comment => 'First Last',
          home    => '/home/guangzu',
          ensure  => present,
          shell  => '/bin/bash',
          uid    => '501',
          gid    => '20',
          require group['guangzu']
        }
        group { 'guangzu':
            gid => '20',
        }
    }
    class install {
        package {
            'package':
                ensure => present;
        }
    }

    class config {
        file {
            '/etc/mysql':
                ensure  => directory,
                owner   => root,
                group   => root,
                mode    => 700,
                require => Class["install"];

            '/etc/mysql/config':
                ensure  => present,
                owner   => root,
                group   => root,
                mode    => 600,
                require => Class['install'];
                #content => template ('mysql/config.erb");
                #source => [
                #   'puppet:///modules/mysql/${fqdn}.conf',
                #   'puppet:///modules/mysql/mysql.conf'
                #];
        }

        #logrotate::file { 'mysql':
        #   source => "/etc/logrotate.d/mysql',
        #   log => "/var/log/logfile.log",
        #}
    }

    class service {
        service { 'mysql':
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
