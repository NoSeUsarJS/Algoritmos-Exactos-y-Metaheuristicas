from Problem import Problem
from Node import Node
import threading
import time

mutex = threading.Lock()

ini = time.time()
class MFC:
    problem: Problem = None
    X_domain: list[list[int]] = None
    X: list = None
    m: int = None
    n: int = None
    max_FO_value: int = None
    nodes: list[Node] = []
    filtered_domain: list[list[int]] = None
    
    Max_Fo_time: list = []
    Time: list = []

    def __init__(self, data_path) -> None:
        self.problem = Problem(data_path)
        self.m = self.problem.m
        self.n = self.problem.n
        self.X_domain = [[1,0]] * self.m
        self.X = [0] * self.m
        self.max_FO_value = 0
        self.stop_threads = False

    
    def run(self, num_threads):
        self._init_mfc(num_threads=num_threads)
    
    def _init_mfc(self, num_threads):
        threads: list[threading.Thread] = []
        chunk_size = self.m // num_threads

        for i in range(0, self.m, chunk_size):
            end_index = min(i + chunk_size, self.m)
            X_copy = self.X[:]
            thread = threading.Thread(target=self._mfc, args=(X_copy, i, end_index))
            threads.append(thread)
            thread.daemon = True
            thread.start()
        
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.stop_threads = True

        for thread in threads:
            thread.join()

    def _mfc(self, X:list, current_index, end_index: int):
        if self.stop_threads:
            return

        if not self.problem._check_restrictions(X) or current_index >= self.m:
            return
        else:
            fo = self.problem._get_FO_value(X)
            #print(fo)
            with mutex:
                if self.max_FO_value < fo:
                    self.max_FO_value = fo
                    print(f"Max FO: {self.max_FO_value}")
                    self.Max_Fo_time.append(fo)
                    fin=time.time()
                    print(f"Current time: {round(fin-ini, 1)} s")
                    self.Time.append(fin-ini)
        
        for i in range(current_index, end_index):
            X_copy = X[:]
            X_copy[i] = 1
            self._mfc(X_copy, i+1, end_index)
                




            
