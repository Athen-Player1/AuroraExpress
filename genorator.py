import tkinter as tk
from tkinter import ttk

def handle_hand_side_selection(event):
    selected_hand_side = hand_side_combobox.get()

    if selected_hand_side == "left":
        ethercat_right_arm_label.grid_remove()
        ethercat_right_arm_combobox.grid_remove()
        arm_ip_right_label.grid_remove()
        arm_ip_right_entry.grid_remove()
        
        ethercat_left_arm_label.grid()
        ethercat_left_arm_entry.grid()
        arm_ip_left_label.grid()
        arm_ip_left_entry.grid()
    elif selected_hand_side == "right":
        ethercat_left_arm_label.grid_remove()
        ethercat_left_arm_entry.grid_remove()
        arm_ip_left_label.grid_remove()
        arm_ip_left_entry.grid_remove()
        
        ethercat_right_arm_label.grid()
        ethercat_right_arm_combobox.grid()
        arm_ip_right_label.grid()
        arm_ip_right_entry.grid()
    else:
        ethercat_right_arm_label.grid()
        ethercat_right_arm_combobox.grid()
        arm_ip_right_label.grid()
        arm_ip_right_entry.grid()
        
        ethercat_left_arm_label.grid()
        ethercat_left_arm_entry.grid()
        arm_ip_left_label.grid()
        arm_ip_left_entry.grid()

def generate_oneliner():
    customer_key = customer_key_entry.get()
    branch = branch_entry.get()
    tag = tag_entry.get()
    product = product_combobox.get()
    hand_side = hand_side_combobox.get()
    reinstall = reinstall_checkbox_var.get()
    ethercat_right_arm = ethercat_right_arm_combobox.get()
    arm_ip_right = arm_ip_right_entry.get()
    ethercat_left_arm = ethercat_left_arm_entry.get()
    arm_ip_left = arm_ip_left_entry.get()
    ur_robot_type = ur_robot_type_combobox.get()

    oneliner = "bash <(curl -Ls bit.ly/run-aurora) server_and_nuc_deploy --branch " + branch + " customer_key=\"" + customer_key + "\" product=" + product + " reinstall=" + str(reinstall)

    if product == "arm_hand_e":
        oneliner += " hand_side=" + hand_side
    
    if hand_side == "left":
        oneliner += " ethercat_left_arm=\"" + ethercat_left_arm + "\""
        oneliner += " arm_ip_left=\"" + arm_ip_left + "\""
    elif hand_side == "right":
        oneliner += " ethercat_right_arm=\"" + ethercat_right_arm + "\""
        oneliner += " arm_ip_right=\"" + arm_ip_right + "\""
    else:
        oneliner += " ethercat_right_arm=\"" + ethercat_right_arm + "\""
        oneliner += " arm_ip_right=\"" + arm_ip_right + "\""
        oneliner += " ethercat_left_arm=\"" + ethercat_left_arm + "\""
        oneliner += " arm_ip_left=\"" + arm_ip_left + "\""

    oneliner_output.delete("1.0", tk.END)
    oneliner_output.insert(tk.END, oneliner)

# Create the main window
window = tk.Tk()
window.title("Oneliner Generator")

# Create input fields and labels
customer_key_label = tk.Label(window, text="Customer Key:")
customer_key_entry = tk.Entry(window)

branch_label = tk.Label(window, text="Branch:")
branch_entry = tk.Entry(window)

tag_label = tk.Label(window, text="Tag:")
tag_entry = tk.Entry(window)

product_label = tk.Label(window, text="Product:")
product_combobox = ttk.Combobox(window, values=["arm_hand_e", "hand_e"], state="readonly")

hand_side_label = tk.Label(window, text="Hand Side:")
hand_side_combobox = ttk.Combobox(window, values=["left", "right", "both"], state="readonly")
hand_side_combobox.bind("<<ComboboxSelected>>", handle_hand_side_selection)

reinstall_checkbox_var = tk.BooleanVar()
reinstall_checkbox = tk.Checkbutton(window, text="Reinstall", variable=reinstall_checkbox_var)

ethercat_right_arm_label = tk.Label(window, text="EtherCAT Right Arm:")
ethercat_right_arm_combobox = ttk.Combobox(window, values=["eno1"], state="readonly")

arm_ip_right_label = tk.Label(window, text="Right Arm IP:")
arm_ip_right_entry = tk.Entry(window)

ethercat_left_arm_label = tk.Label(window, text="EtherCAT Left Arm:")
ethercat_left_arm_entry = tk.Entry(window)

arm_ip_left_label = tk.Label(window, text="Left Arm IP:")
arm_ip_left_entry = tk.Entry(window)

ur_robot_type_label = tk.Label(window, text="UR Robot Type:")
ur_robot_type_combobox = ttk.Combobox(window, values=["ur10e"], state="readonly")
ur_robot_type_combobox.set("ur10e")

generate_button = tk.Button(window, text="Generate", command=generate_oneliner)

# Create output field
oneliner_output_label = tk.Label(window, text="Generated Oneliner:")
oneliner_output = tk.Text(window, height=5)

# Arrange the components in the window using grid layout
customer_key_label.grid(row=0, column=0, sticky="e")
customer_key_entry.grid(row=0, column=1)

branch_label.grid(row=1, column=0, sticky="e")
branch_entry.grid(row=1, column=1)

tag_label.grid(row=2, column=0, sticky="e")
tag_entry.grid(row=2, column=1)

product_label.grid(row=3, column=0, sticky="e")
product_combobox.grid(row=3, column=1)

hand_side_label.grid(row=4, column=0, sticky="e")
hand_side_combobox.grid(row=4, column=1)

reinstall_checkbox.grid(row=5, column=0, columnspan=2)

ethercat_right_arm_label.grid(row=6, column=0, sticky="e")
ethercat_right_arm_combobox.grid(row=6, column=1)

arm_ip_right_label.grid(row=7, column=0, sticky="e")
arm_ip_right_entry.grid(row=7, column=1)

ethercat_left_arm_label.grid(row=8, column=0, sticky="e")
ethercat_left_arm_entry.grid(row=8, column=1)

arm_ip_left_label.grid(row=9, column=0, sticky="e")
arm_ip_left_entry.grid(row=9, column=1)

ur_robot_type_label.grid(row=10, column=0, sticky="e")
ur_robot_type_combobox.grid(row=10, column=1)

generate_button.grid(row=11, column=0, columnspan=2)

oneliner_output_label.grid(row=12, column=0, sticky="e")
oneliner_output.grid(row=12, column=1)

# Run the GUI event loop
window.mainloop()
