set filename (status --current-filename)
set currentUserDir ~(whoami)

if not string match -q -- "$currentUserDir*" $filename
    echo -e "\033[1;33mYou are not running the config.fish as the user who it belongs to!\033[0m"
end

function start --description "Open using the default program"
    xdg-open $argv[1..-1]
end

function ls --description "ls with color"
    /bin/ls --color=always $argv[1..-1]
end

if test -d conf.d
    for configFile in conf.d/*
        source $configFile
    end
end