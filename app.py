from flask import Flask, render_template, request, redirect, url_for
from summarizer import summarize_video

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        summarized_text = summarize_video(video_url)
        return render_template('summary.html', summary=summarized_text)
    return render_template('index.html')

@app.route('/back_to_home')
def back_to_home():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
