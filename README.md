
Flask Marshmallow Tutorial
Table of Contents
1. Intro to Flask-Marshmallow
2. Learning Objective
3. Assumptions
4. Installation / Setup
5. Hello World Application
6. Concepts of Flask-Marshmallow
a. Schemas

b. Deserializing

c. Serializing

7. Advanced Concepts
a. Validation

b. Nested Schemas

c. Custom Fields

8. Follow-ups & External Sources
a. Helpful links for more information

b. List of references

1. Intro to Flask-Marshmallow
"Flask-Marshmallow is a thin integration layer for Flask (a Python web framework) and marshmallow (an object serialization/deserialization library)

that adds additional features to marshmallow, including URL and Hyperlinks fields for HATEOAS-ready APIs.[...]" (readthedocs, 2023, 3)

This is a really good description of what Flask-Marshmallow is and what you can do with it. However there are many other ways of explaining this topic.
Another simpler explanation of Flask-Marshmallow is the following, describing the use of it in a different way.

"[Marshmallow] is used to convert objects to and from Python data types." (golinuxcloud, 2023)

Meaning for example converting an object into a string or vice versa. In other words you can deserialize a JSON object to Python object or serialize Python
object to JSON object.

As you can see there are different ways of explaining Flask-Marshmallow and describing what you can do with it. But just the theoretical part and looking at
the different definitions won't help us to understand Marshmallow completely so we will start to look into code snippets for each concept.

2. Learning Objective
In this tutorial we will focus on the serialization and deserialization as well as schemas and some other advanced concepts. First we will learn about
schemas, serialization and deserialization and then look at some examples to get a better understanding of how these functions work and what it
looks like using them.

So summing up this will be the content of this tutorial. Each of them will be explained with the help of code examples.

In-scope
Schemas
Serialization
Deserialization
Validation
Nested Schemas
Custom Fields
At the end of this tutorial you will understand each of these concepts and after some practice be able to use them correctly.

Out of scope
SQLAlchemy
Custom Fields using Functions
Even though we will not go into these concepts/ topics, there will be useful ressources linked at the end of this tutorial.

3. Assumptions
To be able to follow this tutorial you should already have:

python and Virtual Studio Code (VSCode) installed
set up a virtual environment (venv)
installed flask in your venv
If you haven't done these steps, there will be a short instruction on how to setup up a virtual environment in VSCode and install flask.
Once you've done all of these steps, we are ready to go and continue this tutorial.

4. Installation / Setup
In case you don't know how to setup a virtual environment and flask or just haven't done it yet, we will go through that very process step by step.
Otherwise you can skip the setup parts for virtual environment and flask and continue with the next steps concerning marshmallow.

Set up a virtual environment
The commands used in this tutorial are only for Windows. You can google the equivalent commands for MacOS
if needed.

The first thing you want to do after installing python and VSCode successfully is to open VSCode.
In the side pane you can see several symbols. Click on the "Extensions" button and search for Python.
You want to install the one created by Microsoft. Once you've done that, you can create a new folder
on your desktop for example. You can name it however you want but it might be best to give it a simple
name like App. In the next step you want to open your folder in VSCode. Do that by clicking
"file > open folder" and select your folder.

Before we continue using the VSCode terminal, we need to set the default terminal to cmd.
We can do that by pressing Ctrl + Shift + P and typing *terminal select default profile*.
Then you select Command Prompt. Now you want to create a new terminal by clicking
"terminal > new terminal" and type in:

python -m venv myvenv

By pressing Enter we create a new virtual environment in the folder "myvenv". Since that is the name
of the folder, you can give your folder a different name if you like. But for now lets continue with that.

Now we want to activate the virtual environment. We will do this by typing the following in the terminal:

.\myvenv\Scripts\activate.bat

You can check in the terminal if your virtual environment is activated or not. If the command worked and
successfully activated your virtual environment, you should see (myvenv) at the start of your terminal line.

