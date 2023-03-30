# using Puppet to make changes to our configuration file

file_line{'turn off password':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}

file_line{ 'Declare idebtity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}
