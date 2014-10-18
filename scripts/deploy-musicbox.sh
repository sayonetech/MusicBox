#!/bin/bash

#WEBSRV='insight.davidbianco.net'
#DATSRV='cluster.davidbianco.net'
#SSHCMD='ssh -i $HOME/.ssh/insight-cloudera.pem ubuntu@$SRV '
#GITPULL='cd /home/ubuntu/MusicBox;git pull'
#CMD='cp -rp /home/ubuntu/MusicBox/WebServer/www/* /var/www/.'
#
#echo $SSHCMD \'$GITPULL\'
#$SSHCMD $GITPULL

#echo $SSHCMD \'$CMD\'
#$SSHCMD $CMD

HOME='/Users/david'

PS3='Please enter your choice: '
options=("Pull-Push from Laptop" "Pull on DataServer" "Pull on WebServer" "Deploy www files" "Deploy conf-nginx files" "Deploy conf-uwsgi files" "Restart Webserver" "Restart uWSGI" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Pull-Push from Laptop")
            CMD="$HOME/bin/push-musicbox.sh"
            echo;echo ">> $CMD"
            $CMD
            ;;
        "Pull on DataServer")
            SSHCMD="ssh -i $HOME/.ssh/insight-cloudera.pem ubuntu@cluster.davidbianco.net "
            CMD="cd /home/ubuntu/MusicBox;git pull"
            echo;echo ">> $SSHCMD \"$CMD\""
            $SSHCMD $CMD
            ;;
        "Pull on WebServer")
            SSHCMD="ssh -i $HOME/.ssh/insight-cloudera.pem ubuntu@insight.davidbianco.net "
            CMD="cd /home/ubuntu/MusicBox;git pull"
            echo;echo ">> $SSHCMD \"$CMD\""
            $SSHCMD $CMD
            ;;
        "Deploy www files")
            SSHCMD="ssh -i $HOME/.ssh/insight-cloudera.pem ubuntu@insight.davidbianco.net "
            CMD="cp -rp /home/ubuntu/MusicBox/WebServer/www/* /var/www/."
            echo;echo ">> $SSHCMD \"$CMD\""
            $SSHCMD $CMD
            ;;
        "Deploy conf-nginx files")
            SSHCMD="ssh -i $HOME/.ssh/insight-cloudera.pem ubuntu@insight.davidbianco.net "
            CMD="sudo cp /home/ubuntu/MusicBox/WebServer/conf/musicbox-*nginx.conf /etc/nginx/sites-available/."
            echo;echo ">> $SSHCMD \"$CMD\""
            $SSHCMD $CMD
            ;;
        "Deploy conf-uwsgi files")
            SSHCMD="ssh -i $HOME/.ssh/insight-cloudera.pem ubuntu@insight.davidbianco.net "
            CMD="sudo cp /home/ubuntu/MusicBox/WebServer/conf/musicbox*.ini /etc/uwsgi/.;sudo cp /home/ubuntu/MusicBox/WebServer/conf/uwsgi*.conf /etc/init/."
            echo;echo ">> $SSHCMD \"$CMD\""
            $SSHCMD $CMD
            ;;
        "Restart Webserver")
            SSHCMD="ssh -i $HOME/.ssh/insight-cloudera.pem ubuntu@insight.davidbianco.net "
            CMD="sudo nginx -s reload"
            echo;echo ">> $SSHCMD \"$CMD\""
            $SSHCMD $CMD
            ;;
        "Restart uWSGI")
            SSHCMD="ssh -i $HOME/.ssh/insight-cloudera.pem ubuntu@insight.davidbianco.net "
            CMD="sudo service uwsgi restart;sudo service uwsgi-musicbox-reports restart"
            echo;echo ">> $SSHCMD \"$CMD\""
            $SSHCMD $CMD
            ;;
        "Quit")
            echo "quitting..."
            break
            ;;
        *) echo invalid option;;
    esac
done

