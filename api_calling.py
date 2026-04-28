from google import genai
from dotenv import load_dotenv
import os,io
from gtts import gTTS


#loading the environment varriable
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")


#initializing a client
client= genai.Client(api_key=my_api_key)



# note generator
def note_generator(images):
    prompt = """Summarize the picture in note format in 50 works 
    and make sure to add  markdown in nesessary point"""

    response= client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[images,prompt]
    )

    return response.text


def audio_transcription(text):
    speech = gTTS(text,lang='en',slow=False)
    audio_buffer= io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer


def quiz_generator(image,difficulty):
    prompt = f"Generate 3 quizzes based on the {difficulty}"

    response= client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image,prompt]
    )

    return response.text

