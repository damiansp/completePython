from threading import Thread
import tkinter as tk

from pytube import YouTube


BG = 'olivedrab1'  # GUI background color


def main():
    root = GUIBuilder.build()
    root.mainloop()


class GUIBuilder:
    def __init__(self):
        self.root = self._init_root()
        self.url_box = None

    def _init_root():
        root = tk.Tk()
        root.title('YouTube Downloader')
        root.geometry('780x500+200+200')
        root.configure(bg=BG)
        root.resizable(False, False)
        return root

    def build():
        self._add_labels()
        self._add_url_box()
        self._add_download_button()

    def _add_labels(self):
        intro_label = tk.Label(
            self.root,
            text='YouTube Video Downloader',
            width=30,
            relief='ridge',
            bd=4,
            font=('chiller', 26, 'italic bold'),
            fg='red')
        intro_label.place(x=35, y=20)
        tk.Label(
            self.root,
            text='Enter YouTube Link',
            font=('sans-serif', 16),
            bg=BG
        ).place(x=40, y=150)

    def _add_url_box(self):
        url_box = tk.Entry(self.root, font=('arial', 30), width=30)
        url_box.place(x=40, y=180)
        self.url_box = url_box

    def _add_download_button(self):
        btn = tk.Button(
            self.root,
            text='Download',
            font=('sans-serif', 24),
            command=self._do_threading)
        btn.place(x=270, y=240)

    def _do_threading():
        thread = Thread(target=self._download)
        thead.start()

    def _download():
        try:
            url = YouTube(str(self.url_box.get()))
            vid = url.streams.first()
            file_name = tk.filedialog.asksaveasfilename(
                defaultextension='.mp4', filetypes=[('MP4 files', '*.mp4')])
            if file_name:
                vid.downlaode(filename=file_name)
                tk.messagebox.showinfo('', 'Download completed!')
            else:
                tk.messagbox.showwarning('', 'Download cancelled.')
        except Exception as e:
            tk.messagebox.showerror(
                'Error', f'Unexpectd error while downloading:\n{e}')
            


if __name__ == '__main__':
    main()
