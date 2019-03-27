export SSH_ASKPASS=(which ksshaskpass)
export GPG_TTY=(tty)

pgrep ssh-agent
if $status == 0
    killall ssh-agent 2>&1 > /dev/null
    killall gpg-agent 2>& 1 >/dev/null
end

pgrep gpg-agent
if $status == 1
    gpg-agent --daemon --enable-ssh-support
end
export SSH_AUTH_SOCK=(gpgconf --list-dirs agent-ssh-socket)