### youtube-video-langchain
## Required Libraries
# We use several libraries for this project:

    1.validators: An external library (not inbuilt) that helps validate URLs. The version used is 0.281.1.
    2.youtube_transcript_api: Allows reading the entire transcript from a YouTube video URL.
    3.streamlit: For building the web application interface.
    4.langchain.prompts: To import the prompt template for summarization.
    5.langchain_grok: To import ChatGrok for communicating with LLM models.
    6.langchain.chains.summarize: To import load_summarize_chain for summarization techniques.
    7.langchain_community.document_loaders: To import document loaders such as YouTubeLoader and UnstructuredURLLoader for loading content from YouTube and websites.