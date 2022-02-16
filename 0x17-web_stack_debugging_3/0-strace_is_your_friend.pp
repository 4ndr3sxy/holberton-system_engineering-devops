#Strace is your friend(using sed in file of settings of service apache2)
exec { 'curl-command':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php && sudo service apache2 restart',
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}


curl -X GET "https://api.datadoghq.com/api/v1/hosts" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: efb17bf66c12bfb34f788d744f3d337c" \
-H "DD-APPLICATION-KEY: 6beb4c7cd796c269212620ea40fdb28ae52ce167"
