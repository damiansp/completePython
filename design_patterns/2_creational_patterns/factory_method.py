from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def create(self):
        pass


class PDFDocument(Document):
    def create(self):
        return 'Creating PDF doc'


class WordDocument(Document):
    def create(self):
        return 'Creating Word doc'


class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self):
        pass

class PDFFactory(DocumentFactory):
    def create_document(self):
        return PDFDocument()


class WordFactory(DocumentFactory):
    def create_document(self):
        return WordDocument()


def client_code(factory):
    doc = factory.create_document()
    print(doc.create())
    

pdf_fac = PDFFactory()
word_fac = WordFactory()
client_code(pdf_fac)
client_code(word_fac)
