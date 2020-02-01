from Fighter import Fighter
import pygame as pg
import LinkedList as LL

def construct(inf):
    d = {}
    for line in open(inf):
        line = line.rstrip().split("\t")
        try:
            line[1] = int(line[1])
        except:
            line[1] = pg.image.load(line[1])
        finally:
            if isinstance(line[1], int):
                d[line[0]] = line[1]
            else if line[0][:3] == "walk":
                node = d[line[0]]


    #return Fighter(d["hp"], d["walk"], d[])