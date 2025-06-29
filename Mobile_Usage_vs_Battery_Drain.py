"""
### 📱 3. **Mobile Usage vs Battery Drain**

**Goal:** Understand how usage time affects battery percentage.
**X-axis:** Mobile screen time (hours)
**Y-axis:** Battery percentage dropped
**Use:** Check which apps or durations drain battery most.
"""
### 📱 3. **Mobile Usage vs Battery Drain**
import matplotlib.pyplot as plt 
class Usage_vs_Battery:
    def __init__(self,usage,battery):
        self.usage=usage
        self.battery=battery

    def main_code(self):
        try:
            plt.scatter(self.usage,self.battery,marker='o',color='purple',label="Usage Vs Battery")  
            plt.title("**Mobile Usage vs Battery Drain**")  
            plt.xlabel("**Mobile Screen Time **")
            plt.ylabel("**Battery Percentage Dropped **")
            plt.legend()
            plt.grid(True)
            plt.xlim(0.5,5)
            plt.ylim(5,65)

            plt.show()

        except Exception as e:
            print(f"Error : {e}")

        

        
         


usage_time = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
batter_draiy = [5,10,17,22,30,37,45,52,58,65]



analysis=Usage_vs_Battery(usage_time,batter_draiy)
analysis.main_code()
