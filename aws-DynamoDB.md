read requests  -- eventual consistency [default] aws picks AZ 
               -- strongly consistent -- more expensive $ specific AZ
               
sudo pip3 install boto3    # aws python sdk

docker pull amazon/dynamodb-local

docker run -p 8000:8000 amazon/dynamodb-local

