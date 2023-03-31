# Import the modules
import subprocess
import whisper
import openai
# Load the modal
model = whisper.load_model("base")
# Ask "How can I help you?"
subprocess.run(['say', 'how can i help you'])
# Record to the user and save the recording to a new file called said.mp3
subprocess.run(['ffmpeg', '-y', '-f', 'avfoundation', '-i', ':4', '-t', '10', 'said.mp3'], # Change :4 to your audio device number
   stderr=subprocess.DEVNULL)
# Transcribe the audio file
result = model.transcribe("said.mp3", fp16=False)
# Print out what they said
print(result["text"])
# Add you open-ai key (that you can get at https://platform.openai.com/account/api-keys)
openai.api_key = 'sk-xxx' # Put your key inside the single quotes
# Have ChatGPT provide an answer to the question
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": result["text"]}])
# Print out the answer
print(completion.choices[0].message.content)
# Play the answer out of the speaker
subprocess.run(['say', completion.choices[0].message.content])