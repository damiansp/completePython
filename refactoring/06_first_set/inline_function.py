def get_rating(driver):
    return 2 if has_more_than_five_late_deliveries(driver) else 1


def has_more_than_five_late_deliveries(driver):
    return driver.n_late_deliveries > 5


# ->
def get_rating(driver):
    return 2 if driver.n_late_deliveries > 5 else 1
