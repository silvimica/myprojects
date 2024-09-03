# app.py
from flask import Flask, request, render_template, send_file
from google_play_scraper import Sort, reviews_all
import pandas as pd
import numpy as np
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

reviews_df = None  # Make reviews_df global for CSV download

def extract_app_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('id', [None])[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    global reviews_df
    if request.method == 'POST':
        app_url = request.form.get('app_url')
        app_id = extract_app_id(app_url)

        if app_id:
            # Scrape reviews
            reviews = reviews_all(
                app_id,
                sleep_milliseconds=0,
                lang='ru',
                country='kz',
                sort=Sort.MOST_RELEVANT,
            )

            # Convert to DataFrame
            reviews_df = pd.DataFrame(np.array(reviews), columns=['review'])
            reviews_df = reviews_df.join(pd.DataFrame(reviews_df.pop('review').tolist()))

    return render_template('index.html', reviews=reviews_df)

@app.route('/download', methods=['GET'])
def download_csv():
    if reviews_df is not None:
        reviews_df.to_csv('reviews.csv', index=False)  # Save DataFrame to CSV file
        return send_file('reviews.csv', as_attachment=True)  # Send file as download
    else:
        return "No reviews available to download", 400

if __name__ == '__main__':
    app.run(debug=True)
