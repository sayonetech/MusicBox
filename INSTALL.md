
### AWS Cluster
1 m1.large (Namenode) ami-0c5b5f49
3 m1.medium (Datanodes) ami-0c5b5f49
1 m1.small (Webserver) ami-f1fdfeb4

ssh ~/.ssh/key.pem insight-webserver
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
git clone https://github.com/talldave/MusicBox
