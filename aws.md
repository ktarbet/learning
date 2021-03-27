https://aws.amazon.com/getting-started/hands-on/backup-to-s3-cli/

usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
  
  C:\> aws s3 mb s3://nice-bucket-2021-03-26
make_bucket: nice-bucket-2021-03-26

C:\>aws s3 rb s3://delete-me
remove_bucket: delete-me

aws s3 cp “C:\users\my first backup.bak” s3://my-first-backup-bucket/
