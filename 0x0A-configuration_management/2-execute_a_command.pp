# Using puppet create a manifest that kilss a process

exec { 'killmenow'
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
