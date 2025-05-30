# -*- coding: utf-8 -*-
"""6580043_mongo_lab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PBb9mMFM0hkFA5LAAXWIfpPwpDziAW9D
"""

!curl ipecho.net/plain
# Instaling PyMongo, this is the interface to connect to MongoDB with Python
! python -m pip install "pymongo[srv]"==3.11

! pip  install pymongo[srv,tls]
! pip install dnspython

from pymongo.mongo_client import MongoClient
#uri = "mongodb+srv://pakin-pan:<password>@cluster0.ac197n1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri= "mongodb+srv://pakin-pan:<password>@workshop-bakery.mxeepyw.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client.drop_database("Bakery")

#createDatabase && collections
BakeryDB = client.Bakery
BakeryDB.create_collection("cakes")

from bson import ObjectId #need to import this to set objectId in pymongo

#insert cake collections
cakes = BakeryDB.cakes
cakes.insert_one({
  "_id" : ObjectId("64759d513beb40594cb859e9"),
  "name": "Chocolate Cake",
  "shortDescription": "Chocolate cake is a cake flavored with melted chocolate, cocoa powder, or sometimes both.",
  "description": "Chocolate cake is made with chocolate; it can be made with other ingredients, as well. These ingredients include fudge, vanilla creme, and other sweeteners. The history of chocolate cake goes back to 1764, when Dr. James Baker discovered how to make chocolate by grinding cocoa beans between two massive circular millstones.",
  "image": "https://addapinch.com/wp-content/uploads/2020/04/chocolate-cake-DSC_1768.jpg",
  "ingredients": [
    "flour",
    "sugar",
    "cocoa powder"
  ],
  "recipe": "Preheat your oven to the specified temperature and prepare a greased cake pan. Mix the dry and wet ingredients separately, then combine and pour the batter into the pan. Bake for the recommended time, let it cool, and optionally frost or decorate as desired.",
  "stock": 25
})

cakes.insert_one({
  "_id": ObjectId("64759e4c3beb40594cb859ed"),
  "name": "Cheese Cake",
  "shortDescription": "Cheesecake is a sweet dessert consisting of one or more layers. The main, and thickest, layer consists of a mixture of a soft, fresh cheese (typically cottage cheese, cream cheese or ricotta), eggs, and sugar. ",
  "description": "Cheesecake is a sweet dessert consisting of one or more layers. The main, and thickest, layer consists of a mixture of a soft, fresh cheese (typically cottage cheese, cream cheese or ricotta), eggs, and sugar. If there is a bottom layer, it most often consists of a crust or base made from crushed cookies (or digestive biscuits), graham crackers, pastry, or sometimes sponge cake.[1] Cheesecake may be baked or unbaked (and is usually refrigerated).",
  "image":"https://sallysbakingaddiction.com/wp-content/uploads/2018/05/perfect-cheesecake-recipe.jpg",
  "ingredients": [ "graham cracker crumbs", "sugar", "eggs", "butter", "sour cream", "cream cheese", "vanilla extract" ],
  "recipe": "Mix graham cracker crumbs and melted butter for the crust. Press into a pan. Beat cream cheese, sugar, and vanilla. Fold in whipped cream. Pour over the crust. Refrigerate until set, remove from pan, and serve chilled with desired toppings.",
  "stock": 40
})

cakes.insert_one({
  "name": "Cupcake",
  "shortDescription":"Cupcakes are small, tasty snack cakes that are favored for their portability and portion-control. They are batter cakes baked in a cup-shaped foil or temperature resistant paper.1",
  "description":"Cupcake is a small cake designed to serve one person, which may be baked in a small thin paper or aluminum cup. As with larger cakes, frosting, icing and various other cake decorations such as fruit and candy may be applied. ",
  "image": "https://ichef.bbci.co.uk/food/ic/food_16x9_1600/recipes/cupcakes_93722_16x9.jpg",
  "ingredient":["butter","sugar","eggs","vanila extract","flour","milk","icing sugar","food colouring"],
  "recipe": "    Preheat the oven to 180C/350F/Gas 4 and line a 12-hole muffin tin with paper cupcake cases.Cream the butter and sugar together in a bowl until pale. Beat in the eggs a little at a time and stir in the vanilla extract.Fold in the flour using a large metal spoon, adding a little milk until the mixture is of a dropping consistency. Spoon the mixture into the cupcake cases until they are half full. Bake the cupcakes in the oven for 10-15 minutes, or until golden-brown on top and a skewer inserted into one of the cakes comes out clean. Set aside to cool for 5 minutes, then remove from the tin and cool on a wire rack. For the buttercream icing, beat the butter in a large bowl until soft. Add half the icing sugar and beat until smooth. Then add the remaining icing sugar with one tablespoon of the milk, adding more milk if necessary, until the mixture is smooth and creamy. Add the food colouring and mix until well combined. Spoon the icing into a piping bag with a star nozzle and pipe the icing using a spiralling motion onto the cupcakes in a large swirl.",
  "stock": 50
})

#create collection comments
comments = BakeryDB.create_collection("comments")

from datetime import datetime #for $date format

# add new comments
comments.insert_one({
"_id": ObjectId("6475be48a10dcef00d5c7d9c"),
"cakeId": ObjectId("64759d513beb40594cb859e9"),
"name": "Peter Quill",
"text": "This recipe was super easy to follow and the result was delicious!",
"date": datetime.fromtimestamp(1685750400000/1000)
})

#create index for comment collections
comments.create_index([("cakeId", 1)])
