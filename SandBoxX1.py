# Importer la bibliothèque turtle
import turtle


# Fonction pour dessiner un triangle
def dessiner_triangle(taille, couleur):
    turtle.color(couleur)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(taille)
        turtle.left(120)
    turtle.end_fill()


# Fonction pour dessiner le sapin
def dessiner_sapin(taille):
    # Dessiner le tronc du sapin
    turtle.color("brown")
    turtle.begin_fill()
    turtle.forward(taille / 10)
    turtle.right(90)
    turtle.forward(taille)
    turtle.right(90)
    turtle.forward(taille / 10)
    turtle.right(90)
    turtle.forward(taille)
    turtle.end_fill()

    # Déplacer la tortue en haut du tronc
    turtle.up()
    turtle.forward(taille / 10)
    turtle.right(90)
    turtle.forward(taille / 2)
    turtle.left(90)

    # Dessiner les triangles pour les branches du sapin
    for i in range(2):
        dessiner_triangle(taille / 2, "darkgreen")
        turtle.right(120)
        dessiner_triangle(taille / 2, "darkgreen")
        turtle.up()
        turtle.forward(taille / 2)
        turtle.left(60)
        turtle.forward(taille / 2)
        turtle.right(60)

    # Dessiner le dernier triangle pour la cime du sapin
    dessiner_triangle(taille / 2, "darkgreen")


# Utiliser la fonction pour dessiner un sapin de taille 200
dessiner_sapin(200)


