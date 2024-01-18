# Trying to find out why Apache is returning error & fixing
exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path     => ['/bin', '/usr/bin'],
}
