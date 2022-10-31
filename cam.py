import cv2
# cam = cv2.VideoCapture(0)
# while True:
#     _, frame = cam.read()
#     cv2.imshow('my cam', frame)
#     cv2.waitKey(1)

# cap = cv2.VideoCapture(1)
# while(True):
#     _,frame = cap.read()
#     # cv2.rectangle(frame, (100, 100), (200, 200), [255, 0, 0], 2)
#     # Display the resulting frame
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break


# cap.release()
# cv2.destroyAllWindows()

# import the opencv library
import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# De