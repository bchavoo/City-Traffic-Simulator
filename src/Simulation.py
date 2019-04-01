# Main driver that executes the program

from Map import Map
from Raw import Tiles, raw_map, Point, resource_path
from Car import Car
from CommandPallete import CommandPallete
from tkinter import Tk, Frame, Label, Button
from time import sleep
from PIL import Image, ImageTk

class Simulation(Tk):
    def __init__(self):
        super().__init__()
        self.title('Traffic Simulation')
        self.iconbitmap('C:\\Users\\vuong\\Documents\\CSCE\\cse361\\csce_361\\src\\data\\traffic.ico')
        self.create_widgets()
    
    def create_widgets(self):
        self.command = CommandPallete(self)
        self.traffic_map = Map(self)
        car_tmp = Car(Point(3, 4), Tiles.car_up, master=self.traffic_map.city)
        counter = 0
        while self.command._running is not True:
            self.command.update()
            self.update()
        while self.command._running is True:
            ## Hardcode optimal path for a car
            if counter == 60: car_tmp.turn_right()
            if counter == 180: car_tmp.turn_right()
            if counter == 360: car_tmp.turn_left()
            if counter == 810: car_tmp.turn_right()
            if counter == 960: car_tmp.turn_left()
            if counter == 1110: car_tmp.turn_right()
            if counter == 1140: 
                car_tmp.turn_left()
                car_tmp.stop()

            if counter % 150 == 0 and counter > 0:
                for car in self.traffic_map.get_cars():
                    car.turn_right()
            if self.command._ispause is not True:
                for car in self.traffic_map.get_cars():
                    for comp in car.get_component():
                        self.traffic_map.city.move(comp, car.dx, car.dy)
                    car.x += (car.dx / 30) 
                    car.y += (car.dy / 30)
                # Preprogrammed
                for comp_tmp in car_tmp.get_component():
                    self.traffic_map.city.move(comp_tmp, car_tmp.dx, car_tmp.dy)
                car_tmp.x += (car_tmp.dx / 30) 
                car_tmp.y += (car_tmp.dy / 30) 
                counter += 1
            sleep(0.01)
            
            self.command.update()
            self.traffic_map.update()
            self.update()


