server_port = None

resign_draw_socket_recieving = None
resign_draw_socket_sending = None
game_socket = None
my_server_socket = None

is_client = None
other_ip_address = ""

name1 = ""
name2 = ""

main_window = None

window = None
lock = None
board = None
game = None
node = None
pop = None                  # pop is used for promotion

moves_table = None

voice_label = None
name_label3 = None
name_label4 = None

pgn_button = None

                        
button_list = []
chess_list = []

entry_list = [None]*300

move_counter = 0
move_list = []
color_val = None

x = True                    #Even_clicks checker
newp='t'
prev = -1
draw_offer_count = 0
game_ended = False