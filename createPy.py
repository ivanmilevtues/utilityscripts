network_pane ="network_pane.png"
packets_pane = "packets_pane.png"
results_pane = "1616870839364.png"

win_button = 

csv_file_select="1616870859945.png"
file_picker = "file_picker.png"
save_btn = "save_btn.png"
simulate_btn="1616870891230.png"
ready_simulation_indication = "ready_simulation_indication.png"

leng_buffers =["1616870950372.png","1616870916741.png","1616870926114.png","1616870937034.png"]
inject_channels=["1616870970877.png","1616870980028.png","1616870994672.png","1616871003602.png"]
package_size = ["1616871049622.png","1616871058342.png","1616871070454.png","1616871080962.png"]

broken_configs = [13]


def find_and_click(element):
    find(element)
    click(element)


def setup_network(buffer_size_indx, in_channel_indx):
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
    # if algorithm_indx != None:
    #     find_and_click(routing_algos[algorithm_indx - 1])
    #     handle(algorithm_indx)


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
    write("E:\TU\VPKS\lab2\simulation" + ("0" if simulation_indx < 10 else "") + str(simulation_indx) + ".csv")
    find_and_click(save_btn)


def setup_simulation(simulation_id, buffer_size_id, in_channel_id, package_size_id):
    setup_file_to_save(simulation_id)
    setup_network(buffer_size_id, in_channel_id)
    setup_packets(package_size_id)


def run_simulation():
    find_and_click(simulate_btn)
    find(win_button)
    wait(Pattern(ready_simulation_indication).exact(), FOREVER)

def none_if_same(new, old):
    return new if new != old else None

def run_all_simulations():
    simulation_id = 0
    # invalid data
    last_bf = 100
    last_chn = 100
    last_pck = 100
    last_algo = 100
    for buffer_id in range(4):
        for channel_id in range(4):
            # for algorithm_id in range (3):
                for package_size in range(4):
                    simulation_id += 1
                    if simulation_id in broken_configs:
                        continue
                    if(simulation_id < 13):
                        continue
                    setup_simulation(
                        simulation_id,
                        buffer_id,
                        channel_id,
                        # none_if_same(algorithm_id, last_algo),
                        package_size
                    )
                    # last_bf, last_chn, last_pck = buffer_id, channel_id, package_size
                    run_simulation()

run_all_simulations()