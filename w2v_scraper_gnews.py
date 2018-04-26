import requests
import json


BASE_URL = "https://h2.rare-technologies.com/w2v/most_similar?positive%5B%5D="


class W2VGoogleNews(object):

	def get_all_similar(self, word):
		"""
			Get the most similar word from google news word2vec

			params:
			....word : word that needed to be searched

			returns:
			....A list of list with [word, similarity] that is most similar to the word provided as string.
		"""

		response = json.loads(requests.get(BASE_URL + word).text)
		
		similars = response['similars']
		words = []

		for item in similars:
			words.append(item)

		print(words)

		return words


	def get_similar_with_threshold(self, word, threshold = 0.75):
		"""
			Get the most similar words above a threshold value

			params:
			....word : word that needs to be searched
			....threshold : thershold to get most similar words <Default value : 0.75>

			returns:
			....A list of list with [word, similarity] that is most similar to the word provided as string.
		"""

		response = json.loads(requests.get(BASE_URL + word).text)

		similars = response['similars']
		words = []

		for item in similars:
			if item[1] >= threshold:
				words.append(item)

		print(words)

		return words


	def get_n_most_similar(self, word, n_items = 5):
		"""
			Get n number of similar items from the w2v similarity

			params:
			....word : word that needs to be searched
			....n_items : number of most similar words <Default value -- 5>

			returns:
			....A list of list with [word, similarity] that is most similar to the word provided as string.
		"""

		response = json.loads(requests.get(BASE_URL + word).text)

		similars = response['similars']
		words = []

		words = similars[:n_items]

		print(words)

		return words