Optional
If you plan on working more often on your project, it may be useful to consider setting your newly created
virtual environment as default for this project. To do this, press Ctrl+Shift+P and type in python
select interpreter. You will already see recommendations pop up. Now you want to click on the option that has
the name of your virtual environment in it ((myvenv) in this case).

You can now create a new terminal by clicking Terminal and New Terminal in the navigation bar of VSCode.
If it worked correctly the terminal line should start with (myvenv).

Install Flask
Still in the same terminal (starting with (myvenv)), you can now install flask by simply tiping the following

pip install flask

You should something happening in your terminal and after a few seconds flask is installed. If not sure
whether it is installed correctly or not, you may check your folder in the explorer. Your folder should
contain *flask. It may look something like this (It's only a screenshot of the top of the folder,
not showing jinja2* for example)

Screenshot of the folder!

Upgrade Flask
It may be useful to check if you have installed the newest version of Flask. If you want to upgrade Flask,
type this in your terminal line.

pip install --upgrade flask

Install Flask-Marshmallow
Similar to the previous step where we installed Flask, we now want to install Flask-Marshmallow by typing
one simple command as well.

pip install flask-marshmallow

It should only take a few seconds and it's done. Just as we did with Flask, we now want to check if it was
installed correctly. And your project folder should look something like this.

Another Screenshot of the folder!

Now you have finally completed all of the necessary installation and setup steps. Congratulations.

5. Hello World Application
Now that we have everything necessary set up and ready, we want to start by implementing a simple "Hello World" application.
In our case we want to provide a comparison between a "regular", simple "Hello World" application and another one using
Flask-Marshmallow. This will help get a better understanding about the code by shedding a light on the differences.
Enough of the theory so let's get into it.

Implementing a Hello World Application
A basic Hello World application is the firs step we will go through before doing anything else. It's
alway useful and recommended to write a Hello World application upfront. This is quite helpful to
get a first feeling and understanding for example for the programming language we want to learn or even if
we're just trying out a new environment we're not familiar with yet. The second benefit of a Hello World
application is, that we can check if everything works just fine, concerning e.g. the setup. When trying to run
a Hello World application and it turns out, that it's not working and/ or raising an error, we know
we have to check everything and make it work before we can start doing something more advanced.

So these are some reasons for starting with a Hello World application.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello, World!'

if __name__ == '__main__':
        app.run()
To run this application we simply type in:

flask run

Output
If we run this simple flask application we will get the ouput:

Hello, World!
Error
It may also occur that an error is raised while trying to run the application with flask run:

Screenshot of the error!

There are several ways of fixing this problem. One that works for windows is the following
line we type in the terminal command line:

set FLASK_APP = main. Py

If this Error still keeps coming up, there are some other solutions.

See also:
Fixing the error.

Implementing a Hello World Application with Flask-Marshmallow
As already mentioned before, the benefits from using a Hello World application also applies to
this example. We can see the differences between the two examples. This helps us understand how Marshmallow
is instantiated. In this example we define a message which is then returned with the help of JSON. It's a little
different from the first example (starting with the imports) however still very simple.

from flask import Flask, jsonify
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

@app.route('/')
def hello_world():
        message = {'message': 'Hello, World!'}
        return jsonify(message)

if __name__ == '__main__':
    app.run()
Output
Now running this application will give you a different output:

{"message": "Hello, World!"}
The same advise concerning errors applies to this example as well. When having trouble
using the flask run command, it might help take a look at the following.

See also
Fixing the error.

6. Concepts of Flask-Marshmallow
"The main component of Marshmallow is a Schema. A schema defines the rules that guides deserialization, called load,
and serialization, called dump. It allows us to define the fields that will be loaded or dumped, add requirements
on the fields, like validation or required.[...]" (kimsereylam.com, 2019)

Apart from the mentioned concepts such as loading, dumping and validation we will also take a look at nested schemas and custom
fields as well as SQLAlchemy. However, let's start with schemas.

