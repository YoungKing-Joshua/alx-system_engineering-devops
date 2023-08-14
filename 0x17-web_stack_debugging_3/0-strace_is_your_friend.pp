#Puppet config fix

$php_config_file = '/var/www/html/wp-settings.php'

exec { 'fix-php-config':
  command     => "sed -i 's/phpp/php/g' ${php_config_file}",
  path        => '/usr/local/bin/:/bin',
}

