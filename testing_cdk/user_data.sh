#!/bin/bash

yum install jq -y
REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone | sed 's/\(.*\)[a-z]/\1/')
SSH_DATA=$(aws secretsmanager get-secret-value --secret-id yasir-test --query SecretString --region $REGION --output text)
User_Array+=$(echo $SSH_DATA | jq 'keys' | jq -r '.[]')

for user in $User_Array
do
ssh_key=$(echo $SSH_DATA | jq -r --arg user $user '.[$user]')
adduser $user
sudo -i -u $user bash << EOF
mkdir ~/.ssh
chmod 700 ~/.ssh
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
cat > ~/.ssh/authorized_keys <<- EOM
$ssh_key
EOM
EOF

done