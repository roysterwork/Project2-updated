
# Part 1.  import statements needed
import csv
from flask import Flask

#app = Flask(__name__)

# Commit to remote server - GitHub
# work in virtual enviornment

#Part 2.   open cleaned data set, movies_cleaned.csv
#cleaned_file = open('movies_cleaned.csv', 'r', newline = '')

with open('movies_cleaned.csv', 'r', encoding = 'utf8') as movies_file:
    movies_lines = list(csv.reader(movies_file, delimiter=','))
print(movies_lines[0])
print(movies_lines[1])

#Part 3.   In your movies_tools.py file, define a class Movie that accepts as constructor
#input one row of the movies_clean.csv file (in whatever format you think is appropriate for you).

class Movie:
    #unit_name = "currency" # class variable because it's true of ALL instances of this class (unless overridden in a subclass)
    #rate=1
    def __init__(self, row):
        self.row = row
        self.title= row[0]
        self.rating=row[6]

    def __str__(self):
        return "{} - {} <br/>".format(self.title,self.rating)



movie_1= Movie(movies_lines[1])
movie_2= Movie(movies_lines[2])
movie_3= Movie(movies_lines[3])
movie_4= Movie(movies_lines[4])
movie_5= Movie(movies_lines[5])
print("movie1 ", movie_1)
print('testing movie instance variables/r')
print(type(movie_1))
print(type(movie_1.__str__()))
print(movie_1.__str__() + movie_2.__str__() )
print(movie_1.title, movie_1.rating) ## here it is , do this 5 times for movies_lines[0] - movies_lines[4]
print(movie_2.row)
print(movie_3.row)
print(movie_4.row)
print(movie_5.row)

# count the number of movies here

movie_count= 0
for i in movies_lines:
    movie_count+=1

finalmoviecount=movie_count-1
print(finalmoviecount)
# for function create 5 instances of the class Movie
        #self.base_rate = 1 #always
# how is html interacting with python here? within this route?

# in the route you will define the path
# you will then define a (unique) function with a return value
# the return value will have the html tag, the defaut is a p tag,
# ex. "<h1> hello </h1>"

#Part 4.   cleate routes with functions

app = Flask(__name__)


@app.route('/')
def home():


    return  "<h1>"+ str(finalmoviecount) + " movies recorded" + "</h1>"

@app.route('/movies/ratings')
def ratings():

#CREATE 5 INSTANCES OF MOVIE
    movie_1= Movie(movies_lines[1]).__str__()
    movie_2= Movie(movies_lines[2]).__str__()
    movie_3= Movie(movies_lines[3]).__str__()
    movie_4= Movie(movies_lines[4]).__str__()
    movie_5= Movie(movies_lines[5]).__str__()

    return movie_1 + movie_2 + movie_3 + movie_4 + movie_5

    # .__str__()

# PUT INSTANCES IN DICTIONARY
    # movie_dic={}
    # movie_dic[0]=movie_1
    # movie_dic[1]=movie_2
    # movie_dic[2]=movie_3
    # movie_dic[3]=movie_4
    # movie_dic[4]=movie_5

    # movie_str=""
    # for i in range(5):
    #     movie_str + "{} | {}".format(movie_dic[i].row[0],movie_dic[i].row[3])
    #     print(movie_str)


    # print(movie_1.row) ## here it is , do this 5 times for movies_lines[0] - movies_lines[4]
    # print(movie_2.row)
    # print(movie_3.row)
    # print(movie_4.row)
    # print(movie_5.row[1])

    return "HI THIS IS A TEST"#STRING WITH HTML
           # with correcrt format to console - Movie Title | IMBD rating
           # use "{} | {}".format(vartittle, var_rating)

# print(movie_5.row[6])
#creating class strategie
    #fuction should iterate through first five rows and return a variable
    #that represents these rows

    #the route /movies/ratings/
        #should take variable and return each of them


if __name__ == "__main__": # Still only want the application to RUN if we are running this file specifically, and not using functions inside it as tools for something else
   app.run() # This is what causes an app to work at URLs that start with http://localhost:5000/ (AKA http://127.0.0.1:5000/, they mean the exact same thing) -- on your own computer -- when you run the program with "runserver" at the end, as directed. See HW 1!
