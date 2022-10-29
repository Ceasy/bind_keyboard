import threading
import app_trey as at
import keyboard

import wx
import wx.adv
import main as ap
import generator_pass as gp


class CustomTaskBarIcon(wx.adv.TaskBarIcon):
    """"""

    def __init__(self, frame):
        """Constructor"""
        wx.adv.TaskBarIcon.__init__(self)
        self.enable = None
        self.is_checked = True
        self.frame = frame

        icon = wx.Icon('Z:\\Files\\PYTHON\\bind_keyboard\\ico\\key_treey.ico', wx.BITMAP_TYPE_ICO)

        self.SetIcon(icon, "Pwd Generator")

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.OnTaskBarRightClick)

    def OnTaskBarActivate(self, evt):
        """Проверка активно ли меню"""

        if self.is_checked:

            self.is_checked = False
            ap.main(False)
        else:
            self.is_checked = True
            # at.threading_app(True)
            ap.main(True)

    def OnAbout(self, evt):
        """
        Создаёт диалоговое окно "About"
        """
        dlg = wx.MessageDialog(self.frame,
                               "Это простое приложение, которое позволяет вам генерировать пароли и вводить их в "
                               "любое приложение.\n Для генерации пароля, нажмите Numpad 7. Для того чтобы отключить "
                               "генератор нажмите NumLock или в меню трея нажмите на пункт Enable.\n"
                               "Автор: Алексей "
                               "Федотов"" ",
                               "About Pwd Generator.\n Version 1.0",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnTaskBarClose(self, evt):
        """
        Уничтожает иконку панели задач и рамку в самой иконке панели задач
        """

        self.frame.Close()


    def OnTaskBarLeftClick(self, evt):
        """
        Создаёт меню, которое появляется при нажатии левой кнопки мыши.
        """
        self.frame.Show()
        self.frame.Restore()

    def OnTaskBarRightClick(self, evt):
        """
        Создаёт меню, которое появляется при нажатии правой кнопки мыши.
        """
        menu = wx.Menu()
        menu.AppendSeparator()
        self.m_enable = menu.AppendCheckItem(wx.ID_ANY, "Enable")
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, self.m_enable)
        if self.is_checked:  # Проверка активно ли меню
            self.m_enable.Check(True)
        else:
            self.m_enable.Check(False)

        menu.AppendSeparator()
        # Добавляем пункт меню "About"
        menu.Append(wx.ID_ABOUT, "About")
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)

        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit")
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=wx.ID_EXIT)

        self.PopupMenu(menu)
        menu.Destroy()
