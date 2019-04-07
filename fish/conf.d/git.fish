function gpsh --description "Calls the command git push (while preserving additional arguments)"
    git push $argv[1..-1]
end

function gpl --description "Calls the command git pull (while preserving additional arguments)"
    git pull $argv[1..-1]
end

function gco --description "Calls the command git commit (while preserving additional arguments)"
    git commit $argv[1..-1]
end

function gre --description "Calls the command git rebase (while preserving additional arguments)"
    git rebase $argv[1..-1]
end

function grei --description "Calls the command git rebase --interactive (while preserving additional arguments)"
    git rebase --interactive $argv[1..-1]
end