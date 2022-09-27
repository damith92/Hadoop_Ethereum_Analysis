from mrjob.job import MRJob
import re
import time
import os
import json

class Proj_Part_D_1_2(MRJob):

	categ_dict = {}
	status_dict = {}
	

	def mapper_init(self):
		# load scam data sets
		file_js = open("scams.json") 
		init_str = json.load(file_js)

		for each in init_str["result"]:

			categ_type = str(init_str["result"][each]["category"])
			status_type = str(init_str["result"][each]["status"])

			for each_1 in init_str["result"][each]["addresses"]:
				self.categ_dict[str(each_1)] = categ_type
				self.status_dict[str(each_1)] = status_type
				
			
	
	def mapper(self, _,line):
		fields = line.split(",")
		try:
			if len(fields) == 7:
				addr_to = str(fields[2])
				value = float(fields[3])
				

				if addr_to in self.categ_dict and addr_to in self.status_dict:
					yield ((self.status_dict[addr_to], self.categ_dict[addr_to]), value)
		except:
			pass

	def reducer(self,word,counts):

		yield(word,sum(counts))

	def combiner(self,word,counts):
	
		yield(word,sum(counts))





if __name__ == '__main__':

	Proj_Part_D_1_2.run()
