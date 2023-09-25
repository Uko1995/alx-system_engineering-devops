# changing configuration file using puppet 
file { 'config_file':
  path    => '/etc/ssh/ssh_config',
  ensure  => present,
}

file_line {'edit_password':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^#?PasswordAuthentication',
  ensure  => present
}

file_line {'edit_IdentityFile':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?IdentityFile ~/.ssh/id_rsa',
  ensure  => present,
}
