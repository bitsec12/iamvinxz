class iamvinxz:
    def __init__(self):
        self.variables = {
            'name': 'Vincenzo Basile',
            'age': 33,
            'job': 'Developer',
            'languages': ('Italian', 'English')
        }

    def description(self):
        print('------iamvinxz------')
        for index, value in enumerate(self.variables.values()):
            if index == 0:
                print(f'Name: {value}')
            elif index == 1:
                print(f'Age: {value}')
            elif index == 2:
                print(f'Hobby: {value}')
            elif index == 3:
                print(f'Languages: {value}')

    def social_medias(self):
        platforms = {
            'Instagram': 'iamvinxz',
            'Telegram': 'iamvinxz',
            'LinkedIn': 'vincenzo-basile'
        }

        print('\n-----contact-----')
        for key, value in platforms.items():
            print(f'{key}: {value}')


if __name__ == '__main__':
    iamvinxz = iamvinxz()
    iamvinxz.description()
    iamvinxz.social_medias()
