import threading
import zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip for:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('Main program continues to run in foreground')
background.join() # wait for task to finish
print('Main program waited till background was done.')
