# a puppet script that change the userlimit of holberton user

# Increase hard file limit for user holberton
exec { 'change_hard_nofile_for_holberton':
  command => 'sed -i "/holberton hard/s/5/2048/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for user holberton
exec { 'change_soft_nofile_for_holberton':
  command => 'sed -i "/holberton soft/s/4/2048/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
