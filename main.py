import dearpygui.dearpygui as dpg

dpg.create_context()

def print_text():
    print("yoyo")

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")

    button1 = dpg.add_button(label="Press Me!", callback=print_text)

    slider_int = dpg.add_slider_int(label="Slide to the left!", width=100)
    slider_float = dpg.add_slider_float(label="Slide to the right!", width=100)

    dpg.add_simple_plot(label="Simpleplot1", default_value=(0.3, 0.9, 0.5, 0.3), height=300)
    dpg.add_slider_int(label="slider")

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
