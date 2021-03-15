# coding: utf-8
# Baptiste Feldmann
from plateforme_lidar import calculs
import argparse,time
import numpy as np
import importlib
importlib.reload(calculs)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Process some strings...')

    parser.add_argument('-dirpath', metavar='N', type=str)
    parser.add_argument('-root', metavar='N', type=str)
    parser.add_argument('-buffer',type=int)
    parser.add_argument('-cores',type=int)

    args=parser.parse_args()
    workspace=args.dirpath
    name=args.root
    buffer=bool(args.buffer)
    nbcores=args.cores
    calculs.ReverseTiling_mem(workspace,name,buffer,nbcores)
