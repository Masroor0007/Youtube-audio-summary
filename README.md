# Youtube-audio-summary
Generating audio summaries of youtube videos
**README - Remember Web App**

**Overview:**
The "Audio summary" web app is a powerful tool that allows users to analyze YouTube video comments for sentiment and generate audio summaries of video content. The app provides valuable insights into audience sentiment, video statistics, and a condensed version of the audio content. This README provides essential information to set up, use, and understand the "Remember" web app.

**Features:**
- Sentiment Analysis: Analyze sentiment in YouTube video comments and visualize sentiment distribution using bar and pie charts.
- Video Statistics: Display video statistics such as views, likes, and comments, along with channel information.
- Audio Summarization: Generate a summarized version of the video's audio content using speech recognition and natural language processing techniques.

**Installation:**
1. Clone the repository to your local machine.
2. Install the required dependencies:
   - Flask (for the Flask web app): `pip install Flask`
   - transformers, huggingsound, pytube, pandas, plotly, nltk, and colorama (for summarizer.py): `pip install transformers huggingsound pytube pandas plotly nltk colorama`
   - ffmpeg (for converting video audio to WAV): Refer to the official ffmpeg documentation for installation instructions.

**Usage:**
1. Open a terminal and navigate to the project directory.
2. Run the flask-web-app:
   ```
   python app.py
   ```
3. The Flask web app will be opened, showing an HTML form where you can input the YouTube video URL for audio summarization.
4. After submitting the form, the app will generate an audio summary of the video content and display it on the "summary.html" page.

**Important Notes:**
- Ensure that you have a valid YouTube API key. Replace the `DEVELOPER_KEY` in `YoutubeCommentScrapper.py` with your API key.
- The Flask web app relies on a pre-trained speech recognition model. Make sure to have a compatible device (CPU or GPU) and the required libraries for the model to work properly.


**Credits:**
The "Remember" web app was modified by [Syed Masroor Ul Hasan]. It utilizes various open-source libraries and APIs, including Streamlit, Flask, transformers, huggingsound, pytube, pandas, plotly, nltk, and more.

**Contact:**
If you have any questions or need support, you can reach out to [syedmasroorulhasan2020@gmail.com].

**Acknowledgments:**
We extend our gratitude to the developers of Streamlit, Flask, HuggingFace, and other libraries used in this project. Their efforts make web app development and natural language processing tasks more accessible and efficient.
