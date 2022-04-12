def golden_eagle(bounds, coords):
    if coords[0] < bounds[0] or coords[0] > bounds[2] and coords[1] < bounds[1] or coords[1] > bounds[3]:
        print("Miss")
        return
    print("Hit")

golden_eagle([0, 0, 10, 10], [5, 7])