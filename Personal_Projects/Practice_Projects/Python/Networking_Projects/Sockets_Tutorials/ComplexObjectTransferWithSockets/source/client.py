"""
    Demonstrates the sending of complex objects to a server

    It starts with a Python Dictionary all the way to a Scikit Machine Learning Module
"""

import socket as sckt
import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def eg1_():
    client_socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
    #   Connect to IP at localhost
    client_socket.connect(('127.0.0.1', 9999))

    try:
        my_obj = {'key1': 'val1', 'key2': 'val2'}
        serialized = pickle.dumps(my_obj)
        #   It sends all the data since the object is here so its size can be gotten.
        client_socket.sendall(serialized)

    finally:
        #   If it crashes, still close the socket
        client_socket.close()

def eg2_():
    #   First get data and configure and train model
    data = load_iris()
    x, y = data.data, data.target

    #   To make it be that the performance is not perfect, test_size = 0.5
    #   meaning half of the data for training and half for evaluating
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)

    #   Train Model
    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    #   Then create socket objects
    client_socket = sckt.socket(sckt.AF_INET, sckt.SOCK_STREAM)
    #   Connect to IP at localhost
    client_socket.connect(('127.0.0.1', 9999))

    try:
        #   Serialize and send model
        serialized = pickle.dumps(model)
        # print(serialized)
        #   It sends all the data since the object is here so its size can be gotten.
        client_socket.sendall(serialized)

    finally:
        #   If it crashes, still close the socket
        client_socket.close()


def main():
    # eg1_()
    eg2_()

if __name__ == "__main__":
    main()