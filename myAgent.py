#kviiri's awesome chitty chatty secret agent

import agent
import random
import time
from agent import Feedback

class AgentOfEntropy(agent.Agent):
	def __init__(self, name):
		# Anything you want to initialize
		
		agent.Agent.__init__(self, name)
		
	def lifeCycle(self):
		"""
		The function which is repeatedly started and defines the behaviour
		of the agent in the context of adaption, scoring and generating.
		"""
		r = random.random()
		feedback = Feedback("1", "62eb49e12fab557391bdd844a9efdd84", 'I didn\'t do it', "", 'This is the explanation by the creator', "", 0.5, 'I do not like the phrase "I didn\'t do it" by agent Smith because I find the attribute string length (teamname_agentasd) to be too high and I find the attribute string length (teamname_agentasd) to be too low')
		fr = self.parseFraming(feedback)
		self.callFunction("strLen", "Common sense is not so common")
		if r < 0.33:
			self.generate()
		if r > 0.33 and r < 0.66:
			## Gives the lists of lists, where each sublist is, ordered by timestamp desc:
			## [Word, Word], see documentation
			unratedwords = self.getUnscoredWords()
			if len(unratedwords) > 0:
				scr = self.score(unratedwords[0].word)
				framing = "This is not a nice word"
				self.sendFeedback(unratedwords[0].word_id, scr, framing, wordtext=unratedwords[0].word)
		elif r > 0.66:
			## The result is the following:
			## [Feedback, Feedback], see documentation
			feedback = self.getAllFeedback()
			self.adapt(feedback)
			
		#time.sleep(1)
		
	def score(self, word):
		"""
		score implements a sample function which gives a score to a word. In this case
		it the score is calculated such, that the word has a desired fraction of
		consonants and vowels.
		"""
                return 0
		
	def generate(self):
		"""
		generate implements a sample function which generates a word with random
		length. The system makes a distinction between consonants and vowels and generates
		words by using a self.generateVowel variable, which adapts to the feedback.
		"""
		word = ""
		wordstarts = [ "fee", "gar", "boo", "goo", "zor", "zie", "flu" ];
                wordends_soft = [ "ble", "blie", "flie", "bdy", "gdy", "gnay", "tam" ];
                wordends_hard = [ "st", "blut", "twip", "plup", "plop", "knip", "bup" ]; 

                firstsyllable = random.choice(wordstarts)
                word += firstsyllable + random.choice(wordends_soft) + ' ' + firstsyllable + random.choice(wordends_soft) + ' ' + random.choice(wordstarts) + random.choice(wordends_soft) + ' ' + random.choice(wordstarts) + random.choice(wordends_hard)
		explanation = "I find the attribute phrase vowels to be as high as I prefer"
		## If the word is ready, propose it to the server
		self.propose(word, explanation)
		
	def adapt(self, feedback):
		"""
		adapt implements a sample function which changes the self.generateVowel
		according to the feedback of other agents.
		"""
                return 0
