# 0x1B-web_stack_debugging_4/manifests/init.pp
# This Puppet manifest optimizes the Nginx configuration to handle high loads and reduce failed requests.

class web_stack_debugging_4::nginx_config {
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
        command => 'sed -i "s/worker_connections [0-9]*/worker_connections 10240/" /etc/nginx/nginx.conf && nginx -s reload',
        onlyif  => 'grep -q "worker_connections [0-9]*;" /etc/nginx/nginx.conf',
        require => File['/etc/nginx/nginx.conf'],
    }

    exec { 'increase_nginx_worker_processes':
        command => 'sed -i "s/worker_processes [0-9]*/worker_processes auto/" /etc/nginx/nginx.conf && nginx -s reload',
        onlyif  => 'grep -q "worker_processes [0-9]*;" /etc/nginx/nginx.conf',
        require => File['/etc/nginx/nginx.conf'],
    }

    exec { 'increase_nginx_client_body_buffer_size':
        command => 'sed -i "s/client_body_buffer_size [0-9]*k;/client_body_buffer_size 256k;/" /etc/nginx/nginx.conf && nginx -s reload',
        onlyif  => 'grep -q "client_body_buffer_size [0-9]*k;" /etc/nginx/nginx.conf',
        require => File['/etc/nginx/nginx.conf'],
    }

    exec { 'increase_nginx_client_max_body_size':
        command => 'sed -i "s/client_max_body_size [0-9]*m;/client_max_body_size 10m;/" /etc/nginx/nginx.conf && nginx -s reload',
        onlyif  => 'grep -q "client_max_body_size [0-9]*m;" /etc/nginx/nginx.conf',
        require => File['/etc/nginx/nginx.conf'],
    }

    exec { 'increase_nginx_keepalive_timeout':
        command => 'sed -i "s/keepalive_timeout [0-9]*;/keepalive_timeout 75;/" /etc/nginx/nginx.conf && nginx -s reload',
        onlyif  => 'grep -q "keepalive_timeout [0-9]*;" /etc/nginx/nginx.conf',
        require => File['/etc/nginx/nginx.conf'],
    }
}
