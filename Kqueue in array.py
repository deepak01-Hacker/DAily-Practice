class KQueues:
	def __init__(self, number_of_queues, array_length):
		self.number_of_queues = number_of_queues
		self.array_length = array_length
		self.array = [-1] * array_length
		self.front = [-1] * number_of_queues
		self.rear = [-1] * number_of_queues
		self.next_array = list(range(1, array_length))
		self.next_array.append(-1)
		self.free = 0
	
	def is_empty(self, queue_number):
		return True if self.front[queue_number] == -1 else False

	def is_full(self, queue_number):
		return True if self.free == -1 else False


	def enqueue(self, item, queue_number):
		if self.is_full(queue_number):
			print("Queue FULL")
			return
		next_free = self.next_array[self.free]
		if self.is_empty(queue_number):
			self.front[queue_number] = self.rear[queue_number] = self.free
		else:
			self.next_array[self.rear[queue_number]] = self.free
			self.rear[queue_number] = self.free
		self.next_array[self.free] = -1                                     
		self.array[self.free] = item
		self.free = next_free



	def dequeue(self, queue_number):
		if self.is_empty(queue_number):
			print("Queue EMPTY")
			return

		front_index = self.front[queue_number]
		self.front[queue_number] = self.next_array[front_index]
		self.next_array[front_index] = self.free
		self.free = front_index
		return self.array[front_index]
		
if __name__ == "__main__":
	ks = KQueues(3, 10) 
		
	ks.enqueue(15, 2) 
	ks.enqueue(45, 2)

	ks.enqueue(17, 1); 
	ks.enqueue(49, 1); 
	ks.enqueue(39, 1); 
		
	ks.enqueue(11, 0); 
	ks.enqueue(9, 0); 
	ks.enqueue(7, 0); 
		
	print("Dequeued element from queue 2 is {}".format(ks.dequeue(2)))
	print("Dequeued element from queue 1 is {}".format(ks.dequeue(1))) 
	print("Dequeued element from queue 0 is {}".format(ks.dequeue(0)))
