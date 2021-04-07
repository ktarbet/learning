
backup -- sync..
aws s3 sync karl  s3://backup-bucket-2021-04-06/karl  --storage-class GLACIER

https://aws.amazon.com/getting-started/hands-on/backup-to-s3-cli/

usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
  
  C:\> aws s3 mb s3://nice-bucket-2021-03-26
make_bucket: nice-bucket-2021-03-26

C:\>aws s3 rb s3://delete-me
remove_bucket: delete-me

C:\>aws s3 cp SeriesExplorer.doc s3://this-bucket-backup-2021-03-26
upload: .\SeriesExplorer.doc to s3://this-bucket-backup-2021-03-26/SeriesExplorer.doc

#GLACIER

aws glacier upload-archive --account-id - --vault-name my-vault --body archive.zip
