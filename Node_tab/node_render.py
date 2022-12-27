# import dearpygui.dearpygui as gui

# variable for node editor


# node click events callbacks

def right_click_node_menu_callback(sender, app_data, user_data):
    gui = user_data["gui"]

    # get active tab based on it position
    if gui.get_item_state("node_tab")["pos"] == [8, 31]:
        gui.configure_item("right_click_menu_node_menu", show=True)
        gui.set_item_pos("right_click_menu_node_menu", gui.get_mouse_pos(local=False))


def left_click_node_menu_callback(sender, app_data, user_data):
    gui = user_data["gui"]

    # get active tab based on it position
    if gui.get_item_state("node_tab")["pos"] == [8, 31]:
        if gui.get_item_state(gui.get_active_window())["hovered"] is not True:
            gui.configure_item("right_click_menu_node_menu", show=False)


# callback runs when user attempts to connect attributes
def link_callback(sender, app_data, gui):
    # app_data -> (link_id1, link_id2)
    gui.add_node_link(app_data[0], app_data[1], parent=sender)


# callback runs when user attempts to disconnect attributes
def delink_callback(sender, app_data, gui):
    # app_data -> link_id
    gui.delete_item(app_data)


# ============================================================================================
# ============================================================================================

# node functions

def init_node_menu(gui):

    # TODO: need to solve this error to show combo box at node menu or choose different option
    gui.add_combo({"CSV": "csv", "Excel": "xlsx"},
                  default_value="DataFrame", width=400, tag="cb_node_type_node_tab",
                  parent="right_click_menu_node_menu")


# ============================================================================================
# ============================================================================================

# main node tab
# this is just for development purpose
def node_render():
def node_render(gui, DATA_TABLE):
    gui.delete_item("node_tab")

    # node tab
    with gui.tab(label="node tab", tag="node_tab", parent="main_tab_bar"):
        # node editor ground
        with gui.node_editor(tag="node_ground_node_tab", callback=link_callback, delink_callback=delink_callback,
                             user_data=gui, minimap=True, minimap_location=True, parent="node_tab"):

            # created right click registry
            with gui.handler_registry():
                gui.add_mouse_click_handler(button=gui.mvMouseButton_Right, callback=right_click_node_menu_callback,
                                            user_data={"gui": gui})
                gui.add_mouse_click_handler(button=gui.mvMouseButton_Left, callback=left_click_node_menu_callback,
                                            user_data={"gui": gui})

            with gui.window(label="Right click node menu", modal=True, show=False, id="right_click_menu_node_menu",
                            no_title_bar=True, tag="right_click_menu_node_menu"):
                init_node_menu(gui=gui)


