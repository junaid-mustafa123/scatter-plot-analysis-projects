import matplotlib.pyplot as plt 

class Car_Mileage_vs_Speed:
     

    def __init__(self,speed,mileage):
          self.speed=speed
          self.mileage=mileage

    def main_function(self):
        try:
            plt.scatter(self.speed,self.mileage,marker='o',color='red',label='SPEED VS MILEAGE')
            plt.title("Campare Car Speed With fuel efficiency")
            plt.xlabel("Car Speed (km/h)")
            plt.ylabel("Mileage (km/l)")
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
             print(f"ERROR : {e}")    

               

car_Speed = [20,30,40,50,60,70,80,90,100,110]
mileage = [10,12,15,17,18,17,15,13,10,8]


campare = Car_Mileage_vs_Speed(car_Speed,mileage)
campare.main_function()


        