Schemas
Intro to schemas
As already mentioned, a schema defines the structure of a Python object. Within a schema we can define fields
that can be serialized (dumped) or deserialized (loaded). Upfront it might be useful to have a little look at

At the use of schemas.

"

Validating input data Deserializing input data to app-level objects. Serializing app-level objects to primitive Python types. The serialized objects can then be rendered to
standard formats such as JSON [...]

" (readthedocs.io, 2023, 1)

The following code snippet shows an example of a schema:

Example
from marshmallow import Schema, fields

class MySchema(Schema): 
    firstname= fields.Str()
    lastname = fields.Str(required=True)
    age  = fields.Integer()
We can see that in our Schema "MySchema" we have two string fields "firstname" and "lastname" (which is required
to be able to successfully load the object) and one integer field "age". Now that we have defined the fields
our schema, we can use it to load and dump Python objects. However, we can define the fields even more, by passing parameters.
Therefore we have a list of parameters we can pass onto fields:

Parameters
"

only : a list of fields to only consider from dump and load
exclude : a list of fields to exclude from dump and load
many : whether the resulting schema is an array of the instantiated schema
context : a context object to provide contextual dump and load
load_only: a list of fields to be considered only during load
dump_only: a list of fields to be considered only during dump
partial : a list of fields that can be omitted (left out)
unknown : the behavior to take on unknown fields (EXCLUDE, INCLUDE, RAISE)
"(kimsereylam, 2019, 1)

With these paramaters we have the opportunity to specify what happens on load and dump to each field separately.
To help get a better understanding of these parameters we will take a look at a code snippet with an example schema.

from marshmallow import Schema, fields

class MySchema(Schema):
    firstname = fields.Str()                # adding field
    lastname  = fields.Str(required=True)   # adding field that is required
    age       = fields.Integer()            # adding field
    email     = fields.Str(required=True)   # adding field that is required

schema = MySchema(load_only=['firstname'], unknown='EXCLUDE', partial=['email']) # passing the parameters onto the fields
In this example we start by creating the schema as in the code snippet before. Additional to the fields we
have definded before we added "email" which is required. Now if we take a look at the last line, we can see
3 different parameters that were passed.

load_only: this parameter is passed onto "firstname". It's effect is that on dump, the firstname is excluded.


unknown: with this parameter every unknown field is excluded on dump and load.

partial: this parameter means that "email" can be left out but if it's given/ provided can't be None.
Now that we understand what these parameters do, we can take a look at what it looks like to load and dump this schema.

See also
If you want to learn more about schemas, go check the Extending Schemas.

Deserializing
After looking at schemas and mentioning deserializing and serializing we schoul look into these concepts
as well. The deserialization is also known as load. It's the reverse method of serialization and converts
JSON objects to Python objects (application-level data structure). We will take a look at an example
where we use deserialization. This refers to the schemas example code snippet we just talked through.
Let's get right into it:

schema = MySchema(load_only=['firstname'], unknown='EXCLUDE', partial=['email']) # last line from the schema we created

# if we deserialize this schema it would look something like this

data = schema.load(dict(firstname='Flo', lastname='Präger', age='21', something='some info'))

# loading that would mean this --> data = {"firstname": "Flo", "lastname":"Präger", "age":"21"} 
# the field "something" is excluded beacause it's unknown
We already know the first line from the schema code snippet before. In there we have passed parameters to
each field. These will later define the output we will get on load. To deserialize objects we use schema.load(dict()).

The loading concept "deserializes an input dictionary to application-level data structure." (readthedocs.io, 2023, 1)

On load we will get the firstname, because it's load_olny, the lastname and age. We don't have an email
input. Furthermore we have some unknown input that is not shown because we passed the EXCLUDE parameter.
That is everything we need to know about this code snippet in order to understand what happens on load.

Serializing
We already mentionend serializing and we know it's also known as dumping. What this concept actually
does, is to convert a Python object to a JSON object so it can be used in a web API. We will go through an
example of serialization so we can get a better understanding of it and how it works. The example
will be appropriate to the code snippet used in the Schemas chapter. Let's take a look:

