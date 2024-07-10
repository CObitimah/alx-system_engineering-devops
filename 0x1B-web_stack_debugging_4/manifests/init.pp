# 0x1B-web_stack_debugging_4/manifests/init.pp
# This Puppet manifest optimizes the Nginx configuration to handle high loads and reduce failed requests.

class web_stack_debugging_4::nginx_optimization {
    file { '/etc/nginx/nginx.conf':
        ensure  => file,
        owner   => 'root',
        group   => 'root',
        mode    => '0644',
        content => template('web_stack_debugging_4/nginx.conf.erb'),
        notify  => Service['nginx'],
    }

    service { 'nginx':
        ensure    => running,
        enable    => true,
        subscribe => File['/etc/nginx/nginx.conf'],
    }

    exec { 'increase_file_limits':
        command => 'echo "fs.file-max = 100000" >> /etc/sysctl.conf && sysctl -p',
        unless  => 'sysctl -n fs.file-max | grep -q 100000',
        require => Service['nginx'],
    }

    exec { 'increase_nginx_worker_connections':
        command => 'sed -i "s/worker_connections [0-9]*/worker_connections 4096/" /etc/nginx/nginx.conf && nginx -s reload',
        onlyif  => 'grep -q "worker_connections [0-9]*;" /etc/nginx/nginx.conf',
        require => File['/etc/nginx/nginx.conf'],
    }

    exec { 'increase_nginx_worker_processes':
        command => 'sed -i "s/worker_processes [0-9]*/worker_processes auto/" /etc/nginx/nginx.conf && nginx -s reload',
        onlyif  => 'grep -q "worker_processes [0-9]*;" /etc/nginx/nginx.conf',
        require => File['/etc/nginx/nginx.conf'],
    }
}
