from tkinter import*
from tkinter import ttk
import tkinter as tk
import pandas as pd
import win32com.client as win32
import os

class Attendance:
    csv = pd.read_csv('attendance.csv')
    csv.to_excel('attendance.xlsx', index=False)

    win32c = win32.constants
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True
    wb = excel.Workbooks.Open(r'attendance.xlsx')
