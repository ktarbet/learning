
import os
def run_polly(filename):
  prefix = filename[:3]
  command = f"""
  aws polly start-speech-synthesis-task \
    --region us-west-1 \
    --endpoint-url "https://polly.us-west-1.amazonaws.com/" \
    --output-format mp3 \
    --output-s3-bucket-name my-story-mp3 \
    --output-s3-key-prefix {prefix} \
    --text-type ssml \
    --voice-id Joanna \
    --text 'file://{filename}'
  """
  print(command)
  os.system(command)

run_polly('001_introduction.txt')
run_polly('002_Burley Idaho.txt')
run_polly('003_Caroline Tarbet’s Personal History.txt')
run_polly('004_Benson Moving and buildings.txt')
run_polly('005_Benson Dads Farm.txt')

# truncated..
