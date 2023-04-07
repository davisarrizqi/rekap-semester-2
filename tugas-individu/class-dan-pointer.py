import os; import random
import matplotlib.pyplot as plt


class DataControl:
    def __init__(self, statisticData=['default'], statisticLabel=['default']):
        self.statisticData = statisticData; self.statisticLabel = statisticLabel
        self.encryptedData = self.encryptData(id(self.statisticData))
        self.encryptedLabel = self.encryptData(id(self.statisticLabel))
        
        self.tempData = { 
            self.encryptedData  : self.statisticData, 
            self.encryptedLabel : self.statisticLabel 
        }

        self.statisticData = None; self.statisticLabel = None

    def updateData(self, dataList):
        self.statisticData = dataList

    def updateLabel(self, labelList):
        self.statisticLabel = labelList

    def encryptData(self, data):
        data = (data * 2010105) + 18102003
        return data

    def decryptData(self, data):
        data = int((int(data) - 18102003)/2010105)
        return data

    def idToValue(self, id):
        try: data = tempData[id]; return data
        except: print("Data tidak ditemukan!"); return None

class DataStatistic(DataControl):
    def __init__(self, statisticData, statisticLabel, title='Davis Figure'):
        super().__init__(statisticData, statisticLabel)
        self.title = title; self.color = None

    def setTitle(self, title):
        self.title = title

    def setColor(self, color):
        self.color = color

    def displayBar(self):
        plt.bar(self.tempData[self.encryptedLabel], self.tempData[self.encryptedData], color=self.color if self.color != None else 'blueviolet')
        plt.show()

    def displayPie(self):
        plt.pie(self.tempData[self.encryptedData], labels=self.tempData[self.encryptedLabel], autopct="Berjumlah %i")
        plt.show()


if __name__ == '__main__':
    data = [10, 30, 50, 20, 70, 100]
    label = [f"Bulan ke {dataset + 1}" for dataset in range(len(data))]
    myData = DataStatistic(data, label); myData.setTitle("Sample Image")
    # myData.displayBar()
    myData.displayPie()
    data, label = None, None
    