schema = MySchema(load_only=['firstname'], unknown='EXCLUDE', partial=['email']) # last line from the schema we created before

# if we deserialize this schema it would look something like this

data = schema.load(dict(firstname='Flo', lastname='Präger', age='21', something='some info'))

# loading that would mean this --> data = {"firstname": "Flo", "lastname":"Präger", "age":"21"} 
# the field "something" is excluded beacause it's unknown

result = schema.dump(data)

# the result would be the following --> result = {"lastname":"Präger", "age":"21"} 
# "something" is still excluded and "firstname" is only included on load
We recognize the first line as being the last from the example before. Now the data line
is the one we just saw in the deserialization chapter. What really happens on dump is defined
in the first line with parameters. To dump data we just use schema.dump(data). The ouput is
explained in the comments below that line. So on load and dump, the output depends on the on
the parameters passed upfront.

7. Advanced Concepts
Intro to Advanced Concepts
Now that we looked into these three concepts, how they work and what they look like in a code snippet, we will
with some more advanced concepts, such as validation, nested schemas, custom fields and SQLAlchemy. Similar to
the first three concepts, we will go through each concept theoretically as well as practically by looking into
some code snippets again.

We will start by looking at the validation concept of Flask-Marshmallow.

Validation
Intro to validation
The validation of data is an important aspect in applications. It's the process of creating criteria
for data and checking if the input data meets all of the criteria that was defined upfront. A simple
example for validation is to check whether a field in a schema is empty or not. If the field isn't
empty, we can check whether it has the right data type or not.

Important: The validation process only happens on deserialization, therefore doesn't on serialization.

Now that we understand what validation is, we want to know how it's done. Therefore we will take a look
at validators. There are many validators that can be defined for fields. However we have differ. We will
see what that means in the following code snippet:

Example
from marshmallow import Schema, fields, validate

class NewSchema(Schema):
    password = fields.Str(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=25))
    age = fields.Integer(validate=validate.Range(min=16, max=100))
    email = fields.Email()
In this code snippet we can see that we created a schema, that has 3 fields. Now we have 2 types of validators.
The first (Let's call it type 1) is the defintion of the data type the input has to be. Meaning that the password
has to be a String to be valid data. The age has to be an Integer to be valid. The email has a built-in validation, so we don't have
to add validators. These are also known a the classes or types for defining fields. The second (type 2) type is the validation
through a validate argument, such as Length and Range.If the input doesn't match the requested type,
it will raise an ValidationError. Let's try it out.

from marshmallow import ValidationError, Schema, fields, validate

class NewSchema(Schema):
    password = fields.Str(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=25))
    age = fields.Integer(validate=validate.Range(min=16, max=100))
    email = fields.Email()

try:
    result = NewSchema().load({"name":"Flo", "email":"abc", "age":"21"})
except ValidationError as error:
    print(error.messages) # It will print the error message because abc ist not a valid email
    print(error.valid_data) # It will print the name because it is valid data
Output
Running this code snippet will give us the following output:

{'email': ['Not a valid email address.'], 'password': ['Missing data for required field.']} {'age': 21, 'name': 'Flo'}
As you an see, "abc" is not a valid email adress, password is missing input to be printed out. The only valid output
are age and name, because only these two meet the validation criteria.

Now that we have seen how the validation works, we should take a look at the most important types/ validators that exist.

Field Types/ Classes
Dict
String/ Str
Number
Integer/ Int
Decimal
Boolean/ Bool
Float
Time
Date
URL
Email
Nested
Field Validators
Email
Length
Range
URL
We can see that there are quite a lot options for validation in Flask-Marshmallow. And we didn't even
go through every option of validation. For example it is also possible to validate through a validation
function or defining a validation method.

See also:
Validation more in depth

Validation as methods and functions

Nested Schemas
Intro to Nested Schemas
We already learned what schemas are and what use they have. However we can also nest schemas in
another schema and field. This is useful if we have larger and complex data structures. It's also useful
to represent relationships between two or more objects. For example a movie has a director or
a book has an author. We will have a look at a code snippet to be able to understand what we
just learned.

