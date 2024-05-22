<h1>Instagram Images Crawler and Classifier</h1>
<p>This project is a Python-based application that allows users to crawl images from Instagram based on a given keyword, and then classify those images using a pre-trained machine learning model. It provides two endpoints: one for searching and crawling images from Instagram, and another for uploading images directly for classification.</p>

<h2>Features</h2>
<ul>
    <li>Image Crawling: The application can crawl up to 5 images from Instagram based on a specified keyword.</li>
    <li>Image Classification: It uses a pre-trained machine learning model to classify images into different categories.</li>
    <li>API Endpoints: Provides two API endpoints for searching and uploading images for classification.</li>
</ul>

<h2>Installation</h2>
<p>Clone the repository:</p>
<pre><code>
    git clone https://github.com/wasifali833/ig_images_crawler.git
</code></pre>
<p>Navigate to the project directory:</p>
<pre><code>
    cd IG_Images_Crawler
</code></pre>
<p>Install dependencies:</p>
<pre><code>
    pip install -r requirements.txt
</code></pre>

<h2>Usage</h2>
<p>Run the Flask application:</p>
<pre><code>
    python app.py
</code></pre>
<p>Access the API endpoints:</p>
<ul>
    <li><strong>Search Endpoint:</strong>
        <ul>
            <li>URL: /search</li>
            <li>Method: POST</li>
            <li>Request Payload: JSON object with the keyword (e.g., {"keyword": "nature"})</li>
            <li>Response: JSON object with analysis results for the crawled images.</li>
        </ul>
    </li>
    <li><strong>Upload Endpoint:</strong>
        <ul>
            <li>URL: /upload</li>
            <li>Method: POST</li>
            <li>Request Payload: Form-data with one or more image files to classify.</li>
            <li>Response: JSON object with analysis results for the uploaded images.</li>
        </ul>
    </li>
</ul>


<h2>Acknowledgements</h2>
<p>This project uses TensorFlow for image classification.</p>
<p>Image crawling is performed using requests.</p>
