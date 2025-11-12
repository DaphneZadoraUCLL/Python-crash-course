from pathlib import Path

path_dogs = Path('dogs.txt')
path_cats = Path('cats.txt')

contents_dogs = "Berner Senner\n"
contents_dogs += "Jack Russel\n"
contents_dogs += "Beagle"
path_dogs.write_text(contents_dogs)

contents_cats = "Main Coon\n"
contents_cats += "Savanah\n"
contents_cats += "Bengal"
path_cats.write_text(contents_cats)
