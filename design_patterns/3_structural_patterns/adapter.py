def main():
    old_sys = OldSystem()
    client_code(old_sys)
    new_comp = NewComponent()
    adapter = Adapter(new_comp)
    client_code(adapter)
    

# Existing interface
class OldSystem:
    def request(self):
        return 'Old system request'


# New component with incompatible interface
class NewComponent:
    def specific_request(self):
        return 'New system specific request'


class Adapter(OldSystem):
    def __init__(self, new_component):
        self.new_component = new_component

    def request(self):
        return f'Adapter: {self.new_component.specific_request()}'


def client_code(target):
    print(target.request())


if __name__ == '__main__':
    main()
