import unittest

from DiGraph import DiGraph
from src.DiGraph import DiGraph
from src.Node import Node
from src.Edge import Edge
from src.GraphAlgo import GraphAlgo

class Testload(unittest.TestCase):

    def test1000_load(self):
     g_algo = GraphAlgo()
     file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\1000.json'
     g_algo.load_from_json(file)
     self.assertEqual(g_algo.load_from_json(file),True)

    def test1000_Save(self):
        g_algo = GraphAlgo()
        file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\1000.json'
        g_algo.load_from_json(file)
        self.assertEqual(g_algo.save_to_json("file.json"), True)

    def test1000_SP(self):
        g_algo = GraphAlgo()
        file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\1000.json'
        g_algo.load_from_json(file)
        x,y= g_algo.shortest_path(0,3)
        j = [0, 769, 631, 664, 585, 74, 549, 347, 768, 610, 236, 3]
        self.assertEqual(x, 688.7466378590042)
        self.assertEqual(y, j)


    def test1000_center(self):
            g_algo = GraphAlgo()
            file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\1000.json'
            g_algo.load_from_json(file)
            x, y = g_algo.centerPoint()
            j = 362
            self.assertEqual(x, j)
            self.assertEqual(y, 1185.9594924690523)

    def test1000_tsp(self):
            g_algo = GraphAlgo()
            file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\1000.json'
            g_algo.load_from_json(file)
            x, y = g_algo.TSP([0, 3, 5])
            j = [0, 769, 631, 664, 585, 74, 549, 347, 768, 610, 236, 3, 658, 452, 266, 335, 5]
            self.assertEqual(x, j)
            self.assertEqual(y,1253.9306479126972)

###################################10,000######################################
    def test10000_center(self):
            g_algo = GraphAlgo()
            file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\10000.json'
            g_algo.load_from_json(file)
            x, y = g_algo.centerPoint()
            j = 3846
            self.assertEqual(x, j)


    def test10000_tsp(self):
            g_algo = GraphAlgo()
            file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\10000.json'
            g_algo.load_from_json(file)
            x, y = g_algo.TSP([0, 3, 5])
            j = [0,3744,3730,5625, 7746,963,3979, 4619,5743, 9323, 5325, 7181, 9857, 8335, 3, 1291, 5293, 5]

            self.assertEqual(x, j)
            self.assertEqual(y,1938.5222406376129)

    def test1000_load(self):
     g_algo = GraphAlgo()
     file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\10000.json'
     g_algo.load_from_json(file)
     self.assertEqual(g_algo.load_from_json(file),True)



    def test1000_SP(self):
        g_algo = GraphAlgo()
        file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\10000.json'
        g_algo.load_from_json(file)
        x,y= g_algo.shortest_path(0,3)
        j = [0,3744,3730,5625,7746,963,3979,4619, 5743, 9323,5325, 7181,9857,8335,3]
        self.assertEqual(x,982.0577746186997)
        self.assertEqual(y, j)

# ####################################100,000######################################

    def test100000_tsp(self):
            g_algo = GraphAlgo()
            file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\100000.json'
            g_algo.load_from_json(file)
            x, y = g_algo.TSP([0, 3, 5])
            j =  [0, 59017, 44285,60998, 68736, 49460, 15153, 3, 53548, 83229, 87797, 83303, 64038, 27374, 77355, 43285, 79691, 5]
            self.assertEqual(x, j)
            self.assertEqual(y,892.9572316882791)

    def test10000_load(self):
     g_algo = GraphAlgo()
     file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\100000.json'
     g_algo.load_from_json(file)
     self.assertEqual(g_algo.load_from_json(file),True)



    def test100000_SP(self):
        g_algo = GraphAlgo()
        file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\100000.json'
        g_algo.load_from_json(file)
        x,y= g_algo.shortest_path(0,3)
        j = [0, 59017, 44285, 60998, 68736, 49460, 15153, 3]
        self.assertEqual(x,462.6082344635053)
        self.assertEqual(y, j)




