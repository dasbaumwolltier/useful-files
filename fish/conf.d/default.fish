if test -x (which emacs 2>&1 > /dev/null)
    set -gx EDITOR (which nano)
else if test -x (which nano 2>&1 > /dev/null)
    set -gx EDITOR (which nano)
end