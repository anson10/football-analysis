import cv2

# 24 frames per second

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  #output format
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (output_video_frames[0].shape[1],output_video_frames[0].shape[0] ))  #path, format, fps, (img_size #W 640, #H 480)
    for frame in output_video_frames:
        out.write(frame)
        
    out.release()