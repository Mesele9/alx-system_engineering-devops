file { '/home/ubuntu/.ssh/config':
    ensure => 'present',
    owner  => 'ubuntu',
    group  => 'adm',
    mode   => '0600',
    content => "Host 54.80.197.65\n
                IdentityFile ~/.ssh/school\n
                PreferredAuthentications publickey\n
                PasswordAuthentication no\n",
}

