import glob
import time
from datetime import datetime
import cv2
import supervision
from ultralytics import YOLO
import random
from barcode import EAN13
from barcode.writer import ImageWriter

from Funcs_.config_app import PATH_MODEL_YOLO_V8, YOLOv8_IMAGE_INPUT_SIZE

if "def":
    def save_image(image_param, path_save_image, format_save_image=".jpg"):
        now = datetime.now()
        time.sleep(1)
        fileName = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3] + ".jpg"
        path_save_image = path_save_image + fileName + format_save_image
        cv2.imwrite(path_save_image, image_param)
        print(f"Image saved successfully at {path_save_image}")


    def resize_image(path_, save_path, width=416, height=416):
        images_folders = glob.glob(path_ + "/" + "*.jpg")
        dim = (width, height)
        for p in images_folders:
            fileName = datetime.utcnow().strftime('%Y-%m-%d__%H-%M-%S-%f')

            image_ = cv2.imread(p)
            image_resized = cv2.resize(image_, dim, interpolation=cv2.INTER_AREA)
            name = save_path + '/' + fileName + ".jpg"
            check_save = cv2.imwrite(name, image_resized)

            if not check_save:
                raise Exception("Could not write image")
            else:
                print('Created...' + name)
            if cv2.waitKey(1) == 27:
                break
        cv2.destroyAllWindows()


    def extract_image_from_video(path):
        """
        Extract ảnh từ video.
        :param path:
        :return:
        """
        path_videos = glob.glob(path + "/*.mp4")
        current_frame = 0
        for path_video in path_videos:
            cap = cv2.VideoCapture(path_video)
            if not cap.isOpened:
                print("Can note open video")
                exit()
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                name = path + '/imgs/' + str(current_frame) + '.jpg'
                print('Creating...' + name)
                cv2.imwrite(name, frame)
                current_frame += 1
                if cv2.waitKey(1) == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()


    def duplicate_labels(path):
        c = 5
        current = c
        limit = 14

        file_original = path + f"/{str(c)}.txt"

        while current < limit:
            current = current + 1
            file_copy = path + f"/{str(current)}.txt"
            with open(file_original, mode="r") as file1, open(file_copy, mode="a") as file2:
                for line in file1:
                    file2.write(line)


    def extract_barcode_img_from_yolov8_result(path_param):
        model_yolov8 = YOLO(PATH_MODEL_YOLO_V8)
        img = cv2.imread(path_param)
        image_resize = cv2.resize(img, YOLOv8_IMAGE_INPUT_SIZE, interpolation=cv2.INTER_AREA)
        result = model_yolov8(image_resize)[0]

        detections_ = supervision.Detections.from_yolov8(result)
        x1, y1, x2, y2 = [int(num_) for num_ in detections_.xyxy[0]]
        image_crop = image_resize[y1 - 2:y2 + 2, x1 - 2:x2 + 2]
        img_rectangle = cv2.rectangle(image_resize, (x1 - 2, y1 - 2), (x2 + 2, y2 + 2), (255, 0, 0), 2)

        cv2.imshow("test1", img_rectangle)
        cv2.imshow("test2", image_crop)

        k = cv2.waitKey(0)
        if k == ord("s"):
            cv2.imwrite("../sddle_data/working_on_images/barcode_restore_2.jpg", image_crop)
        print("debug")

    def generate_barcode():
        count_index = 0

        while count_index < 1000:
            number_in_barcode = str(random.random()).replace(".", "")
            my_code = EAN13(number_in_barcode, writer=ImageWriter())
            my_code.save(f"Data/SR_Barcode_Images/{count_index}")
            count_index += 1

RUN = 1
if 1 == RUN:
    generate_barcode()
