#kviiri's awesome chitty chatty secret agent

import agent
import random
import time
import nltk
import string
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
		self.generate()
		time.sleep(1);
		
	def score(self, word):
		return 0               
		
	def generate(self):
		sent1 = random.choice(nltk.corpus.genesis.tagged_sents())
                sent2 = random.choice(nltk.corpus.genesis.tagged_sents())
                ret = ""
                for element in sent1:
                        if element[0] in string.punctuation:
                                ret = ret.strip()
                        opponent = random.choice(sent2)
                        if(element[1] != opponent[1]):
                                ret += element[0]
                        else:
                                ret += opponent[0]
                        ret += " "
		explanation = "I find the attribute spirituality to be as high as I prefer"
		self.propose(ret.strip(), explanation)
		
	def adapt(self, feedback):
		"""
		adapt implements a sample function which changes the self.generateVowel
		according to the feedback of other agents.
		"""
                return 0
