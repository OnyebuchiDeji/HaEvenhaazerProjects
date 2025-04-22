#   Date: Sunu-7-July-2024

#   Briefing
This practice project demonstrates file transfer via sockets.
In this project, there is a sender script and a receiver script.

The sender script takes the file and sends its bytes via the network.
Then the receiver script gets those bytes and reconstructs it into the file.

Also used a module called twdm `pip install tqdm` to visualise a progress bar to show
the progress of the file transfer.
It's used for creating CLI progress bars in Python.


#   References
"File Transfer Via Socket", NeuralNine, 2022