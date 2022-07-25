def get_rating(driver):
    return 2 if has_more_than_five_late_deliveries(driver) else 1


def has_more_than_five_late_deliveries(driver):
    return driver.n_late_deliveries > 5


# ->
def get_rating(driver):
    return 2 if driver.n_late_deliveries > 5 else 1



def report_lines(customer):
    lines = []
    lines = gather_customer_data(lines, customer)
    return lines


def gather_customer_data(out, customer):
    out.append(['name', customer.name])
    out.append(['location', customer.location])
    return out


# ->
def report_lines(customer):
    lines = []
    lines.append(['name', customer.name])
    lines.append(['location', customer.location])
    return lines


