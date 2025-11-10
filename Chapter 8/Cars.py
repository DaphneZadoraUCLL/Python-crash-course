def car_directory(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


my_car = car_directory('subaru', 'outback', color='blue', tow_package=True)
print(my_car)
your_car = car_directory('audi', 'a4', color='black',
                         sunroof=True, navigation_system=True)
print(your_car)
