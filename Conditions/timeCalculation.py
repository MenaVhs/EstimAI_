def time_per_frame(distances, FPS):
    time = [0]
    fps = FPS[0]

    for i in range(1, len(distances)):
        t = 1 / fps
        time.append(t)
    return time