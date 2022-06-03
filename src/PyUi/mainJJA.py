from sqlite3 import paramstyle
from cv2 import Scharr

from traitlets import default
import main_window
import docReader




sigma=1
updb=0.17650
edgesType=Scharr
iteration=10
Clusters=5
udpf=0.01790
coefficientType="Perona and Malik II"


class Parameters():
    def __init__(self):

        self.t = 10
        self.updb = 0.17650
        self.updf = 0.01790
        self.sigma = 1
        self.num_seg = 8

        self.edge = 'Scharr'
        self.coeff = "Perona and Malik II"
        self.value = True
    

def main():
    myWindow=main_window.MainWindow()
    docReader.DocRead()
    myWindow.picturesList=docReader.mylist
        
main()