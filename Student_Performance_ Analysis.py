import matplotlib.pyplot as plt 
class Student_Performance_Analysis:

    def __init__(self,hours,exam_marks):
        self.hours=hours
        self.exam_marks=exam_marks


    def main_code(self):
        try:
            plt.scatter(self.hours,self.exam_marks,marker='o',color='green',label="Record With Time & Result")
            plt.title("Analysis Student Performance With Time & Result")
            plt.xlabel("Hours Studied")
            plt.ylabel("Exam Result")
            plt.legend()
            plt.grid(True) 
            plt.xlim(1,10)
            plt.ylim(45,95)
            plt.show()

        except Exception as e:
            print(f"✖️Error : {e}")

hours_studied = [1,2,3,4,5,6,7,8,9,10]
exam_marks = [45,50,55,65,70,78,85,88,90,95]

analysis = Student_Performance_Analysis(hours_studied,exam_marks)
analysis.main_code()

