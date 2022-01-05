# connect to a server Execute a command
exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" > ~/.ssh/ssh_config':
        path    => '/bin/'
}
