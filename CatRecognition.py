import cv2
from time import sleep


def load_cascade(cascade_path):
    cascade = cv2.CascadeClassifier(cascade_path)
    if cascade.empty():
        raise IOError(f'Неможливо завантажити файл каскадного класифікатора: {cascade_path}')
    return cascade


def process_frame(frame, cascade, scale_factor):
    frame_resized = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
    face_rects = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=8, minSize=(80, 80))

    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame_resized


def detect_and_display_faces(video_path, cascade_path, scale_factor=0.4):
    face_cascade = load_cascade(cascade_path)
    cap = cv2.VideoCapture(video_path)

    while True:
        sleep(0.01)
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_frame(frame, face_cascade, scale_factor)
        cv2.imshow('Cat Face Detector', processed_frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect_and_display_faces(video_path='cats.mp4', cascade_path='haarcascade_frontalcatface.xml')
