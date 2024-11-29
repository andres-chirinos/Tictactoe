import argparse
import Estadistica

class EstadisticaCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Aplicación de estadísticas.')
        self.parser.add_argument('--media', nargs='+', type=int, help='Calcula la media de una lista de números.')
        self.args = self.parser.parse_args()

    def run(self):
        if self.args.media:
            print(Estadistica.funcion_media(self.args.media))

if __name__ == "__main__":
    cli = EstadisticaCLI()
    cli.run()
