import threading

import custTray_phoenix as custTray
import wx
import main as ap


class MainFrame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Pwd Generator", size=(360, 300))
        # Расположить по центру экрана
        self.Center()
        panel = wx.Panel(self)
        self.tbIcon = custTray.CustomTaskBarIcon(self)
        # Изменить размер шрифта и цвет текста
        wx.StaticText(panel, label="Run generator password (len 7 symbols)", pos=(60, 30)).SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        wx.StaticText(panel, label="Num7 - ", pos=(10, 30)).SetForegroundColour(wx.Colour(0, 0, 255))

        # Изменить иконку приложения
        icon = wx.Icon('Z:\\Files\\PYTHON\\bind_keyboard\\ico\\key_treey.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.Show()

    def onClose(self, evt):
        """
        Уничтожает иконку панели задач и рамку
        """
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()

    def onMinimize(self, event):
        """
        Во время сворачивания, делаем так, чтобы приложение оставило иконку в трее
        """
        if self.IsIconized():
            self.Hide()


def main():
    """
    Запуск приложения
    :return:
    """

    app = wx.App(False)
    frame = MainFrame()
    ap.main(True)
    # threading_app(True)
    app.MainLoop()


# def threading_app(check):
#     if check:
#         # Запуск генератора паролей в отдельном потоке
#         print('Запуск генератора паролей в отдельном потоке')
#         t = threading.Thread(target=ap.main(True))
#         t.start()


if __name__ == "__main__":
    main()

# This is main start app