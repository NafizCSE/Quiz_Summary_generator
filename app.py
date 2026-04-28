import streamlit as st
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image

st.title("Note Summary and Quiz Generator")
st.markdown("UPload upto 3 images to generate not summary")
st.divider()



with st.sidebar:
    st.header("Controls")


    ##img niye kaj korchi
    images = st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True

    )

    pil_images=[]

    for img in images:
          pil_img = Image.open(img)
          pil_images.append(pil_img)  


    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))

            

            for i ,img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    #difficulty
    Selected_option = st.selectbox(
        "Enter the difficulty of yorr quiz",
        ("Easy","Medium","Hard"),
        index = None
    )

    pressed = st.button("Click the button to initiate AI", type="primary")



if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not Selected_option:
        st.error("you must select difficulty")

    if images and Selected_option:
        #note
        with st.container(border=True):
            st.subheader("Your note")
             #the portion below will be replaced
            
            with st.spinner("AI is writing notes for you"):
             generated_notes=note_generator(pil_images)
             st.markdown(generated_notes)

#Audio trascript

        with st.container(border=True):
            st.subheader("Audio Transcription")
             #the portion below will be replaced
        
        with st.spinner("AI is writing notes for you"):
            audio_trascript= audio_transcription(generated_notes)
            st.audio(audio_trascript)


            #quiz

        with st.container(border=True):
            st.subheader(f"quiz ({Selected_option})")
             #the portion below will be replaced

        with st.spinner("AI is generating the quizzes"):

            quizzes = quiz_generator(pil_images,Selected_option)
            st.markdown(quizzes)