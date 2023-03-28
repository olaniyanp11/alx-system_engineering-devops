# create a file in /tmp using Puppet
file { '/tmp/school':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => "I love Puppet\n",
}
