export SSH_ASKPASS=(which ksshaskpass)
export GPG_TTY=(tty)

pgrep gpg-agent
if $status == 1
    gpg-agent --daemon --enable-ssh-support
end
export SSH_AUTH_SOCK=(gpgconf --list-dirs agent-ssh-socket)

function start --description "Open using the default program"
    xdg-open $argv[1..-1]
end

function ls --description "ls with color"
    /bin/ls --color=always $argv[1..-1]
end