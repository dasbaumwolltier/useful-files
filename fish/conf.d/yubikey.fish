set -gx SSH_ASKPASS (which ksshaskpass)
#set -gx GPG_TTY (tty)

pgrep ssh-agent 2>&1 > /dev/null
if test $status -eq 0
    killall ssh-agent 2>&1 > /dev/null
    killall gpg-agent 2>&1 >/dev/null
end

pgrep gpg-agent 2>&1 > /dev/null
if test $status -eq 1
    gpg-agent --daemon --enable-ssh-support 2>&1 > /dev/null
end

set -gx SSH_AUTH_SOCK (gpgconf --list-dirs agent-ssh-socket)
echo UPDATESTARTUPTTY | gpg-connect-agent 2>&1 > /dev/null