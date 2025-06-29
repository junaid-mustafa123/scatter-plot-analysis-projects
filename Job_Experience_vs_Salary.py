import matplotlib.pyplot as plt 
class Job_Experience_Vs_Salary:

    def __init__(self,exp,salary):
        self.exp=exp
        self.salary=salary


    def main_code(self):
        try:
            plt.scatter(self.exp,self.salary,marker='o',color="blue",label='Experience vs Salary')
            plt.title("**Job Experience vs Salary**")
            plt.xlabel("**year of experience**")
            plt.ylabel("**Monthly salary**")
            plt.legend()
            plt.grid(True)
            plt.xlim(0,9)
            plt.ylim(25000,90000)
            plt.show()
        except Exception as e:
            print(f"ERROR : {e}")    
        

exp  = [0,1,2,3,4,5,6,7,8,9]
monthly_salary = [25000,30000,35000,40000,45000,50000,60000,70000,80000,90000]


campare = Job_Experience_Vs_Salary(exp,monthly_salary)
campare.main_code()
