# A puppet script that replace a line in a file on server

$edited_file = '/var/www/html/wp-settings.php'


exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${edited_file}",
  path    => ['/bin','/usr/bin']
}
