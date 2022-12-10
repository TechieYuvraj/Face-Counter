import cv2
import mediapipe as mp
face_detection = mp.solutions.face_detection.FaceDetection(0.6)

def detector(frame):

    count = 0
    height, width, channel = frame.shape
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_detection.process(imgRGB)

    try:
        for count, detection in enumerate(result.detections):
            score = detection.score
            box = detection.location_data.relative_bounding_box
            x, y, w, h = int(box.xmin*width), int(box.ymin * height), int(box.width*width), int(box.height*height)
            score = str(round(score[0]*100, 2))
            print(x, y, w, h)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x+w, y-25), (0, 0, 255), -1)
            cv2.putText(frame, score, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        count += 1
        print("Found ",count, "Faces!")

    except:
        pass 
    return count, frame

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    count, output = detector(frame)
    cv2.putText(output, "Number of Faces: "+str(count),(10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2 )
    cv2.imshow("frame", output)
    if cv2.waitKey(15) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()