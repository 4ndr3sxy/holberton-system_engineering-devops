#Strace is your friend(using sed in file of settings of service apache2)
exec { 'curl-command':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php && sudo service apache2 restart',
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}
