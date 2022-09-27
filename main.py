import arcade

my_window = arcade.open_window(800,650, "Our First Window Demo")
arcade.set_background_color(arcade.color.BLUEBERRY)

arcade.start_render()
#everything else goes here
arcade.draw_lrtb_rectangle_filled(160, 460, 150, 50, arcade.color.CADET_GREY)
arcade.draw_xywh_rectangle_outline(10, 10, 380, 250, arcade.color.BLACK, 6)
arcade.draw_xywh_rectangle_outline(400, 100, 390, 50, arcade.color.AMBER, 6)
arcade.draw_circle_filled(75, 400, 50, arcade.color.ALLOY_ORANGE)
arcade.draw_circle_outline(85, 400, 75, arcade.color.BITTER_LIME, 6)
arcade.draw_triangle_outline(300, 400, 700, 800, 600, 400, arcade.color.AZURE_MIST, 7)
arcade.draw_triangle_filled(300, 700, 100, 500, 700, 600, arcade.color.BITTER_LIME)
arcade.finish_render()
arcade.run()