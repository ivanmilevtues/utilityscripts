injection_uncheck = "injection_uncheck.png"
ejection_channels = "ejection_channels.png"
virtuals = "1616929432713.png"
head_fits = "1616929460711.png"
nodes = "1616929445285.png"
number_of_packtes = "1616929483594.png"
show_simulation_btn = "1616929497242.png"
network_pane ="network_pane.png"
simulation_pane = "simulation_pane.png"
packets_pane = "packets_pane.png"
results_pane = "1616870839364.png"

win_button = "win_button.png"

csv_file_select="1616870859945.png"
file_picker = "file_picker.png"
save_btn = "save_btn.png"
simulate_btn="1616870891230.png"
ready_simulation_indication = "ready_simulation_indication.png"

leng_buffers =["1616870950372.png","1616870916741.png","1616870926114.png","1616870937034.png"]
inject_channels=["1616870970877.png","1616870980028.png","1616870994672.png","1616871003602.png"]
package_size = ["1616871049622.png","1616871058342.png","1616871070454.png","1616871080962.png"]
algorithm = "algorithm.png"

broken_configs = [13, 14, 15, 16, 29, 30, 31, 32, 46, 45, 47, 48, 61, 62, 63, 64,
                  77, 78, 79, 80, 93, 94, 95, 96, 109, 110, 111, 112, 125, 126, 127, 128,
                  141, 142, 143, 144 ,157 , 158, 159, 160, 173, 174 , 175 , 176, 189, 190, 191, 192]
start_from = 0
offset_postfix = 0 

def find_and_click(element):
    find(element)
    click(element)


def setup_network(buffer_size_indx, in_channel_indx, algorithm_indx):
    global leng_buffers
    global inject_channels
    global routing_algos
    find_and_click(network_pane)
    if buffer_size_indx != None:
        find_and_click(leng_buffers[buffer_size_indx - 1])
        clear()
        write(str(2 ** buffer_size_indx))
    if in_channel_indx != None:
        find_and_click(inject_channels[in_channel_indx - 1])
        clear()
        write(str(2** in_channel_indx))
    if(algorithm_indx != 0):
        find_and_click(algorithm)
        if(algorithm_indx == 1):
            write(Key.DOWN)
            write(Key.DOWN)
        if(algorithm_indx == 2):
            write(Key.DOWN)
            write(Key.DOWN)
            write(Key.DOWN)
        write(Key.ENTER)


def setup_packets(package_indx):
    global package_size
    find_and_click(packets_pane)
    if package_indx != None:
        find_and_click(package_size[package_indx - 1])
        clear()
        write(str([32, 64, 128, 256][package_indx]))


def clear():
    for _ in range(5):
        write(Key.BACKSPACE)


def handle(algorithm_indx):
    if algorithm_indx == 0:
        write(Key.UP)
        write(Key.UP)
        write(Key.UP)
    elif algorithm_indx == 1:
        write(Key.DOWN)
        write(Key.DOWN)
    else:
        write(Key.DOWN)
    write(Key.ENTER)


def setup_file_to_save(simulation_indx):
    find_and_click(results_pane)
    find_and_click(csv_file_select)
    wait(file_picker)
    find_and_click(file_picker)
    write("F:\\TU\\simulation" + ("0" if simulation_indx + offset_postfix < 10 else "") + str(simulation_indx + offset_postfix) + ".csv")
    find_and_click(save_btn)


def setup_simulation(simulation_id, buffer_size_id, in_channel_id, package_size_id, algorithm_id):
    setup_file_to_save(simulation_id)
    setup_network(buffer_size_id, in_channel_id, algorithm_id)
    setup_packets(package_size_id)


def run_simulation():
    find_and_click(simulate_btn)
    find_and_click(network_pane)
    wait(Pattern(ready_simulation_indication).exact(), FOREVER)

def none_if_same(new, old):
    return new if new != old else None

def run_all_simulations():
    init_config()
    simulation_id = 0

    for algorithm_id in range (3):
        for buffer_id in range(4):
            for channel_id in range(4):
                for package_size in range(4):
                    simulation_id += 1
                    if simulation_id in broken_configs:
                        continue
                    if(simulation_id < start_from):
                        continue
                    setup_simulation(
                        simulation_id,
                        buffer_id,
                        channel_id,
                        package_size,
                        algorithm_id
                    )
                    run_simulation()


def init_config():
    find_and_click(network_pane)
    find_and_click(nodes)
    clear()
    write("8")
    click(injection_uncheck)
    find_and_click(virtuals)
    clear()
    write("2")
    find_and_click(ejection_channels)
    clear()
    write("4")

    find_and_click(packets_pane)
    find_and_click(number_of_packtes)
    clear()
    write("2000")
    find_and_click(head_fits)
    clear()
    write("1")

    find_and_click(simulation_pane)
    find_and_click(show_simulation_btn)


run_all_simulations()