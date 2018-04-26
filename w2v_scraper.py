import requests
import json


BASE_URL = "https://api.explosion.ai/sense2vec/"

def getmostsimilar(word, sense, n_items = 10):
	"""
		Retrive most similar words with confidence of similarity

		params:
		....word : word that needed to be searched
		....sense : sence of the word to find similarity, for example -- NOUN    <NOTE: DO NOT USE 'AUTO' OR 'auto'>
		....n_items : number of most similar words <Default value -- 10>

		returns:
		....words: A list of tuples (text, confidence_score)
	"""

	response = get(word, sense)
	words = []

	for item in response['results'][:n_items]:
		words.append((item["text"], item["score"]))

	print(words)
	return words


def get_with_threshold(word, sense, threshold = 0.75):
	"""
		Retrive most similar words with confidence more than or equal to that of specified threshold

		params:
		....word : word that needed to be searched
		....sense : sence of the word to find similarity, for example -- NOUN    <NOTE: DO NOT USE 'AUTO' OR 'auto'>
		....threshold : thershold to get most similar words <Default value : 0.75>

		returns:
		....words: A list of tuples (text, confidence_score)
	"""

	response = get(word, sense)
	words = []

	for item in response['results']:
		if item['score'] >= threshold:
			words.append((item['text'], item['score']))

	print(words)
	return words


def get_all(word, sense):
	"""
		Retrive all possible similar words

		params:
		....word : word that needed to be searched
		....sense : sence of the word to find similarity, for example -- NOUN    <NOTE: DO NOT USE 'AUTO' OR 'auto'>

		returns:
		....words: A list of tuples (text, confidence_score)
	"""

	response = get(word, sense)
	words = []

	for item in response['results']:
		words.append((item['text'], item['score']))

	print(words)
	return words


def get(word, sense):
	"""
		Requests the explosion API server for word2vec similar words

		params:
		....word : word that needed to be searched
		....sense : sence of the word to find similarity, for example -- NOUN    <NOTE: DO NOT USE 'AUTO' OR 'auto'>

		returns:
		....A loaded json response object <type dict>
	"""

	APPEND_URL = word + "|" + sense
	REQUEST_URL = BASE_URL + APPEND_URL

	response = requests.get(REQUEST_URL)
	response = requests.get(REQUEST_URL)
	return json.loads(response.text)



get_with_threshold("Hello", "NOUN")
# get_most_similar_googlenews("hello")