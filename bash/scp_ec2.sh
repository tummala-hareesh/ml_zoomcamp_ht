. ./bash/ec2_public.sh
scp -i ./bash/ec2_zoomcamp_pair.pem $1 ubuntu@${ec2_public}:/home/ubuntu
