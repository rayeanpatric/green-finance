from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Directory to save uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # Load your data here
    # For demonstration, let's create some dummy data
    companies = [
        {"Project Name": "Project A", "Investment Amount": 100000, "ROI": 10, "ESG Score": 75, "Risk Status": "Low", "Project Duration": "12 months"},
        {"Project Name": "Project B", "Investment Amount": 200000, "ROI": 15, "ESG Score": 80, "Risk Status": "Medium", "Project Duration": "24 months"},
        {"Project Name": "Project C", "Investment Amount": 150000, "ROI": 12, "ESG Score": 70, "Risk Status": "High", "Project Duration": "18 months"},
        {"Project Name": "Project D", "Investment Amount": 250000, "ROI": 20, "ESG Score": 85, "Risk Status": "Low", "Project Duration": "36 months"},
        {"Project Name": "Project E", "Investment Amount": 300000, "ROI": 25, "ESG Score": 90, "Risk Status": "Medium", "Project Duration": "30 months"},
        {"Project Name": "Project F", "Investment Amount": 120000, "ROI": 8, "ESG Score": 65, "Risk Status": "High", "Project Duration": "15 months"},
        {"Project Name": "Project G", "Investment Amount": 180000, "ROI": 18, "ESG Score": 78, "Risk Status": "Low", "Project Duration": "20 months"},
        {"Project Name": "Project H", "Investment Amount": 220000, "ROI": 22, "ESG Score": 82, "Risk Status": "Medium", "Project Duration": "28 months"},
        {"Project Name": "Project I", "Investment Amount": 160000, "ROI": 14, "ESG Score": 72, "Risk Status": "High", "Project Duration": "16 months"},
        {"Project Name": "Project J", "Investment Amount": 190000, "ROI": 19, "ESG Score": 88, "Risk Status": "Low", "Project Duration": "22 months"},
    ]
    
    # Prepare data for graphs (dummy data)
    investment_data = {
        'data': [{
            'x': [project['Project Name'] for project in companies],
            'y': [project['Investment Amount'] for project in companies],
            'type': 'bar',
            'name': 'Investment Amount'
        }],
        'layout': {
            'title': 'Investment Amount by Project'
        }
    }
    
    roi_data = {
        'data': [{
            'x': [project['Project Name'] for project in companies],
            'y': [project['ROI'] for project in companies],
            'type': 'bar',
            'name': 'ROI'
        }],
        'layout': {
            'title': 'ROI by Project'
        }
    }
    
    esg_data = {
        'data': [{
            'x': [project['Project Name'] for project in companies],
            'y': [project['ESG Score'] for project in companies],
            'type': 'bar',
            'name': 'ESG Score'
        }],
        'layout': {
            'title': 'ESG Score by Project'
        }
    }

    return render_template('dashboard.html', companies=companies, investment_data=investment_data, roi_data=roi_data, esg_data=esg_data)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file.filename.endswith('.pdf'):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            flash('File successfully uploaded')
            return redirect(url_for('dashboard'))
        else:
            flash('Only PDF files are allowed')
            return redirect(request.url)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)