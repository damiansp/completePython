def print_owning(invoice):
    print_banner()
    outstanding = calculate_outstanding()
    # print details
    print(f'Name: {invoice.customer}')
    print(f'Amount: {outstanding}')


# ->
def print_owning(invoice):
    print_banner()
    outstanding = calculate_outstanding()
    print_details(invoice, outstanding)

def print_details(invoice, outstanding):
    print(f'Name: {invoice.customer}')
    print(f'Amount: {outstanding}')
