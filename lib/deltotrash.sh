#!/bin/bash
fp=$1
if [[ -d "$fp" ]]; then
    fp=$(cd $fp;pwd)
elif [[ -e "$fp" || -L "$fp" ]];then
    fp=$(cd $(dirname "$fp");pwd)/$(basename "$fp")
else
    echo "Error: '$fp' could not be found, or permission denied"
    exit
fi
#avoid to delete /
if [[ $fp == '/' ]];then
    echo "Error: you cant rm / to trash"
    exit
fi

osascript << EOF
tell application "Finder"
    posix path of ((delete posix file "${fp}") as unicode text)
end tell
EOF

