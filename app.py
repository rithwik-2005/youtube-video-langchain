import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


##streamlit app
st.title("Summarize Content from Youtube Or Website")
st.subheader("Enter the details below:")

#get the Groq API key and URL to be summarized
url_input=st.text_input("please enter URL",label_visibility="collapsed")
#gemma  model is created
llm = ChatGroq(model="llama-3.1-8b-instant")


#prompt_templete
prompt_template="""
Provide a summary of the following content:
Content:{text}
"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])

if st.button("Summarize the content from Youtube or website"):
    #Validate the url
    if not url_input.strip():
        st.error("Please enter the URL properly")

    elif not validators.url(url_input):
        st.error("Please enter the valid URL")
    else:
        try:
            with st.spinner("Processing..."):
            #loading the website or youtube
                if "youtube.com" in url_input or "youtu.be" in url_input:
                    loader=YoutubeLoader.from_youtube_url(
                        url_input,
                        add_video_info=True,#includes metadata like title,author, etc
                        #translation="en" #translate if transcript is in another language
                    )
                else:
                    headers = {
                        "User-Agent": (
                            "Mozilla/5.0 (Macintosh; Intel Mac OS X) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/58.0.3029.110 Safari/537.3"
                        )
                    }
                    loader=UnstructuredURLLoader(
                        urls=[url_input],
                        ssl_verify=True,
                        headers=headers
                    )
                docs=loader.load() #data is loaded 
                #chain for summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)
                st.success(output_summary)
        except Exception as e:
            st.error(f"An error occurred: {e}") 