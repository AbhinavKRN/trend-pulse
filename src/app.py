from flask import Flask, render_template, jsonify
from database.db_manager import DatabaseManager
from scraper.selenium_scraper import TwitterScraper
import traceback
from datetime import datetime

app = Flask(__name__)
db_manager = DatabaseManager()
scraper = TwitterScraper()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/scrape')
def scrape_trends():
    """Endpoint to trigger trend scraping."""
    try:
        trends, ip_address = scraper.get_trending_topics()
        
        trend_id = db_manager.save_trends(trends, ip_address)
        
        saved_record = db_manager.get_trends_by_id(trend_id)
        
        if not saved_record:
            raise Exception("Failed to retrieve saved record")
        
        response_data = {
            'status': 'success',
            'data': {
                'trends': trends,
                'ip_address': ip_address,
                'id': trend_id,
                'timestamp': saved_record.get('timestamp', datetime.utcnow()).strftime('%Y-%m-%d %H:%M:%S UTC')
            }
        }
        return jsonify(response_data)

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)