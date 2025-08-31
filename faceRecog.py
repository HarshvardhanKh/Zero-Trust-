import cv2
import face_recognition as fr


def checkFace():
    cam = cv2.VideoCapture(0)

    rec,frame = cam.read()
    cam.release()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_encoding = fr.face_encodings(frame_rgb)[0]

    src = cv2.imread("userData/faceData.jpg")
    src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    src_encoding = fr.face_encodings(src_rgb)[0]

    result = fr.compare_faces([frame_encoding],src_encoding)
    cv2.waitKey(0)
    return result[0]
