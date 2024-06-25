exec { 'fix-nginx-config':
  command => '/bin/sed -i "/worker_processes/c\worker_processes auto;" /etc/nginx/nginx.conf && \
              /bin/sed -i "/worker_connections/c\    worker_connections 1024;" /etc/nginx/nginx.conf && \
              /bin/sed -i "/keepalive_timeout/c\    keepalive_timeout 65;" /etc/nginx/nginx.conf && \
              /bin/sed -i "/sendfile on;/a\    tcp_nopush on;\n    tcp_nodelay on;" /etc/nginx/nginx.conf && \
              /bin/sed -i "/http {/a\    worker_rlimit_nofile 8192;" /etc/nginx/nginx.conf',
  onlyif  => '/bin/grep -q -e "worker_processes auto;" -e "worker_connections 1024;" -e "keepalive_timeout 65;" /etc/nginx/nginx.conf',
  notify  => Exec['reload-nginx'],
}

exec { 'reload-nginx':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
}

