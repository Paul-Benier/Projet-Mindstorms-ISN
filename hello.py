#!/usr/bin/env python3
from ev3dev.ev3 import *    #Module permettant d'interagir avec le robot
import sys    #Module permettant d'arrêter le programme en cours d'éxecution

############################################################################
############################################################################
                                        #Partie de PAUL#
############################################################################
############################################################################

#Fonctions donnant les instructions à suivre pour écrire chaque caractères#
# Lettres A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

def A(m,my1,my2,mc,sens):		# Lettre A
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    for loop in range (2):# Trait vertical du bas à gauche à en haut au milieu
        m.run_to_rel_pos(position_sp=90, speed_sp=30, stop_action="hold")
		# Puis trait vertical du haut au milieu à en bas à droite
        my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
        my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
        my1.wait_while('running')
        sens=-1
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
		# Départ au milieu gauche sur le trait gauche de la lettre A
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=90, stop_action="hold")
    my1.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du milieu gauche sur le trait gauche de la lettre A
    sens=1
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')	# au milieu à droite sur le trait droit de la lettre A
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    m.run_to_rel_pos(position_sp=45*sens, speed_sp=30, stop_action="hold")
	# Position de fin : en bas à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def B(m,my1,my2,mc,sens):	# Lettre B

    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
	# Poser le crayon
    mc.wait_while('running')
	# Trait du bas à gauche à en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

	# Trait horizontal du haut à gauche à en haut à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
    # Trait oblique du haut à 1/4 du bord droit à la droite à 1/4 du bord haut
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical de la droite à 1/4 du bord haut à la droite à 1/4 du milieu
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de la droite à 1/4 du milieu à au milieu à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait horizontal au milieu à 1/4 du bord droit à au milieu à gauche
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
    sens=1
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

	# Position au milieu à gauche à au milieu à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique de la droite à 1/4 du milieu à au milieu à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical du milieu à 1/4 du bord droit à la droite à 1/4 du bord bas
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de la droite à 1/4 du bas à en bas à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait horizontal en bas à 1/4 du bord droit à en bas à gauche
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=1# Position de fin : en bas à droite
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def C(m,my1,my2,mc,sens):# Lettre C
	# Position en haut à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=60, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1						   # Trait du haut à droite à en haut à gauche
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait du haut à gauche à en bas à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    sens=1						# Trait du bas à gauche à en bas à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def D(m,my1,my2,mc,sens):# Lettre D
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du bas à gauche à en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait horizontal du haut à gauche à en haut à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait oblique du haut à 1/4 du bord droit à la droite à 1/4 du bord haut
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical de la droite à 1/4 du bord haut à la droite à 1/4 du bas
    my1.run_to_rel_pos(position_sp=270*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=270*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de la droite à 1/4 du bas à au bas à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait horizontal du bas à 1/4 du bord droit à en bas à gauche
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=1 # Position de fin : en bas à droite
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def E(m,my1,my2,mc,sens):# Lettre E

    F(m,my1,my2,mc,sens)# Lettre F		# Départ en bas à droite

    sens=-1					        			# Position en bas à gauche
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=1# Trait du bas à gauche à en bas à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def F(m,my1,my2,mc,sens):# Lettre F
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du bas à gauche à en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait du haut à gauche à en haut à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1# Position au milieu à gauche
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=1# Trait du milieu à gauche à au centre
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position de fin : en bas à droite
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def G(m,my1,my2,mc,sens):# Lettre G

    C(m,my1,my2,mc,sens)    # Lettre C		# Départ en bas à droite
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du bas à droite à droite à milieu
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    sens=-1							     # Trait de droite au milieu à au centre
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position de fin : en bas à droite
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    sens=1
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def H(m,my1,my2,mc,sens):	# Lettre H
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du bas à gauche à en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1	    								# Position au milieu à gauche
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=1# Trait du milieu à gauche à au milieu à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en haut à droite
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1# Trait du haut à droite à en bas à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def I(m,my1,my2,mc,sens):# Lettre I
	# Position en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du haut à gauche à en haut à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position au milieu en haut
    sens=-1
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du milieu en haut à milieu en bas
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position au milieu en haut
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du bas à gauche à en bas à droite
    sens=1
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def J(m,my1,my2,mc,sens):# Lettre J
	# Position en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du haut à gauche à en haut à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en haut au milieu
    sens=-1
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du haut au milieu à en bas au milieu
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait du bas au milieu à en bas à gauche
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait du bas à gauche à la gauche à 1/8 du bas
    sens=1
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Positionn de fin : en bas à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')


def K(m,my1,my2,mc,sens):# Lettre K
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du bas à gauche à en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en haut à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1
    for loop in range(2):
    	m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    	sens=-1					# Puis trait du milieu à gauche à en bas à droite
    	my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    	my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    	my1.wait_while('running')
    	sens=1
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def L(m,my1,my2,mc,sens):# Lettre L

    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du haut à gauche à en bas à gauche
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    sens=1# Trait du bas à gauche à en bas à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def M(m,my1,my2,mc,sens):# Lettre M
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait vertical du bas à gauche à en haut à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique du haut à gauche à au milieu à 1/4 du haut
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
    sens=1
	# Trait oblique du milieu à 1/4 du haut à en haut à droite
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
    sens=-1
	# Trait vertical du haut à droite à en bas à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def N(m,my1,my2,mc,sens):# Lettre N
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait vertical du bas à gauche à en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique du haut à gauche à en bas à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=60, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
    sens=1
	# Trait vertical du bas à droite à en haut à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position de fin : en bas à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def O(m,my1,my2,mc,sens):# Lettre O

    m.run_to_rel_pos(position_sp=45*sens, speed_sp=15, stop_action="hold")
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du haut à 1/4 du bord gauche à en haut à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait oblique du haut à 1/4 du bord droit à la droite à 1/8 du bord haut
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical de la droite à 1/8 du bord haut à la gauche à 1/8 du bord du bas
    my1.run_to_rel_pos(position_sp=270*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=270*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique du bas à 1/8 du bord bas à en bas à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait horizontal du bas à 1/4 du bord droit à en bas à 1/4 du bord gauche
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait oblique du bas à 1/4 du bord gauche à la gauche à 1/8 du bord bas
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical de la gauche à 1/8 du bord bas à la gauche à 1/8 du bord du haut
    my1.run_to_rel_pos(position_sp=270*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=270*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de la gauche à 1/8 du bord du haut à en haut à 1/4 du bord gauche
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position de fin : en bas à droite
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=115, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def P(m,my1,my2,mc,sens):# Lettre P
	# Position en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du haut à gauche à en haut à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait oblique du haut à 1/4 du bord droit à la droite à 1/4 du bord haut
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')

    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de la droite à 1/4 du milieu à au milieu à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')

    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en haut à gauche
    my1.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait vertical du haut à gauche à en bas à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position de fin : en bas à gauche
    m.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def Q(m,my1,my2,mc,sens):# Lettre Q

    O(m,my1,my2,mc,sens)# Lettre O		# Départ en bas à droite

    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    sens=-1
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique du milieu à en bas à droite
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    sens=1
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def R(m,my1,my2,mc,sens):# Lettre R

    P(m,my1,my2,mc,sens)				# Lettre P		# Départ en bas à droite

    sens=-1									# Position au milieu à gauche
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    sens=1
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique du milieu gauche à en bas à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def S(m,my1,my2,mc,sens):# Lettre S
	# Position en haut à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=60, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
    sens=-1
	# Trait horizonntal du haut à droite à en haut à 1/4 de la gauche
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait oblique du haut à 1/4 de la gauche à gauche à 1/8 du haut
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical de la gauche à 1/8 du haut à gauche à 3/8 du haut
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de la gauche à 3/8 du haut au milieu à 1/4 de la gauche
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=1
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait horizonntal du milieu à 1/4 de la gauche à au milieu à 1/4 de la droite
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait oblique du milieu à 1/4 de la droite à la droite à 3/8 du bas
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait vertical de la droite à 3/8 du bas à la droite à 1/8 du bas
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de la droite à 1/8 du bas au bas à 1/4 de la droite
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait horizonntal du bas à 1/4 de la droite à bas à gauche
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=1			# Position de fin : en bas à droite
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def T(m,my1,my2,mc,sens):# Lettre T

    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
    sens=-1
	# Position en haut au milieu
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait vertical du milieu
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=1						# Position de fin : en bas à droite
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def U(m,my1,my2,mc,sens):# Lettre U
	# Position en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1	# Trait vertical du haut à gauche à la gauche à 1/8 du bord bas
    my1.run_to_rel_pos(position_sp=315*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=315*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de la gauche à 1/8 du bas à en bas à 1/4 de la gauche
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=1
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait horizontal du bas à gauche à en bas à droite
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait oblique du bas à 1/4 de la droite à droite à 1/8 du bas
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=1
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical de la droite à 1/8 du bas à en haut à droite
    my1.run_to_rel_pos(position_sp=315*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=315*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position de fin : en bas à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def V(m,my1,my2,mc,sens):# Lettre V

    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
    sens=-1
	# Trait oblique du haut à gauche à en bas au milieu
    m.run_to_rel_pos(position_sp=90, speed_sp=30, stop_action="hold")
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
    sens=1
	# Trait oblique du bas au milieu à en haut à droite
    m.run_to_rel_pos(position_sp=90, speed_sp=30, stop_action="hold")
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1# Position de fin : en bas à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def W(m,my1,my2,mc,sens):# Lettre W
	# Position en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
    sens=-1
	# Trait oblique du haut à gauche à au milieu bas gauche
    m.run_to_rel_pos(position_sp=45, speed_sp=15, stop_action="hold")
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
    sens=1

    for loop in range(2):		# Trait oblique du milieu bas gauche à au milieu
    	m.run_to_rel_pos(position_sp=45, speed_sp=15, stop_action="hold")
    	my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    	my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    	my1.wait_while('running')
    	sens=-1
    sens=1
	# Trait oblique du milieu bas droite à en haut à droite
    m.run_to_rel_pos(position_sp=45, speed_sp=15, stop_action="hold")
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position de fin : en bas à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def X(m,my1,my2,mc,sens):# Lettre X

    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique du haut à gauche à en bas à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=60, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
    sens=1
	# Position en haut à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
    sens=-1
	# Trait oblique du haut à droite à en bas à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du bas
    m.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def Y(m,my1,my2,mc,sens):# Lettre Y
	# Position en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique du haut à gauche au centre
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
    sens=1
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en haut à droite
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')
    sens=-1
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique du haut à droite au centre
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')
	# Trait vertical du milieu à en bas
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 30, stop_action='hold')
    mc.wait_while('running')
	# Position de fin : en bas à droite
    m.run_to_rel_pos(position_sp=90, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def Z(m,my1,my2,mc,sens):# Lettre Z
	# Position en haut à gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action='hold')
    mc.wait_while('running')
	# Trait horizontal du haut
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
    sens=-1
	# Trait oblique
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')
    sens=1
	# Trait horizontal du bas
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

# Chiffres 0 1 2 3 4 5 6 7 8 9

def Chiffre0(m,my1,my2,mc,sens):# Chiffre O
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    for loop in range(2):# Trait vertical du bas à gauche à en haut à gauche
    	my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    	my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    	my1.wait_while('running')
	# Trait horizontal du haut à gauche à en haut à droite
    	m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    	m.wait_while('running')
    	sens=-1
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position de fin : en bas à droite
    m.run_to_rel_pos(position_sp=180, speed_sp=115, stop_action="hold")
    m.wait_while('running')


def Chiffre1(m,my1,my2,mc,sens):# Chiffre 1
	# Position à la gauche à 1/4 du bord haut
    my1.run_to_rel_pos(position_sp=270*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=270*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique de la gauche à 1/4 du bord haut à en haut à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')

    sens=-1# Trait vertical du haut à droite à en bas à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def Chiffre2(m,my1,my2,mc,sens):	# Chiffre 2

    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    for loop in range (2):
    	m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    	m.wait_while('running')
	# Puis Trait horizontale du milieu à droite à au milieu à gauche
    	sens=-1
    	my1.run_to_rel_pos(position_sp=180*sens, speed_sp=60, stop_action="hold")
    	my2.run_to_rel_pos(position_sp=180*sens, speed_sp=60, stop_action="hold")
    	my1.wait_while('running')
	# Trait horizontale du bas à gauche à en bas à droite
    sens=1
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def Chiffre3(m,my1,my2,mc,sens):# Chiffre 3
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du bas à gauche à en bas à gauche
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical du bas à droite à en haut à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait horizontal du haut à droite à en haut à gauche
    sens=-1
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position au milieu à gauche
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    m.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def Chiffre4(m,my1,my2,mc,sens):# Chiffre 4

    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait vertical du haut à gauche à au milieu à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    sens=1
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en haut à droite
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait vertical du haut à droite à en bas à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def Chiffre5(m,my1,my2,mc,sens):  # Chiffre 5
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    for loop in range (2):
        m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
        m.wait_while('running')

        my1.run_to_rel_pos(position_sp=180, speed_sp=60, stop_action="hold")
        my2.run_to_rel_pos(position_sp=180, speed_sp=60, stop_action="hold")
        my1.wait_while('running')
        sens=-1
	# Trait horizontale du bas à gauche à en bas à droite
    sens=1
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def Chiffre6(m,my1,my2,mc,sens):        # Chiffre 6
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait vertical du bas à gauche à au milieu à gauche
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1# Position en bas à gauche
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    sens=1

    Chiffre5(m,my1,my2,mc,sens)  # Chiffre 5    # Départ en bas à droite


def Chiffre7(m,my1,my2,mc,sens):        # Chiffre 7

    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du haut à gauche à en haut à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical du haut à droite à en bas à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running') # Lettre P      # Départ en bas à droite


def Chiffre8(m,my1,my2,mc,sens):        # Chiffre 8

    Chiffre0(m,my1,my2,mc,sens) # Chiffre 0      # Départ en bas à droite

    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    sens=-1
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du milieu à gauche à au milieu à droite
    m.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def Chiffre9(m,my1,my2,mc,sens):        # Chiffre 9

    Chiffre5(m,my1,my2,mc,sens)   # Chiffre 5      # Départ en bas à droite
	# Position en haut à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait vertical du haut à droite à au milieu à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

# Caractères "espace" ? . : ! > < ( )
# Fonction permettant de faire un point
def PointBasique(mc):  # Départ et fin à l'endroit où la fonction est utilisée
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

# Fonction permettant de faire une virgule
def VirguleBasique(m,my1,my2,mc,sens):
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique du milieu en bas à plus bas à gauche
    sens=-1
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de plus bas à gauche à au milieu en bas
    sens=1
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')


def Espace(m):		   # Espace
	# Position en bas à gauche à en bas à droite
    m.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def PointInterro(m,my1,my2,mc,sens):    # Point d'interrogation ?
	# Position en haut à droite
    my1.run_to_rel_pos(position_sp=315*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=315*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique de la gauche à 1/8 du haut à en haut à 1/4 de la gauche
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait horizontal du haut à 1/4 de la gauche à en haut à 1/4 de la droite
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait oblique du haut à 1/4 de la droite à la droite à 1/8 du bord haut
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait vertical de la droite à 1/8 du bord haut à la droite à 3/8 du haut
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique de la droite à 3/8 du haut à au milieu à 3/8 du bord bas
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait vertical du milieu à 3/8 du bord bas à au milieu à 1/8 du bord bas
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas au milieu
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    PointBasique(mc)  # Fonction permettant de faire un point

    m.run_to_rel_pos(position_sp=90, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def Point(m,mc,sens):		        # Point .

    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')

    PointBasique(mc)# Fonction permettant de faire un point
	# Position en bas à droite
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def DeuxPoints(m,my1,my2,mc,sens):	# Point .
	# Position en bas au milieu
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')

    PointBasique(mc) # Fonction permettant de faire un point
	# Position au milieu à 1/4 du bord bas
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    PointBasique(mc) # Fonction permettant de faire un point

    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def PointExcla(m,my1,my2,mc,sens):	# Point d'exclamation !

    m.run_to_rel_pos(position_sp=90*sens, speed_sp=60, stop_action="hold")
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait du haut au milieu à au milieu à 1/8 du bord bas
    sens=-1
    my1.run_to_rel_pos(position_sp=315*sens, speed_sp=100, stop_action="hold")
    my2.run_to_rel_pos(position_sp=315*sens, speed_sp=100, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas au milieu
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=40, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=40, stop_action="hold")
    my1.wait_while('running')

    PointBasique(mc) # Fonction permettant de faire un point

    m.run_to_rel_pos(position_sp=90, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def Superieur(m,my1,my2,mc,sens):	# Supérieur à >

    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    for loop in range (2):
        m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
        sens=-1
        my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
        my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
        m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    m.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def Inferieur(m,my1,my2,mc,sens):	# Supérieur à <
	# Position en haut à droite
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=60, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=60, stop_action="hold")
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    for loop in range (2):
        m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
        sens=-1
        my1.run_to_rel_pos(position_sp=-180, speed_sp=120, stop_action="hold")
        my2.run_to_rel_pos(position_sp=-180, speed_sp=120, stop_action="hold")
        m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    m.run_to_rel_pos(position_sp=180, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def ParentheseGauche(m,my1,my2,mc,sens): # Parenthèse gauche (
	# Position en haut à 1/4 du bord droit
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=60, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=60, stop_action="hold")
    m.run_to_rel_pos(position_sp=135*sens, speed_sp=90, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique du haut à 1/4 du bord droit à au milieu à 1/8 du bord haut
    sens=-1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')
	# Trait vertical du milieu à 1/4 du bord gauche et à 3/8
	#du bord haut au milieu à 1/4 du bord gauche et à 3/8 du bord bas
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique du milieu à 1/4 du bord gauche et à 3/8 du bord bas
	#à au milieu à 1/8 du bord bas
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45, speed_sp=60, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique du milieu à 1/8 du bord bas en bas à 1/4 du bord droit
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    m.run_to_rel_pos(position_sp=45, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def ParentheseDroite(m,my1,my2,mc,sens): # Parenthèse droite )
	# Position en haut à 1/4 du bord gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=15, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')

    sens=-1
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45, speed_sp=60, stop_action="hold")
    my1.wait_while('running')

    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=60, stop_action="hold")
    my1.wait_while('running')
	# Trait oblique du milieu à 1/8 du bord bas en bas à 1/4 du bord gauche
    my1.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=45*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    m.run_to_rel_pos(position_sp=135, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def CrochetGauche(m,my1,my2,mc,sens): 	# Crochet gauche [
	# Position en haut à 1/4 du bord droit
    sens=-1
    my1.run_to_rel_pos(position_sp=360, speed_sp=60, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360, speed_sp=60, stop_action="hold")
    m.run_to_rel_pos(position_sp=135, speed_sp=90, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du haut à 1/4 du bord droit à en haut à 1/4 du bord gauche
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical du haut à 1/4 du bord gauche à en bas à 1/4 du bord gauche
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait horizontal du bas à 1/4 du bord gauche à en bas à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=90, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    m.run_to_rel_pos(position_sp=45, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def CrochetDroit(m,my1,my2,mc,sens): 	# Crochet droit ]
	# Position en haut à 1/4 du bord gauche
    sens=-1
    my1.run_to_rel_pos(position_sp=360, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360, speed_sp=120, stop_action="hold")
    m.run_to_rel_pos(position_sp=90, speed_sp=30, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du haut à 1/4 du bord gauche à en haut à 1/4 du bord droit
    m.run_to_rel_pos(position_sp=90, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Trait vertical du haut à 1/4 du bord droit à en bas à 1/4 du bord droit
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Trait horizontal du bas à 1/4 du bord droit à en bas à 1/4 du bord gauche
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    m.run_to_rel_pos(position_sp=135, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def Virgule(m,my1,my2,mc,sens):		# Virgule ,
	# Position en bas au milieu
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')

    VirguleBasique(m,my1,my2,mc,sens)# Fonction permettant de faire une virgule

    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')


def PointVirgule(m,my1,my2,mc,sens):	# Point virgule ;
	# Position en bas au milieu
    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')

    VirguleBasique(m,my1,my2,mc,sens) # Fonction permettant de faire une virgule

    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

    PointBasique(mc) # Fonction permettant de faire un point

    m.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    sens=-1
    my1.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=90*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def Tiret(m,my1,my2,mc,sens):		# Tiret -

    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait horizontal du milieu à gauche eu milieu à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    m.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait vertical du milieu à droite à en bas à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=180*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')


def Slash(m,my1,my2,mc,sens):		# Slash /
	# Poser le crayon
    mc.run_to_rel_pos(position_sp=10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Trait oblique du bas à gauche à en haut à droite
    m.run_to_rel_pos(position_sp=180*sens, speed_sp=60, stop_action="hold")
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
	# Lever le crayon
    mc.run_to_rel_pos(position_sp=-10, speed_sp= 15, stop_action= 'hold')
    mc.wait_while('running')
	# Position en bas à droite
    sens=-1
    my1.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=360*sens, speed_sp=120, stop_action="hold")
    my1.wait_while('running')

##############################################################################
##############################################################################
                                        #Partie de LOAN LESEC#
##############################################################################
##############################################################################

#Cette fonction a pour mission d'effectuer un repérage pour savoir s'il y a assez de place pour le prochain mot à écrire
def sensor(ts,m,my1,my2, listeelement, compteurcaractere):

    avancement = 0 #variable qui enregistre le nombre de degrés réalisé par le robot
    while not ts.value():   #tant que le bouton est pas pressé il tourne en boucle
	#fait tourner le moteur x de 5°
        m.run_to_rel_pos(position_sp=5, speed_sp=350, stop_action="hold")
        avancement += 5  #ajoute 5° à la variable


	#fait revenir à la position initiale le robot
    m.run_to_rel_pos(position_sp=-avancement, speed_sp=500, stop_action="hold")
    m.wait_while('running')

    nbrdispo = avancement/ 350 #permet de connaître le nombre de mots qui reste de disponible

    if nbrdispo >= len(listeelement):
        Sound.speak("No problem, I'm going to write").wait()  #fait parler le robot
        return compteurcaractere

    else:
        if compteurcaractere == 0: #si jamais le mot est trop long alors que le robot est sur le bord, le programme cesse
            Sound.speak("There is a problem, I can't write this word because I have not enoff space").wait()
            Sound.speak("Sorry").wait()
            sys.exit() #le programme s'arrête
        #La suite permet de sauter une ligne
        Sound.speak("There is a problem, I'm going to jump").wait()
        my1.run_to_rel_pos(position_sp=-500, speed_sp=120, stop_action="hold")	#saute une ligne
        my2.run_to_rel_pos(position_sp=-500, speed_sp=120, stop_action="hold")
        my1.wait_while('running')
		#fait revenir le robot tout à gauche
        m.run_to_rel_pos(position_sp=-compteurcaractere*270+150, speed_sp=900, stop_action="hold")
        m.wait_while('running')
        return 0




#Fonction de lancement du robot
def lancement(ts,m,my1,my2):
	#variable de type int enregistrant le nombre de caractère réalisés par le robot
    compteurcaractere = 0

    f= open('fichiercaracteres', 'r')  #ouvre le fichier
    contenuf = f.readline() #met le contenu dans une variable de type str
    listeelement = contenuf.split(' ') #forme une liste en séparant les éléments/mots

    for i in range(len(listeelement)):

        if compteurcaractere != 0:   #ajoute un espace entre chaque élément
            Espace(m)
            compteurcaractere +=1

        compteurcaractere = sensor(ts,m,my1,my2, listeelement[i], compteurcaractere)  #remettre après si besoin

		#chaque caractère de l'élément va être réalisé par le robot
        for loop in listeelement[i]:

            if loop == 'A':
                A(m,my1,my2,mc,sens)
            elif loop == 'B':
                B(m,my1,my2,mc,sens)
            elif loop == 'C':
                C(m,my1,my2,mc,sens)
            elif loop == 'D':
                D(m,my1,my2,mc,sens)
            elif loop == 'E':
                E(m,my1,my2,mc,sens)
            elif loop == 'F':
                F(m,my1,my2,mc,sens)
            elif loop == 'G':
                G(m,my1,my2,mc,sens)
            elif loop == 'H':
                H(m,my1,my2,mc,sens)
            elif loop == 'I':
                I(m,my1,my2,mc,sens)
            elif loop == 'J':
                J(m,my1,my2,mc,sens)
            elif loop == 'K':
                K(m,my1,my2,mc,sens)
            elif loop == 'L':
                L(m,my1,my2,mc,sens)
            elif loop == 'M':
                M(m,my1,my2,mc,sens)
            elif loop == 'N':
                N(m,my1,my2,mc,sens)
            elif loop == 'O':
                O(m,my1,my2,mc,sens)
            elif loop == 'P':
                P(m,my1,my2,mc,sens)
            elif loop == 'Q':
                Q(m,my1,my2,mc,sens)
            elif loop == 'R':
                R(m,my1,my2,mc,sens)
            elif loop == 'S':
                S(m,my1,my2,mc,sens)
            elif loop == 'T':
                T(m,my1,my2,mc,sens)
            elif loop == 'U':
                U(m,my1,my2,mc,sens)
            elif loop == 'V':
                V(m,my1,my2,mc,sens)
            elif loop == 'W':
                W(m,my1,my2,mc,sens)
            elif loop == 'X':
                X(m,my1,my2,mc,sens)
            elif loop == 'Y':
                Y(m,my1,my2,mc,sens)
            elif loop == 'Z':
                Z(m,my1,my2,mc,sens)
            elif loop =='0':
                Chiffre0(m,my1,my2,mc,sens)
            elif loop =='1':
                Chiffre1(m,my1,my2,mc,sens)
            elif loop == '2':
                Chiffre2(m,my1,my2,mc,sens)
            elif loop == '3':
                Chiffre3(m,my1,my2,mc,sens)
            elif loop == '4':
                Chiffre4(m,my1,my2,mc,sens)
            elif loop == '5':
                Chiffre5(m,my1,my2,mc,sens)
            elif loop == '6':
                Chiffre6(m,my1,my2,mc,sens)
            elif loop == '7':
                Chiffre7(m,my1,my2,mc,sens)
            elif loop == '8':
                Chiffre8(m,my1,my2,mc,sens)
            elif loop == '9':
                Chiffre9(m,my1,my2,mc,sens)
            elif loop == '>':
                Superieur(m,my1,my2,mc,sens)
            elif loop == '<':
                Inferieur(m,my1,my2,mc,sens)
            elif loop == '?':
                PointInterro(m,my1,my2,mc,sens)
            elif loop == '!':
                PointExcla(m,my1,my2,mc,sens)
            elif loop == ':':
                DeuxPoints(m,my1,my2,mc,sens)
            elif loop == '.':
                Point(m,mc,sens)
            elif loop == '(':
                ParentheseGauche(m,my1,my2,mc,sens)
            elif loop == ')':
                ParentheseDroite(m,my1,my2,mc,sens)
            elif loop == '[':
                CrochetGauche(m,my1,my2,mc,sens)
            elif loop == ']':
                CrochetDroit(m,my1,my2,mc,sens)
            elif loop == ',':
                Virgule(m,my1,my2,mc,sens)
            elif loop == ';':
                PointVirgule(m,my1,my2,mc,sens)
            elif loop == '-':
                Tiret(m,my1,my2,mc,sens)
            elif loop == '/':
                Slash(m,my1,my2,mc,sens)

            m.run_to_rel_pos(position_sp=90, speed_sp=200*0.3, stop_action="hold")
            m.wait_while('running')
            compteurcaractere +=1
	#fait revenir le robot tout a gauche
    m.run_to_rel_pos(position_sp=-compteurcaractere*270, speed_sp=120, stop_action="hold")
    m.wait_while('running')
    my1.run_to_rel_pos(position_sp=-1000, speed_sp=120, stop_action="hold")
    my2.run_to_rel_pos(position_sp=-1000, speed_sp=120, stop_action="hold")
    my1.wait_while('running')
    Sound.speak("Mission complete").wait()

############################################################
#Programme Principal#
############################################################

ts = TouchSensor ()     # Objet correspondant au capteur tactile
m = LargeMotor('outB')  # Objet correspondant au moteur de l'axe x
my1 = LargeMotor('outA')# Objet correspondant au 1er moteur de l'axe y
my2 = LargeMotor('outD')# Objet correspondant au 2ème moteur de l'axe y
mc = LargeMotor('outC') # Objet correspondant au moteur de l'axe du crayon
sens = 1                # Variable qui permet de changer le sens de rotation lors d'un moteur

lancement(ts,m,my1,my2)


