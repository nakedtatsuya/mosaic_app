import cv2
import insightface
import numpy as np

face_analysis = insightface.app.FaceAnalysis()
face_analysis.prepare(ctx_id=0, det_size=(640, 640))


def compute_face_diff(target_face, registed_face_image_path) -> bool:
    embedding1 = target_face.embedding

    registed_face_image = cv2.imread(registed_face_image_path)
    registed_faces = face_analysis.get(registed_face_image)
    if len(registed_faces) != 1:
        return 0
    embedding2 = registed_faces[0].embedding

    # 顔認識
    return (
        np.dot(embedding1, embedding2)
        / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
        < 0.6
    )
