from flask import Flask, request, jsonify
from crawler.crawler import crawl_instagram_images
from classification_model.model import classify_image

app = Flask(__name__)

"""First Endpoint: which takes a keyword as input, crawl images based on keyword, classify them using ML model and
return the response """
@app.route('/search', methods=['POST'])
def search():
    keyword = request.json.get('keyword')
    if not keyword:
        return jsonify({'error': 'Please provide a keyword to search'}), 400
    
    keyword = keyword.replace(' ','').strip()
    # Crawling images using function from crawler.py file
    images = crawl_instagram_images(keyword)
    if images: 
        analysis_results = []
        # Loop through crawled images and perform analysis
        for image in images:  
            analysis = classify_image(image)  # Perform analysis using ML model
            analysis_results.append(analysis)
        return jsonify({'results': analysis_results})
    else:
        return jsonify({'error': 'Images not found as per your keyword'})

"""Second Endpoint: which takes image as an input, us ML model to classify it, then
return the response """
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    analysis = classify_image(image_file)
    return jsonify({'results': analysis})


if __name__ == '__main__':
    app.run(debug=True)
