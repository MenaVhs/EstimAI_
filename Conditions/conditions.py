# CU: Presentar evento simulado bajo criterio de distancia
def distance_condition(acumulated_distances, x, y, times_per_frame, distances_per_frame, event_time, c, FPS):
    fps = FPS[0]
    relative_time = 0
    frames_per_time_event = event_time * fps  # frames que deben transcurrir para terminar el evento desde que se inició
    event_status = 0
    frame_time_list = []
    acumulated_distance_list = []
    relative_distance = 0
    relative_distance_list = []
    event_status_list = []

    count = 0
    for frame_time, acumulated_distance in acumulated_distances:
        count += 1
        frame_time_list.append(frame_time)
        acumulated_distance_list.append(acumulated_distance)



    for i, distance_per_frame in enumerate(distances_per_frame):
        relative_distance += distance_per_frame

        # Se inicia el evento
        if relative_distance >= c:  # si se cumple criterio de distancia -> 3
            event_status = 1  # inicializa el evento por los segundos de time_e

            relative_index = i
            # relative_distance_list.append(relative_distance)

            relative_time += 1

            # Fin de evento
            if relative_time > frames_per_time_event:
                event_status = 0
                relative_index = 0

                # Reset  de distancia relativa en el índice siguiente donde acabó el fin de evento
                relative_distance = distances_per_frame[i]
                relative_time = 0


        relative_distance_list.append(relative_distance)

        event_status_list.append(event_status)

    # print(acumulated_distance_list) # diatancia acumulada durante todo_ el video
    # print(frame_time_list) # segundo por cada frame
    # print(relative_distance_list) # distancia acumulada hasta finalizar un evento
    # print(event_status_list) # Estado del evento por cada frame

    return times_per_frame, x, y, distances_per_frame, acumulated_distance_list, relative_distance_list, event_status_list

