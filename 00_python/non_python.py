def make_chai():
    if not kettle_hes_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    add_tea_cup("tea leaves")
    add_tea_cup("sugar")
    pour("boiled water")
    stir()
    serve()

    make_chai()