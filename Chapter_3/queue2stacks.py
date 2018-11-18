class Queue2Stacks(object):

	def __init__(self):

		# Two Stacks
		self.instack = []
		self.outstack = []

	def enqueue(self,element):

		self.instack.append(element)

	def dequeue(self):

		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())

		return self.outstack.pop()