# Using puppet create a manifest that kilss a process

Exec { path => '/usr/bin:/bin' }

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
}
