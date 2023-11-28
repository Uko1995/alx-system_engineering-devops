# Using Puppet, install flask from pip3

exec{ 'puppet-lint':
    command => '/usr/bin/gem install puppet-lint',
}