Example
from marshmallow import Schema, fields
from pprint import pprint

class DirectorSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


class MovieSchema(Schema):
    title = fields.Str()
    director = fields.Nested(DirectorSchema)

data = {
    "title": "Interstellar",
    "director": {
        "name": "Christopher Nolan" ", "
        "email" " " "Christopher@Nolan.us" ", "
        "created_at" " " "06.11.2014"
    }
}

result = MovieSchema().load(data)
pprint(result)
Output
The output for this code snippet will be this:

{'director': {'name': 'Christopher Nolan, email Christopher@Nolan.us, ' 'created_at 06.11.2014'}, 'title': 'Interstellar'}
We now have successfully created a nested schema. The output shows us, that it worked. The title from the
MovieSchema as well as the DirectorSchema was printed out after deserializing the data. This is just a
simple example of what we can do with nested schemas. We can also define specifically which fields we want to nest
and some more functions like nesting a schema within itself. For this you can look at the See also section.

See also
Here you can find out more about nested schemas.

Custom Fields
Intro to Custom Fields
Custon Fields are user-defined fields, meaning that we can create our fields individually. Similar to the
concept of validation in Flask-Marshmallow, we have three different ways to create a custom field
as well. We can either:

Create a custom field as a class,
Use a method to create a custom field or
Use a function to create a custom field (out of scope)
We will start by looking at creating a custom field class.

Creating a Custom Field Class
To create a custom field class, we are going to subclass the fields.Field class. Furthermore we need to
implement the serializing and deserializing methods. Let's see what it looks like
in a code snippet:

from marshmallow import schema, fields, ValidationError

class EmailField(fields.Field):
    
    def _serialize(self, value, attr, obj):
        if value is None:
            return ""
        return value.lower() # before serializing the email adress we want it converted into lowercase letters
    
    def _deserialize(self, value, attr, data):
        if "@" not in value:
            raise ValueError("Email adress is not valid. Please try again.")
        return value
    
# Now we need to create a schema to use the EmailField in it.

class UserSchema(Schema):
    name = fields.Str()
    email = EmailField(required=True)
    created_at = fields.DateTime()
Now if we would start to serialize or deserialize data with the UserSchema, the custom field EmailField
will take care of the validation of email adresses and the conversion from upper case to lowercase. And with that,
we created our first custom field class.

Create a Custom Field Method
If we want to create a custom field using a method, the code will look a little different then before, creating a class.
The benefit of these custom fields is that we can define and create them however we like. To create a custom field using
using a method we have to use fields.Method. Let's take a look at the following example.

from marshmallow import fields, Schema

class MySchema(Schema):
    name = fields.Str(required=True)
    age = fields.Integer(required=True)
    is_adult = fields.Method("check_age") # we can name our Method whatever we want it to be called.

    def check_age(self, obj): # the method must have an obj parameter, which is then serialized.
        return obj.age >= 18 # check whether age is over 17 or not (True | False).
And with that we created our custom field using a method. The method is checking the integer input
whether it's greater than 17 or less than 18. In other words, it's checking if you're an adult or
a minor. In the is_adult line we instantiate our method and call it "check_age". Then below that
we define our method and returning the object, which can be "True" or "False". That's how an example
of creating a custom field using a method looks like. Although doing said thing using a function is
out of scope, you can still check the link to find out more about that.

See also
Click here to find out more

8. Follow-Ups & External Sources
Because of the fact that we have didn't cover all of the concepts of Flask-Marshmallow to the full extend,
we have to at least recommend some useful ressources that will help get into this topic more in depth.

Helpful Links to Follow-Up With
If you're interested in the Integraton of SQLAlchemy, then you should take look at this.
Another good ressource, if you want to go deeper into the Custom Fields topic.
List of References
Due to the length of the list of ressources, they will be saved and listed in a seperate document.
