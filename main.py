import tkinter as tk


# joint = 'Spine'
# condition = 150
# unit = 'cm'  # or m
# event_time = 3  # sec
#
# config_path = r'C:\Users\Angel\Desktop\EstimAI-Mena-2023-07-06\config.yaml'
# video_path = r'D:\EstiAI_\4_JOINTS\0Iteration\1 SEC\ADFE_1-00-85_2-00-60 - 2SEC.mp4'
# # video_path = r'C:\Users\Angel\Desktop\PRUEBAS con videos externos\ADFE\Pruebas 100\100cm_recortado_brillo.mp4'
#
# shuffle = 1
# gputouse = 0
# videotype = 'mp4'
# save_as_csv_DeepLabCut = True
# destfolder_DeepLabCut_documents = None

# destfolder_DeepLabCut_documents = r'D:\EstiAI_\4_JOINTS\0Iteration\1 SEC\Datos DLC'

def guardar_datos():
    joint = joint_entry.get()
    condition = int(condition_entry.get())
    unit = unit_entry.get()
    event_time = int(event_time_entry.get())
    config_path = config_path_entry.get()
    video_path = video_path_entry.get()
    shuffle = int(shuffle_entry.get())
    gputouse = int(gputouse_entry.get())
    videotype = videotype_entry.get()
    save_as_csv_DeepLabCut = save_as_csv_DeepLabCut_var.get()
    destfolder_DeepLabCut_documents = destfolder_DeepLabCut_documents_entry.get()


    # Aquí puedes realizar cualquier acción adicional con los datos guardados

    print("Data saved correctly.")

# Crear la ventana principal
window = tk.Tk()
window.title("EstimAI")
window.geometry("400x500")

# Crear campos de entrada de texto
joint_label = tk.Label(window, text="Joint:")
joint_label.pack()
joint_entry = tk.Entry(window)
joint_entry.pack()

condition_label = tk.Label(window, text="Condition:")
condition_label.pack()
condition_entry = tk.Entry(window)
condition_entry.pack()

unit_label = tk.Label(window, text="Unit (cm or m):")
unit_label.pack()
unit_entry = tk.Entry(window)
unit_entry.pack()

event_time_label = tk.Label(window, text="Event Time (seg):")
event_time_label.pack()
event_time_entry = tk.Entry(window)
event_time_entry.pack()

config_path_label = tk.Label(window, text="Config Path:")
config_path_label.pack()
config_path_entry = tk.Entry(window)
config_path_entry.pack()

video_path_label = tk.Label(window, text="Video Path:")
video_path_label.pack()
video_path_entry = tk.Entry(window)
video_path_entry.pack()

shuffle_label = tk.Label(window, text="Shuffle:")
shuffle_label.pack()
shuffle_entry = tk.Entry(window)
shuffle_entry.pack()

gputouse_label = tk.Label(window, text="GPU to Use:")
gputouse_label.pack()
gputouse_entry = tk.Entry(window)
gputouse_entry.pack()

videotype_label = tk.Label(window, text="Video Type (.mp4):")
videotype_label.pack()
videotype_entry = tk.Entry(window)
videotype_entry.pack()

save_as_csv_DeepLabCut_var = tk.BooleanVar()
save_as_csv_DeepLabCut_checkbox = tk.Checkbutton(window, text="Save as CSV (DeepLabCut)", variable=save_as_csv_DeepLabCut_var)
save_as_csv_DeepLabCut_checkbox.pack()

destfolder_DeepLabCut_documents_label = tk.Label(window, text="Destination Folder (DeepLabCut):")
destfolder_DeepLabCut_documents_label.pack()
destfolder_DeepLabCut_documents_entry = tk.Entry(window)
destfolder_DeepLabCut_documents_entry.pack()

# Crear botón de guardar
guardar_button = tk.Button(window, text="Save", command=guardar_datos)
guardar_button.pack()


# Iniciar el bucle de la interfaz gráfica
window.mainloop()
