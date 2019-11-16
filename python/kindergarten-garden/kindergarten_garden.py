from itertools import zip_longest


class Garden(object):
    def __init__(self, diagram, students=None):
        self.kids = ['Alice', 'Bob', 'Charlie', 'David',
                     'Eve', 'Fred', 'Ginny', 'Harriet',
                     'Ileana', 'Joseph', 'Kincaid', 'Larry']
        self.plant_names_dict = {'R': 'Radishes',
                                 'C': 'Clover',
                                 'G': 'Grass',
                                 'V': 'Violets'}

        # Students
        self.students = students

        self.fill_diagram(diagram)

    # def grouper(self, n, iterarable, fillvalue=None):
    #     args = [iter(iterarable)] * n
    #     return zip_longest

    def fill_diagram(self, diagram):
        self.row1, self.row2 = diagram.split('\n')

        # TODO: Tem que criar o dicionario intercalando 2 elementos de cada lista
        self.diagram_tmp = [
            [x for x in self.row1],
            [x for x in self.row2]
        ]

        self.diagram = []
        for row in self.diagram_tmp:
            for char in row:
                self.diagram.append(char)
        return self.diagram

    def plants(self, name):
        # Cria Dicionario com as criancas e as plantas
        self.plants = {}
        for kid in self.kids:
            # Adiciona os 4 primeiros indices da lista de plantas
            self.plants.update({kid: [plant for index, plant in enumerate(self.diagram) if index < 4]})

            # Apaga as plantas que ja foram adicionados
            self.diagram = [plant for index, plant in enumerate(self.diagram) if index >= 4]

        # Faz o Switch das plantas pelos nomes extensos
        for key, value in self.plants.items():
            for index, planta in enumerate(value):
                value[index] = self.plant_names_dict[planta]

        return list(self.plants[f'{name}'])


# TODO: garden.plants("Alice"), ["Radishes", "Clover", "Grass", "Grass"]


if __name__ == '__main__':
    # pass
    # garden = Garden("RC\nGG")  # Alice - Ok
    garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")  # Alice - ['Violets', 'Radishes', 'Violets', 'Radishes']
    # garden = Garden("VC\nRC")  # Alice - diferent

    # print(garden.kids)
    # print(garden.diagram)
    # print('--')
    # print(garden.plants)
    # print('--')
    print(garden.plants('Alice'))
