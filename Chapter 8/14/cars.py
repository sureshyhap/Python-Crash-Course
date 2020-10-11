def car_info(manufacturer, model, **extra_info):
    info = {
        "manufacturer" : manufacturer,
        "model" : model
        }
    for key, value in extra_info.items():
        info[key] = value
    return info

car = car_info("subaru", "outback", color="blue", tow_package=True)
print(car)
             
