function start --description "Open using the default program"
    xdg-open $argv[1..-1]   
end

function ls --description "ls with color"
    /bin/ls --color=always $argv[1..-1]
end