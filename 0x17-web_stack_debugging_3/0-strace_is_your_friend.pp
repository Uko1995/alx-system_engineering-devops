# fixes the bug in the file and it  makes it work

exec {'replaces wrong php filetype':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  onlyif  => 'test -f /var/www/html/wp-settings.php'
}
