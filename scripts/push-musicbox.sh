#!/bin/bash

COMMENT=$1
HOME='/Users/david'

if [ -z "${COMMENT}" ]; then
    echo "Enter git comment: "
    read COMMENT
fi

echo ">> git add $HOME/Projects/MusicBox"
git add $HOME/Projects/MusicBox
echo
echo ">> git status"
git status
echo
echo ">> git pull"
git pull
echo
echo ">> git commit -a -m \"$COMMENT\""
git commit -a -m "$COMMENT"
echo
echo ">> git push"
git push

