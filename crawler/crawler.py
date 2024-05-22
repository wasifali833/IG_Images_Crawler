import requests

def crawl_instagram_images(keyword):
    """"Getting 5 images from Instagram API using requests and params"""
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.instagram.com/explore/tags/appletree/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.208", "Google Chrome";v="124.0.6367.208", "Not-A.Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"19.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-asbd-id': '129477',
        'x-csrftoken': 'K6mvcKqxSEhYRTtTYmiv_v',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'tag_name': str(keyword),
    }

    response = requests.get(
        'https://www.instagram.com/api/v1/tags/logged_out_web_info/',
        params=params,
        headers=headers,
    )

    #retrieving the images url's from the api response
    try:
        gridimages = response.json()['data']['hashtag']['edge_hashtag_to_top_posts']['edges']
        urls = [url['node']['display_url'] for url in gridimages[:5]]
    except Exception as e:
        urls = []
        print('Results not found as per your input')
    return urls