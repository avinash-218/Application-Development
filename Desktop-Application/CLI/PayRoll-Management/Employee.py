months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

#class Employee
class Employee:
	#static members
	num_leaves_per_annum = 12 #number of leaves per annum is 12
	Employee_id = 0 #employee id
	hike = 0.1

	def __init__(self, salary, date_of_join, name):#initializer
		#salary - salary of an employee in lakhs

		self.emp_id = Employee.Employee_id #employee id
		Employee.Employee_id+=1 #increment employee id

		self.date_of_join = date_of_join 	#employee's date of joining
		self.leaves_availed = 0 			#leaves availed is 0 by default
		self.name = name 					#employee's name
		self.salary = salary 				#salary of the employee
		self.basic_pay = 0.4*self.salary 	#basic pay of employee = 40% of salary
		self.provident_fund = 0.12*self.basic_pay 			#PF amount  per month = 12% of basic pay
		self.allowances = self.salary - (self.basic_pay+self.provident_fund)		#allowances = salary - (basic_pay+PF)
		self.tax_per_annum = self.calculate_annual_tax() 		#calculate tax per annum
		self.loss_of_pay = [0]*12			#loss of pay for each month
		#self.display_all()

	def display_all(self):
		print(self.emp_id, self.provident_fund)

	def get_id(self):
		#getter method for employee id
		return self.emp_id

	def get_salary(self):
		#getter method for employee salary
		return (self.salary)

	def calculate_annual_tax(self):
		#method to calculate annual tax for an employee
		annual_salary = self.salary*12
		if(annual_salary > 0 and annual_salary <200000): #0-2 lakhs
			self.tax = 0
		elif(annual_salary < 500000): 					#2-5 lakhs
			self.tax = 0.1*annual_salary
		elif(annual_salary < 800000): 					#5-8 lakhs
			self.tax = 0.2*annual_salaryy
		elif(annual_salary >=800000): 					#above 8 lakhs
			self.tax = 0.3*annual_salary

	def calc_provident_fund_contrib_till_month(self, month):
		#calculate PF contribution made till a month
		#month - month as integer

		return (month*self.provident_fund)

	def calc_tax_paid_till_month(self, month):
		#calculate tax paid till given month
		#month - month as integer

		monthly_tax_installment = self.tax / 12.0 #monthly tax installment
		return (month*monthly_tax_installment)

	def avail_leave(self, num_of_days):
		#avail leave
		#num_of_days - number of days to avail leave
		self.leaves_availed += num_of_days

	def calc_loss_of_pay(self, month):
		#calculate loss of pay due to availing additional leave
		#month - month as integer
		salary_per_day = self.salary / 30 #assuming month has 30 days

		if(self.leaves_availed > Employee.num_leaves_per_annum): #if leaves availed more than the eligibility
			self.loss_of_pay[month] = salary_per_day * (self.leaves_availed - Employee.num_leaves_per_annum)
			self.leaves_availed = Employee.num_leaves_per_annum #if pay lost due to additional leave, set back to initial

	def get_loss_of_pay(self, month):
		#getter to get loss of pay for a given month
		return (self.loss_of_pay[month])

	def calc_gross_salary(self, month):
		#calculate gross salary per month

		monthly_tax_installment = self.tax / 12.0 #monthly tax installment
		self.calc_loss_of_pay(month) #loss of pay due to extra availing of leave
		return (self.salary - monthly_tax_installment - self.loss_of_pay[month])


	def generate_pay_slip(self, month):
		#generate pay slip for an employee
		#month - month as integer

		print('ID :', self.emp_id)		#employee id 
		print('Name :', self.name)		#employee name
		print('Month :', months[month-1])	#month
		print('Basic Pay :', self.basic_pay)		#basic pay
		print('Allowances :', self.allowances)		#allowances
		print('PF Contribution :', self.provident_fund) #PF contribution
		print('Tax :', self.tax / 12.0)		#tax installment for this month
		print('Loss of Pay :', self.loss_of_pay[month])	#loss of pay for this month
		print('Gross Salary :',self.calc_gross_salary(month))	#gross salary

	def hike_salary(self):
		#hike salary by 10%
		self.salary += self.salary*Employee.hike
		#recalculate
		self.basic_pay = 0.4*self.salary 	#basic pay of employee = 40% of salary
		self.provident_fund = 0.12*self.basic_pay 			#PF amount  per month = 12% of basic pay
		self.allowances = self.salary - (self.basic_pay+self.provident_fund)		#allowances = salary - (basic_pay+PF)
		self.tax_per_annum = self.calculate_annual_tax() 		#calculate tax per annum