class TrafficLight:
    __color = {'Красный': 4, 'Желтый': 2, 'Зеленый': 3}

    def running(self):
        colors = list(TrafficLight.__color.keys())
        for i in range(3):
            color = colors[i]
            time = TrafficLight.__color[color]
            print(f'{color} {time} сек.')
        return ''


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
