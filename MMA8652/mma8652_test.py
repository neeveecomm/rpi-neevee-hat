from mma8652 import MMA8652
sensor=MMA8652(1)
data=sensor.get3DValues()
print(f"Xaxis , Yaxis , Zaxis : {data[0]}, {data[1]}, {data[2]}")
print("sensor goes to standby mode")
sensor.setStandbyMode()
print(f"Xaxis : {sensor.getXValue()}")
print(f"Yaxis : {sensor.getYValue()}")
print(f"Zaxis : {sensor.getZValue()}")
print("sensor goes to active mode")
sensor.setActiveMode()
print(f"Xaxis , Yaxis , Zaxis : {data[0]}, {data[1]}, {data[2]}")
print(f"Manufacturer ID : {sensor.getManufacturerId()}")