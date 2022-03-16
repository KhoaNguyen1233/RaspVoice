# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtCore import QObject, Qt, Slot, Property
from PySide2.QtGui import QGuiApplication, QStandardItemModel, QStandardItem 
from PySide2.QtQml import QQmlApplicationEngine

class ElementRoles:
    NameRole = Qt.UserRole
    ValueRole = Qt.UserRole + 1

class ElementModel(QStandardItemModel, ElementRoles):
    
    def __init__(self, parent=None):
        super(ElementModel, self).__init__(parent)
        roles = {
            ElementModel.NameRole: b'mcmdName',
            ElementModel.ValueRole: b'mcmdValue'
        }
        self.setItemRoleNames(roles)

    @Slot(str, str)
    def addElement(self, name, value):
        item = QStandardItem()
        item.setData(name, ElementModel.NameRole)
        item.setData(value, ElementModel.ValueRole)
        self.appendRow(item)

class Manager(QObject):
    def __init__(self, parent=None):
        super(Manager, self).__init__(parent)
        self._model = ElementModel()

    def addData(self, data):
        print(data)
        self._model.addElement(data[0],data[1])  
    
    @Property(QObject, constant=True)
    def model(self):
        return self._model
        

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    
    data = [
        ["Fans", "Low"],
       ["Lights", "On"],
       ["Diffuser", "On"],
       ["Socket", "On"],
    #    ["Fans", "High"],
    #    ["Lights", "Off"],
    #    ["Diffuser", "Off"],
    #    ["Socket", "Off"],
    #    ["Fans", "Medium"],
    #    ["Fans", "Off"],
    ]
    
    dataModel = Manager()
    engine = QQmlApplicationEngine()
    
    for item in data:
        print(item[0],"/",item[1])
        dataModel.addData(item)
        
    engine.rootContext().setContextProperty("dataModel",dataModel)    
        
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
