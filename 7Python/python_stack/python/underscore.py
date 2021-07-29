class Underscore(object):
	def map(self, list, callback):
		new_list = []
		for i in list:
			new_list.append(callback(i))
		print (new_list)

	def reduce(self, list, callback):
		new_list = []
		total = 0
		for i in list: 
			new_list.append(callback(i))
		for j in new_list:
			total += j
		print (total)

	def find(self, list, callback):
		for i in range(0, len(list)): 
			if callback(list[i]) == True: 
				print (list[i])
				break
			else: 
				return False

	def filter(self, list, callback):
		result = []
		for i in range(0, len(list)): 
			if callback(list[i]) == True: 
				result.append(list[i])
		print (result)

	def reject(self, list, callback):
		result = []
		for i in range(0, len(list)): 
			if callback(list[i]) != True: 
				result.append(list[i])
		print (result)