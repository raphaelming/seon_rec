import cv2
from datetime import datetime


class RecordScreen:

    SCREEN_SIZE = (1920, 1080)
    base_name = 'record'
    suffix = datetime.now().strftime('%y%m%d_%H%M%S')
    file_name = '_'.join([base_name, suffix])
    extension = '.avi'
    print(file_name + extension)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # out = cv2.VideoWriter(file_name + extension, fourcc, 20.0, (SCREEN_SIZE))
    cv2.destroyAllWindows()



