import Employee

def hash_function(n):
	#hash function n%10
	return (n%10)

#class PayRollSystem
class PayRollSystem:
	def __init__(self):#initializer
		self.table = [None]*10	#hashtable is implemented by list
		self.count = len(self.table)	#count of data

	def add_data(self, obj):
		#add object to the hash table
		self.table[hash_function(obj.get_id())] = obj

	def calc_total_CTC(self):
		#calculate total cost to the company
		total_CTC = 0
		for i in range(self.count):

			if(self.table[i] == None): #if no data in the ith index of hash table, skip
				continue

			total_CTC += self.table[i].get_salary()
		return total_CTC

	def get_employee(self, id):
		#getter to return employee object based on employee id
		return (self.table[hash_function(id)])

	def hike_for_employees(self):
		#apply hike to all employees
		for i in range(self.count):
			if(self.table[i] == None): #if no data in the ith index of hash table, skip
				continue
			employee_obj = self.get_employee(self.table[i].get_id())
			employee_obj.hike_salary()