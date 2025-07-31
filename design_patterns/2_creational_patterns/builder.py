class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return (
            f'Computer: CPU: {self.cpu}, Memory: {self.memory}GB, '
            f'Storage: {self.storage}GB, GPU: {self.gpu}')


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def configure_memory(self, mem):
        self.computer.memory = mem
        return self

    def configure_storage(self, stor):
        self.computer.storage = stor
        return self

    def configure_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer


class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_gaming_computer(self):
        computer = (
            self
            .builder
            .configure_cpu('Intel i9')
            .configure_memory(32)
            .configure_storage(1000)
            .configure_gpu('Nvidia RTX 3080')
            .build())
        return computer

    def build_office_computer(self):
        computer = (
            self
            .builder
            .configure_cpu('Intel i5')
            .configure_memory(16)
            .configure_storage(512)
            .build())
        return computer


def main():
    builder = ComputerBuilder()
    director = ComputerDirector(builder)
    gaming_pc = director.build_gaming_computer()
    print(gaming_pc)
    office_pc = director.build_office_computer()
    print(office_pc)
    custom_pc = (
        builder
        .configure_cpu('AMD Ryzen 7')
        .configure_memory(64)
        .configure_storage(2000)
        .configure_gpu('AMD Radeon RX 6800')
        .build())
    print(custom_pc)


if __name__ == '__main__':
    main()

