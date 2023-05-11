# fixing wordpress configuration error in the include statement

exec { 'fix_wp_settings_include':
  command     => "sed -i 's/require_once( ABSPATH \\. WPINC \\. \\\/class-wp-locale\\.phpp' \\);/require_once( ABSPATH \\. \
                  WPINC \\. \\\/class-wp-locale\\.php' \\);/g' /var/www/html/wp-settings.php",
  path        => '/bin:/usr/bin',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
  require     => Package['wordpress'],
}
