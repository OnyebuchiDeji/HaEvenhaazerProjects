"""
    This sucessfully does the monocular depth test estimation with MiDaS
"""
#   Import Dependencies
import cv2
import torch
import matplotlib.pyplot as plt


#   Download the MiDaS
#   Downloading the small model version of MiDaS
midas = torch.hub.load('intel-isl/MiDaS', 'MiDaS_small')
#   this `.to` sends the MiDaS model to the CPU
midas.to('cpu')
#   The below removes the training regularization steps
#   used when performing inference
midas.eval()

#   Input the transformation pupeline
transforms = torch.hub.load('intel-isl/MiDaS', 'transforms')
transform = transforms.small_transform


#   Hook into OpenCV
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    #   Transform input for midas
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgbatch = transform(img).to('cpu')

    #   Make a Prediction
    with torch.no_grad():
        prediction = midas(imgbatch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size = img.shape[:2],
            mode = 'bicubic',
            align_corners = False,
        ).squeeze()

        output = prediction.cpu().numpy()

        # print(prediction)
        print(output)

    plt.imshow(output)
    cv2.imshow('CV2Frame', frame)
    #   Gives matplotlivb some time to make the update
    plt.pause(0.00001)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        frame.release()
        cv2.destroyAllWindows()
    
plt.show()