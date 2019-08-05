import requests, json, sys


NUMBER_OF_POSTS = 5


def parse_reddit(reddit_url, number):
    themes_and_rating = dict()
    response = requests.get(reddit_url + '/.json', headers = {'User-agent': 'Mozilla/5.0'})
    json_obj = json.loads(response.text)
    posts = json_obj['data']['children']
    for post in posts:
        themes_and_rating[post['data']['ups']] = post['data']['title']

    print(f'Best {NUMBER_OF_POSTS} posts are:\n')
    i = 0
    for rating in sorted(themes_and_rating, reverse=True):
        i += 1
        print(f'{i}: {themes_and_rating[rating]} (with rating: {rating})')
        
        if i == NUMBER_OF_POSTS:
            break


if __name__ == '__main__':
    try:
        parse_reddit(sys.argv[1], NUMBER_OF_POSTS)
    except:
        sys.exit(f'Wrong command line argument. Usage: python {sys.argv[0]} reddit_url_to_parse')
