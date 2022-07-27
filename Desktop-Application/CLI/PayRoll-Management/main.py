import PayRollSystem as prs
import Employee

#main method
def main():
	pay_roll_system = prs.PayRollSystem()
	
	n=int(input("Enter number of Employees : "))
	for i in range(n):

		print("Enter Employee " + str(i+1) + " Details :")
		salary = float(input("Salary : "))
		date_of_join = input('Date : ')
		name = input('Name : ')
		
		employee_obj = Employee.Employee(salary, date_of_join, name) #employee object 
		pay_roll_system.add_data(employee_obj) #add employee to hash function


	while(True):
		print("1 - PF contribution of employee till a month")
		print("2 - Total amount of tax paid by employee till a month")
		print("3 - Generate pay slip for a employee for a month")
		print("4 - Loss of pay for given employee for a month")
		print("5 - Total CTC")
		print("6 - Hike 10 percent for all employees")
		print("7 - Exit")

		ch = int(input())

		if(ch==1):
			emp_id = int(input("Enter empoyee id ? "))
			month = int(input("Month (in digits) ? "))

			emp_obj = pay_roll_system.get_employee(emp_id)		#retrieve employee object based on id
			pf = emp_obj.calc_provident_fund_contrib_till_month(month)
			print("PF contribution of the employee till", month, ":", pf)
		elif(ch==2):
			emp_id = int(input("Enter empoyee id ? "))
			month = int(input("Month (in digits) ? "))

			emp_obj = pay_roll_system.get_employee(emp_id)		#retrieve employee object based on id
			tax_paid = emp_obj.calc_tax_paid_till_month(month)
			print("Tax paid by the employee till", month, ":", tax_paid)
		elif(ch==3):
			emp_id = int(input("Enter empoyee id ? "))
			month = int(input("Month (in digits) ? "))

			emp_obj = pay_roll_system.get_employee(emp_id)		#retrieve employee object based on id
			emp_obj.generate_pay_slip(month)
		elif(ch==4):
			emp_id = int(input("Enter empoyee id ? "))
			month = int(input("Month (in digits) ? "))
			num_of_leaves = int(input("Enter number of days the employee availed leave"))

			emp_obj = pay_roll_system.get_employee(emp_id)		#retrieve employee object based on id
			emp_obj.avail_leave(num_of_leaves)

			emp_obj.calc_loss_of_pay(month)
			print("Loss of pay for this month :", emp_obj.get_loss_of_pay(month))
		elif(ch==5):
			print("Total CTC per month :",pay_roll_system.calc_total_CTC())
		elif(ch==6):
			print("Total CTC per month (prior Hike) :",pay_roll_system.calc_total_CTC())
			pay_roll_system.hike_for_employees()
			print("Total CTC per month (post Hike) :",pay_roll_system.calc_total_CTC())
		elif(ch==7):
			break
		else:
			print("Invalid Input")

main()