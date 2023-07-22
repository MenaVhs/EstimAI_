from Conditions.conditions import distance_condition
from GenerateCSV.writeInCSV import import_distance_contition_to_CSV
from Conditions.timeCalculation import time_per_frame
import main

#
#
# def get_project_feature(joint: str, condition: float, unit: str, event_time: float):
#     return joint, condition, unit, event_time

joint = main.joint
condition = main.condition
unit = main.unit  # or m
event_time = main.event_time



##############################

list_ = []
elapsed_time = []
FPS = []
VIDEO = []
time_per_frame_ = []
NX = []
NY = []


class Coordenada:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


class Etiqueta:
    def __init__(self, nombre):
        self.coordenadas = []
        self.nombre = nombre

    def __str__(self):
        coordenadas_str = ', '.join(str(c) for c in self.coordenadas)
        return coordenadas_str


class Time:
    def __init__(self, time):
        self.time = time

    def __str__(self):
        return f'Tiempo recorrido {self.time}'


class Fps:
    def __init__(self, fps):
        self.fps = fps


def get_joints(frames, bodyparts, time, video, nx, ny):
    cols_frames = len(frames[0])
    elapsed_time.extend(time)
    VIDEO.append(video)
    NX.append(nx)
    NY.append(ny)

    for body in bodyparts:
        list_.append(Etiqueta(body))

    for i in range(len(frames)):
        xyz = Coordenada()

        count = 0
        count_etiqueta = 0
        for j in range(cols_frames):
            if count == 0:
                xyz.x = frames[i][j]
            if count == 1:
                xyz.y = frames[i][j]
            if count == 2:
                xyz.z = frames[i][j]
            count += 1

            if count > 2:
                count = 0
                list_[count_etiqueta].coordenadas.append(xyz)
                xyz = Coordenada()
                count_etiqueta += 1
    detect_joint(joint)


def detect_joint(name):
    for etiqueta in list_:
        if name == etiqueta.nombre:
            etiqueta
            split_xy(etiqueta)
            return etiqueta


def split_xy(tuples):
    import ast
    x = []
    y = []

    labels = str(tuples)
    labels = ast.literal_eval(labels)

    for coordinates in labels:
        for coordinate in range(len(coordinates)):
            if coordinate == 0:
                x.append(coordinates[coordinate])
            if coordinate == 1:
                y.append(coordinates[coordinate])

    calculate_distance(x, y)


def calculate_distance(x_, y_):
    convertion = convert_coordinates(x_, y_, unit, NX, NY)
    x = convertion[0]
    y = convertion[1]

    acumulated_distance = 0
    acumulated_distance_list = []
    distances = []

    for n in range(len(x)):
        if n + 1 < len(x):
            X = float(x[n + 1]) - float(x[n])
            Y = float(y[n + 1]) - float(y[n])
        distance = (X ** 2 + Y ** 2) ** 0.5
        distances.append(distance)
        acumulated_distance += distance
        acumulated_distance_list.append(acumulated_distance)

        times_per_frame = time_per_frame(distances, FPS)
    # print("x",x)
    # print("y", y)
    time_with_acumulated_distance_ = time_with_acumulated_distance(acumulated_distance_list, FPS)
    data = distance_condition(time_with_acumulated_distance_, x, y, times_per_frame, distances, event_time, condition,
                  FPS)
    import_distance_contition_to_CSV(data, unit, joint, event_time, condition, VIDEO[0], FPS[0], NY[0]) ########################  return to excel

def convert_coordinates(pixel_x, pixel_y, u, W, H):
    # Define the image resolution in pixels per unit
    w = W[0]
    h = H[0]

    resolution = 28  # Pixels per inch
    if u == "cm":
        resolution /= 2.54  # Pixels per centimeter
    elif u == "m":
        resolution /= 2.54 * 100  # Pixels per meter

    # Convert the pixels to the selected unit
    unit_x = [px / resolution for px in pixel_x]
    unit_y = [py / resolution for py in pixel_y]

    return unit_x, unit_y


def convert_to_time(duration: float, fps: int):
    FPS.append(fps)

    seg_per_frame = 1 / fps
    time_frames = []
    for i in range(1, int(duration) + 1):
        elapsed_seconds = i * seg_per_frame
        time_frames.append(elapsed_seconds)
    # print("desde convert to time: elapsed second", time_frames)
    return time_frames


def time_with_acumulated_distance(distances, FPS):
    fps = int(FPS[0])
    distance_time = []
    count = 0
    sec = 1

    for distance in distances:
        distance_time.append((sec, distance))
        count += 1
        if count >= fps:
            count = 0
            sec += 1
    # print(distance_time)
    return distance_time