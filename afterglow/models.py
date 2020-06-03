from django.db import models

import tensorflow as tf
import numpy as np
import cv2
import io
from PIL import Image

graph = tf.compat.v1.get_default_graph()

class Photo(models.Model):
    image = models.ImageField(upload_to='photos')

    IMAGE_SIZE = 64
    MIN_SIZE = 32
    MODEL_FILE_PATH = './afterglow/ml_models/afterglow.h5'
    classes = ['ran', 'moca', 'himari', 'tsugumi', 'tomoe']

    def detect_main(self):
        model = None
        global graph
        with graph.as_default():
            model = tf.keras.models.load_model(self.MODEL_FILE_PATH)

            img_data = self.image.read()
            image = io.BytesIO(img_data)

            # 顔検出実行
            rec_image = self.detect_face(image, model)

            return image

    def detect_face(self, image, model):
        img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        cascade_xml = './cascade/lbpcascade_animeface.xml'
        cascade = cv2.CascadeClassifier(cascade_xml)

        # 顔検出の実行
        faces = cascade.detectMultiScale(
            img_gray, scaleFactor=1.11, minNeighbors=2, minSize=self.MIN_SIZE)

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face_img = image[y:y+h, x:x+w]
                face_img = cv2.resize(face_img, self.IMAGE_SIZE)
                # BGR->RGB変換、float型変換
                face_img = cv2.cvtColor(
                    face_img, cv2.COLOR_BGR2RGB).astype(np.float32)
                name, score = self.prediction(face_img, model)
                col = self.classes[name]
                # 認識結果を元画像に表示
                if score >= 0.60:
                    cv2.rectangle(image, (x, y), (x+w, y+h), col, 2)
                    cv2.putText(image, '%s:%d%%' % (name, score*100),
                                (x+10, y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, col, 2)
                else:
                    cv2.rectangle(image, (x, y), (x+w, y+h), (192, 192, 192), 2)
                    cv2.putText(image, '%s:%d%%' % ('others', score*100),
                                (x+10, y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (192, 192, 192), 2)
        else:
            pass
        return image

    def prediction(self, x, model):
        # 画像データをテンソル整形
        x = np.expand_dims(x, axis=0)
        x = x / 255.0
        pred = model.predict(x)[0]

        # 確率が高い上位3キャラを出力
        num = 3
        top_indices = pred.argsort()[-num:][::-1]
        result = [(self.classes[i], pred[i]) for i in top_indices]

        # 1番予測確率が高いキャラ名を返す
        return result[0]
