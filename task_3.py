import pandas as pd


class MicroLib:
    """Micro library that allows users to work with notes about ukrainian films. Contain film_name, note, rating
    (rating - is 1 - 5 rating of the film) Micro lib contain the next funcitonality:
Read notes from .csv file
Add note to .csv file
Remove note from .csv file
Print notes to console
Get films with the highest rating
Get films with the lowest rating
Get average rating among all films"""
    def __init__(self):
        # initialize the MicroLib class
        self.path = ''
        self.df = None

    def connect(self, path):
        # Function that connects to existing library
        self.df = pd.read_csv(path)
        self.path = path
        return self.df

    def create_mockup(self, path):
        # function creates a new library
        movies = {
            'film_name': ['Dovbush', 'Rhino', 'Solovei'],
            'note': ['some notes', 'ukrainian film', "film about ukrainian language"],
            'rating': [4, 4, 5]
        }
        self.df = pd.DataFrame(movies)
        self.path = path + 'lib.csv'
        self.df.to_csv(self.path, index=False)
        return self.df

    def read_notes(self, film_name):
        # function read all notes and returns it in DataFrame
        return self.df[self.df['film_name'] == film_name]

    def add_notes(self, film_name, note, rating):
        # function add notes to lib
        if not isinstance(rating, int) and not (0 < rating <= 5):
            raise ValueError('Rating must be int between 1 and 5')
        df2 = pd.DataFrame({'film_name': [film_name],
                            'note': [note],
                            'rating': [rating]})
        self.df = pd.concat([self.df, df2], ignore_index=True, axis=0)
        self.df.to_csv(self.path, index=False)
        return self.df


    def print_notes(self):
        # function that prints out notes
        print(self.df)

    def remove_notes(self, film_name):
        # function for removing notes
        self.df.drop(self.df[self.df['film_name'] == film_name].index, inplace=True)

    def get_highest_rating(self):
        # function returns film with highest rating
        return self.df[self.df.rating == max(self.df.rating)]

    def get_lowest_rating(self):
        # function returns film with lowest rating
        return self.df[self.df.rating == min(self.df.rating)]

    def get_average_rating(self):
        # function returns average rating for all films in lib
        return self.df['rating'].mean()

if __name__ == '__main__':
    lib = MicroLib()  # create instance of MicroLib
    lib.create_mockup("")  # create mockup lib
    lib.connect('lib.csv')  # connect to lib
    print(lib.read_notes('Dovbush'))  # read notes from lib
    print('-----------')
    lib.print_notes()  # prints out notes
    print('-----------')
    lib.remove_notes('Rhino')  # remove notes
    lib.print_notes()  # to see that Rhino was deleted
    print('-----------')
    lib.add_notes('Added film', 'added_notes', 3)  # Adding a new film
    lib.print_notes()  # to see that new film was added
    print('-----------')
    print(lib.get_highest_rating())  # film with highest rating
    print('-----------')
    print(lib.get_lowest_rating())  # film with lowest rating
    print('-----------')
    print(lib.get_average_rating())  #average film ratings
