from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main timer page"""
    return render_template('index.html')

if __name__ == '__main__':
    # Debug mode is enabled for Phase 1 development
    # TODO: Disable debug mode in production deployment
    app.run(debug=True, host='0.0.0.0', port=5000)