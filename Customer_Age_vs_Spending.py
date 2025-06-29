"""
### 🛒 5. **Customer Age vs Spending**

| Customer Age | Amount Spent (PKR) |
| ------------ | ------------------ |
| 18           | 2000               |
| 22           | 3500               |
| 25           | 5000               |
| 30           | 6000               |
| 35           | 5800               |
| 40           | 5500               |
| 45           | 5200               |
| 50           | 5000               |
| 55           | 4800               |
| 60           | 4000               |
"""
# age = [18,22,25,30,35,40,45,50,55,60]
# amount = [2000,3500,5000,6000,5800,5500,5200,5000,4800,4000]

"""
### 🛒 5. **Customer Age vs Spending**

**Goal:** Compare age of customers to their average spending.
**X-axis:** Customer age
**Y-axis:** Amount spent in store
**Use:** Identify target age groups for marketing.
"""


import matplotlib.pyplot as plt


class Age_VS_Spending:

    def __init__(self,Customer_Age,Amount_Spent):
        self.customer_Age=Customer_Age
        self.Amount_Spent=Amount_Spent

    def main_code(self):
        try:
            plt.scatter(self.customer_Age,self.Amount_Spent,marker='o',color="red",label="Age vs Spending")
            plt.title("**Identify target age groups for marketing**")
            plt.xlabel("**Customer Age**")
            plt.ylabel("**Amount spent in store**")
            plt.xlim(18,60)
            plt.grid()
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"ERROR : {e}")



age = [18,22,25,30,35,40,45,50,55,60]
amount = [2000,3500,5000,6000,5800,5500,5200,5000,4800,4000]


analysis = Age_VS_Spending(age,amount)
analysis.main_code()

               


        