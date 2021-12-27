import unittest

from DiGraph import DiGraph
from src.DiGraph import DiGraph
from src.Node import Node
from src.Edge import Edge
from src.GraphAlgo import GraphAlgo

class Testload(unittest.TestCase):

    def test_loadA0(self):
      g_algo = GraphAlgo()
      file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A0.json'
      g_algo.load_from_json(file)
      self.assertEqual(g_algo.load_from_json(file),True)

    def test_loadA1(self):
      g_algo1 = GraphAlgo()
      file1 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A1.json'
      g_algo1.load_from_json(file1)
      self.assertEqual(g_algo1.load_from_json(file1),True)


    def test_loadA2(self):
      g_algo2 = GraphAlgo()
      file2 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A2.json'
      g_algo2.load_from_json(file2)
      self.assertEqual(g_algo2.load_from_json(file2), True)

    def test_loadA3(self):
      g_algo3 = GraphAlgo()
      file3 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A3.json'
      g_algo3.load_from_json(file3)
      self.assertEqual(g_algo3.load_from_json(file3), True)

    def test_loadA4(self):
      g_algo4 = GraphAlgo()
      file4 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A4.json'
      g_algo4.load_from_json(file4)
      self.assertEqual(g_algo4.load_from_json(file4), True)

    def test_loadA5(self):
       g_algo5 = GraphAlgo()
       file5 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A5.json'
       self.assertEqual(g_algo5.load_from_json(file5), True)

    def test_SaveA0(self):
         g_algo = GraphAlgo()
         file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A0.json'
         g_algo.load_from_json(file)
         self.assertEqual(g_algo.save_to_json("file.json"),True)

    def test_SaveA1(self):
         g_algo1 = GraphAlgo()
         file1 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A1.json'
         g_algo1.load_from_json(file1)
         self.assertEqual(g_algo1.save_to_json("file.json"), True)

    def test_SaveA2(self):
         g_algo2 = GraphAlgo()
         file2 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A2.json'
         g_algo2.load_from_json(file2)
         self.assertEqual(g_algo2.save_to_json("file.json"), True)

    def test_saveA3(self):
         g_algo3 = GraphAlgo()
         file3 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A3.json'
         g_algo3.load_from_json(file3)
         self.assertEqual(g_algo3.save_to_json("file.json"), True)

    def test_saveA4(self):
         g_algo4 = GraphAlgo()
         file4 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A4.json'
         g_algo4.load_from_json(file4)
         self.assertEqual(g_algo4.save_to_json("file.json"), True)

    def test_saveA5(self):
         g_algo5 = GraphAlgo()
         file5 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A5.json'
         g_algo5.load_from_json(file5)
         self.assertEqual(g_algo5.save_to_json("file.json"), True)

    def test_SPA0(self):
        g_algo = GraphAlgo()
        file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A0.json'
        g_algo.load_from_json(file)
        x,y= g_algo.shortest_path(0,3)
        j = [0, 1, 2, 3]
        self.assertEqual(x, 4.3086815935816)
        self.assertEqual(y, j)

    def test_SPA1(self):
        g_algo1 = GraphAlgo()
        file1 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A1.json'
        g_algo1.load_from_json(file1)
        x,y= g_algo1.shortest_path(0,3)
        j = [0, 1, 2, 3]
        self.assertEqual(x, 4.096793421922225)
        self.assertEqual(y, j)

    def test_SPA2(self):
        g_algo2 = GraphAlgo()
        file2 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A2.json'
        g_algo2.load_from_json(file2)
        x, y = g_algo2.shortest_path(0,3)
        j =  [0, 1, 2, 3]
        self.assertEqual(x, 4.096793421922225)
        self.assertEqual(y, j)

    def test_SPA3(self):
        g_algo3 = GraphAlgo()
        file3 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A3.json'
        g_algo3.load_from_json(file3)
        x, y = g_algo3.shortest_path(0, 3)
        j = [0, 1, 2, 3]
        self.assertEqual(x, 4.096793421922225)
        self.assertEqual(y, j)

    def test_SPA4(self):
        g_algo4 = GraphAlgo()
        file4 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A4.json'
        g_algo4.load_from_json(file4)
        x, y = g_algo4.shortest_path(0, 3)
        j = [0, 1, 2, 3]
        self.assertEqual(x, 4.053703927458311)
        self.assertEqual(y, j)

    def test_SPA5(self):
        g_algo5 = GraphAlgo()
        file5 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A5.json'
        g_algo5.load_from_json(file5)
        x, y = g_algo5.shortest_path(0, 3)
        j =  [0, 2, 3]
        self.assertEqual(x, 2.4671072694403673)
        self.assertEqual(y, j)

    def test_cA0(self):
        g_algo = GraphAlgo()
        file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A0.json'
        g_algo.load_from_json(file)
        x, y = g_algo.centerPoint()
        j = 7
        self.assertEqual(x, j)
        self.assertEqual(y,6.806805834715163)


    def test_cA1(self):
        g_algo1 = GraphAlgo()
        file1 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A1.json'
        g_algo1.load_from_json(file1)
        x, y = g_algo1.centerPoint()
        j = 8
        self.assertEqual(x, j)
        self.assertEqual(y, 9.925289024973141)

    def test_cA2(self):
        g_algo2 = GraphAlgo()
        file2 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A2.json'
        g_algo2.load_from_json(file2)
        x, y = g_algo2.centerPoint()
        j = 0
        self.assertEqual(x, j)
        self.assertEqual(y, 7.819910602212574)

    def test_cA3(self):
        g_algo3 = GraphAlgo()
        file3 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A3.json'
        g_algo3.load_from_json(file3)
        x, y = g_algo3.centerPoint()
        j = 2
        self.assertEqual(x, j)
        self.assertEqual(y, 8.182236568942237)

    def test_cA4(self):
        g_algo4 = GraphAlgo()
        file4 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A4.json'
        g_algo4.load_from_json(file4)
        x, y = g_algo4.centerPoint()
        j = 6
        self.assertEqual(x, j)
        self.assertEqual(y,8.071366078651435)

    def test_cA5(self):
        g_algo5 = GraphAlgo()
        file5 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A5.json'
        g_algo5.load_from_json(file5)
        x, y = g_algo5.centerPoint()
        j = 40
        self.assertEqual(x, j)
        self.assertEqual(y,9.291743173960954)


    def test_tspA0(self):
        g_algo = GraphAlgo()
        file = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A0.json'
        g_algo.load_from_json(file)
        x, y = g_algo.TSP([0,3 ,5])
        j = [5, 4, 3, 2, 1, 0]
        self.assertEqual(x, j)
        self.assertEqual(y, 7.654301221486735)


    def test_tspA1(self):
        g_algo1 = GraphAlgo()
        file1 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A1.json'
        g_algo1.load_from_json(file1)
        x, y = g_algo1.TSP([0,3 ,5])
        j = [0, 1, 2, 3, 4, 5]
        self.assertEqual(x, j)
        self.assertEqual(y, 6.492958412797456)

    def test_tspA2(self):
        g_algo2 = GraphAlgo()
        file2 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A2.json'
        g_algo2.load_from_json(file2)
        x, y = g_algo2.TSP([0,3 ,5])
        j = [0, 1, 2, 3, 4, 5]
        self.assertEqual(x, j)
        self.assertEqual(y, 6.492958412797456)

    def test_tspA3(self):
        g_algo3 = GraphAlgo()
        file3 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A3.json'
        g_algo3.load_from_json(file3)
        x, y = g_algo3.TSP([0, 3, 5])
        j = [0, 1, 2, 3, 4, 5]
        self.assertEqual(x, j)
        self.assertEqual(y, 6.492958412797456)

    def test_tspA4(self):
        g_algo4 = GraphAlgo()
        file4 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A4.json'
        g_algo4.load_from_json(file4)
        x, y = g_algo4.TSP([0, 3, 5])
        j = [0, 1, 2, 3, 4, 5]
        self.assertEqual(x, j)
        self.assertEqual(y, 7.215824789079969)

    def test_tspA5(self):
        g_algo5 = GraphAlgo()
        file5 = 'C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A5.json'
        g_algo5.load_from_json(file5)
        x, y = g_algo5.TSP([0, 3, 5])
        j = [0, 2, 3, 13, 5]
        self.assertEqual(x, j)
        self.assertEqual(y, 4.685698594072881)